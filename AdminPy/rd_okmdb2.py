#openkm@master ~/tomcat_sino4/scripts/rd_okmdb
#$ cat rd_okmdb2.py
#!/home/miniconda/envs/py27/bin/python
import MySQLdb
from pandas import *
db = MySQLdb.connect(host="localhost", user="kuang", passwd="***", db="okmdb", charset='utf8',port=8080,unix_socket="/var/lib/mysql/mysql.sock" )
cursor = db.cursor()
cursor.execute("SELECT * from OKM_ACTIVITY")
data = cursor.fetchall()
cursor.execute("describe OKM_ACTIVITY")
cols = cursor.fetchall()
cols=[cols[i][0] for i in xrange(len(cols))]
dd={}
for i in xrange(len(cols)):
    dd.update({cols[i]:[data[j][i] for j in xrange(len(data))]})
df=DataFrame(dd)
df['count']=[1 for i in xrange(len(df))]
email=read_csv('email.csv')
email['nam']=[i.split('@')[0] for i in email.email]
nam,grp=[],[]
for i in df.ACT_USER:
  try:
    ii=int(i)
  except:
    nam.append(i)
    grp.append(i)
  else:
    nam.append(list(email.loc[email.empno==ii,'nam'])[0])
    grp.append(list(email.loc[email.empno==ii,'group'])[0])
df['nam'],df['grp']=nam,grp
df1=email.loc[email.chief.map(lambda x:type(x)==str)].reset_index(drop=True)
df1.nam=[i.upper() for i in df1.nam]
chf={i:j for i,j in zip(df1.group,df1.nam)}
df=df.drop(df.loc[df.nam=='kuang'].index).reset_index(drop=True)
df=df.drop(df.loc[df.nam=='okmAdmin'].index).reset_index(drop=True)
pv1=pivot_table(df.loc[df.ACT_ACTION=='LOGIN'],index='nam',values='ACT_ACTION',aggfunc='count').reset_index().sort_values('ACT_ACTION',ascending=False).reset_index(drop=True)
pv2=pivot_table(df.loc[df.ACT_ACTION=='LOGIN'],index='grp',values='ACT_ACTION',aggfunc='count').reset_index().sort_values('ACT_ACTION',ascending=False).reset_index(drop=True)
pv2=pv2.loc[pv2.grp.map(lambda x:x in chf)].reset_index(drop=True)
pv2['chf']=[chf[i] for i in pv2.grp]
print 'total logins= '+str(sum(list(pv1.ACT_ACTION)))
print pv1
print pv2
pv2['div']=[i[:3] for i in pv2.grp]
print pivot_table(pv2,index='div',values='ACT_ACTION',aggfunc='sum').reset_index().sort_values('ACT_ACTION',ascending=False).reset_index(drop=True)
cols=['count','ACT_PATH']
print pivot_table(df.loc[df.ACT_ACTION.map(lambda x:'DOCUMENT' in x)],index='ACT_PATH',values='count',aggfunc='count').reset_index().sort_values('count',ascending=False).reset_index(drop=True)[cols].head(10)
