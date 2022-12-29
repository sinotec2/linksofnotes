#openkm@master ~/tomcat_sino4/scripts/rd_okmdb
#$ cat rd_okmdb4.py
#!/home/miniconda/envs/py37/bin/python
import MySQLdb
from pandas import *


def ll2str(ll):
  ss = ''
  for j in range(len(ll)):
    ll[j] = str(ll[j]).replace(' ', '_')
    ss += ll[j] + ' '
  return ss


def df2str(df):
  col=list(df.columns)
  if len(df)==0:
    col='count ACT_PATH ref Name'.split()
  line = ll2str([len(df)] + col) + '\n'
  if len(df)!=0:
    for i in range(len(df)):
      line += ll2str([i] + list(df.loc[i])) + '\n'
  return line


db = MySQLdb.connect(host="localhost", user="kuang", passwd="***", db="okmdb", charset='utf8', port=8080,
                     unix_socket="/var/lib/mysql/mysql.sock")
cursor = db.cursor()
cursor.execute("SELECT * from OKM_ACTIVITY")
data = cursor.fetchall()
cursor.execute("describe OKM_ACTIVITY")
cols = cursor.fetchall()
cols = [cols[i][0] for i in range(len(cols))]
dd = {}
for i in range(len(cols)):
  dd.update({cols[i]: [data[j][i] for j in range(len(data))]})
df = DataFrame(dd)
df['count'] = [1 for i in range(len(df))]
dfm = read_csv('/home/openkm/tomcat/scripts/users/users-exportSino4.csv', delimiter=';')
dfm['nam'] = [i.split('@')[0] for i in dfm.Mail]
rpl = ['USER', 'E1 ', 'E2 ', 'WW ', 'ER ', 'EIA', 'AIR', 'VP', 'PM', 'AQM', 'KO']
for r in rpl:
  dfm.Roles = [i.replace('ROLE_' + r, '') for i in dfm.Roles]
dfm.Roles = [i.replace('ROLE_', '') for i in dfm.Roles]
dfm.Roles = [i.replace('AIRO', 'AIR') for i in dfm.Roles]
dfm.Roles = [i.replace('ADMIN', 'adm') for i in dfm.Roles]
for r in range(10):
  dfm.Roles = [i.replace(' ', '') for i in dfm.Roles]
nam, grp = [], []
for i in df.ACT_USER:
  try:
    ii = int(i)
  except:
    nam.append(i)
    grp.append(i)
  else:
    nam.append(list(dfm.loc[dfm.Id == str(ii), 'nam'])[0])
    grp.append(list(dfm.loc[dfm.Id == str(ii), 'Roles'])[0])
df['nam'], df['grp'] = nam, grp
email = read_csv('email.csv')
df1 = email.loc[email.chief.map(lambda x: type(x) == str)].reset_index(drop=True)
df1.nam = [i.upper() for i in df1.nam]
chf = {i: j for i, j in zip(df1.group, df1.nam)}
df = df.drop(df.loc[df.nam=='kuang'].index).reset_index(drop=True)
df = df.drop(df.loc[df.ACT_USER=='4189'].index).reset_index(drop=True)
df = df.drop(df.loc[df.ACT_USER=='system'].index).reset_index(drop=True)
df = df.drop(df.loc[df.nam == 'okmAdmin'].index).reset_index(drop=True)
#most freq. login, by indivisual
pv1 = pivot_table(df.loc[df.ACT_ACTION == 'LOGIN'], index='nam',
        values='ACT_ACTION', aggfunc='count')\
        .reset_index().sort_values('ACT_ACTION', ascending=False)\
        .reset_index(drop=True)
#most freq. login, by group
pv2 = pivot_table(df.loc[df.ACT_ACTION == 'LOGIN'], index='grp',
        values='ACT_ACTION', aggfunc='count')\
        .reset_index().sort_values('ACT_ACTION', ascending=False)\
        .reset_index(drop=True)
pv2 = pv2.loc[pv2.grp.map(lambda x: x in chf)].reset_index(drop=True)
pv2['chf'] = [chf[i] for i in pv2.grp]
pv2['div'] = [i[:3] for i in pv2.grp]
#most freq. login, by divisions
pv3 = pivot_table(pv2, index='div', values='ACT_ACTION', aggfunc='sum')\
        .reset_index().sort_values('ACT_ACTION',ascending=False)\
        .reset_index(drop=True)
del pv2['div']
cols = ['count', 'ACT_PATH']
#10 most freq. got_doc

#10 most freq. got_doc, today, this 7 days, this 30 days.
df['date']=[datetime(Timestamp(i).year,Timestamp(i).month,Timestamp(i).day)
        for i in df.ACT_DATE]
df['Tdelta']=[df.loc[len(df)-1,'date']-i for i in df.date]
df_yes=df.loc[df.Tdelta <= Timedelta(days= 1)].reset_index(drop=True)
df_07d=df.loc[df.Tdelta <= Timedelta(days= 7)].reset_index(drop=True)
df_30d=df.loc[df.Tdelta <= Timedelta(days=30)].reset_index(drop=True)
pv4=[]
linkH='http://200.200.12.191:8080/OpenKM/index.jsp?uuid='
ldf=[df_yes,df_07d,df_30d,df]
ndf=['yesterday','last 7 days','last 30 days','Since 201907']
for idd in range(len(ldf)):
  dd=ldf[idd]
  if len(dd)==0:
    pv4.append(DataFrame({}))
    continue
  dd_doc=dd.loc[dd.ACT_ACTION.map(lambda x: 'DOCUMENT' in x)]
  if len(dd_doc)==0:
    pv4.append(DataFrame({}))
    continue
  pv  = pivot_table(dd_doc,
        index='ACT_PATH', values='count', aggfunc='count')\
        .reset_index().sort_values('count', ascending=False)\
        .reset_index(drop=True)[cols].head(10)
  pv['ref']=[linkH+list(dd.loc[dd.ACT_PATH==i,'ACT_ITEM'])[0] for i in pv.ACT_PATH]
  Name=[]
  for i in list(pv.ACT_PATH):
    dfa=dd.loc[dd.ACT_PATH==i]
    pva=pivot_table(dfa,
        index='ACT_USER', values='count', aggfunc='count')\
        .reset_index().sort_values('count', ascending=False)\
        .reset_index(drop=True).head(1)
    Name.append(list(dfm.loc[dfm.Id==list(pva.ACT_USER)[0],'Name'])[0])
  pv['Name']=Name
# pv['day']=[ndf[idd] for i in pv.ACT_PATH]
  pv4.append(pv)
with open('rd_okmdb.txt', 'w', encoding="utf-8") as f:
  f.write('total logins= ' + str(sum(list(pv1.ACT_ACTION))) + '\n')
  f.write(df2str(pv1))
  f.write(df2str(pv2))
  f.write(df2str(pv3))
  for i in range(len(pv4)):
    f.write(df2str(pv4[i]))
