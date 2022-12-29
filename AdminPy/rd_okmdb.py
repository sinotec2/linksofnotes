import MySQLdb
from pandas import *
db = MySQLdb.connect(host="localhost", user="kuang",
passwd="****", db="okmdb",
charset='utf8', port=8080,unix_socket="/var/lib/mysql/mysql.sock"
)
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

pivot_table(df.loc[df.ACT_ACTION=='LOGIN'],index='ACT_USER',values='ACT_ACTION',aggfunc='count').reset_index().sort_values('ACT_ACTION',ascending=False).reset_index(drop=True)
pivot_table(df.loc[df.ACT_ACTION.map(lambda x:'DOCUMENT' in x)],index='ACT_PATH', values='dum',aggfunc='count').reset_index().sort_values('dum',ascending=False).reset_index(drop=True).head(10)