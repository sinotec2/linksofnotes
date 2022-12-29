#openkm@master ~/tomcat_sino4/scripts/rd_okmdb
#$ cat daily_ana.py
#!/home/miniconda/envs/py37/bin/python
# -*- coding: utf-8 -*-
"""

 """
import matplotlib.pyplot as plt
from pandas import *
import MySQLdb, subprocess, os, sys

fname = 'day_tot.csv'
db = MySQLdb.connect(host="localhost", user="kuang", passwd="yck4139", db="okmdb", charset='utf8', port=8080,
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
df['date'] = [datetime(Timestamp(i).year, Timestamp(i).month, Timestamp(i).day)
                  for i in df.ACT_DATE]
df['day'] = [(i - df.loc[len(df) - 1, 'date']).days for i in df.date]

pv2 = pivot_table(df.loc[df.ACT_ACTION == 'LOGIN'], index=['day'], values='count',
                      aggfunc='count').reset_index().sort_values(['day']).reset_index(drop=True)
pv2.set_index('day').to_csv('M2' + fname)

email = read_csv('email.csv')
email['nam'] = [i.split('@')[0] for i in email.email]
dfm = read_csv('/home/openkm/tomcat/scripts/users/users-exportSino4.csv', delimiter=';')
dfm=dfm.loc[dfm.Id.map(lambda x:x[0] in ['3','4','5','6','7','8'])].reset_index(drop=True)
dfm.Id=[int(i) for i in dfm.Id]
rpl = ['USER', 'E1 ', 'E2 ', 'WW ', 'ER ', 'EIA', 'AIR', 'VP', 'PM', 'AQM', 'KO']
for r in rpl:
  dfm.Roles = [i.replace('ROLE_' + r, '') for i in dfm.Roles]
dfm.Roles = [i.replace('ROLE_', '') for i in dfm.Roles]
dfm.Roles = [i.replace('ADMIN', 'adm') for i in dfm.Roles]
for r in range(10):
  dfm.Roles = [i.replace(' ', '') for i in dfm.Roles]

df1 = email.loc[email.chief.map(lambda x: type(x) == str)].reset_index(drop=True)
grp, lev = [], []
for i in df.ACT_USER:
    try:
        ii = int(i)
    except:
        grp.append(i)
        lev.append('adm')
    else:
        grp.append(list(dfm.loc[dfm.Id == ii, 'Roles'])[0])
        if ii in set(list(df1.empno)):
            lev.append('chf')
        else:
            lev.append('eng')
df['grp'], df['lev'] = grp, lev
df['grp2'] = [i[:3] for i in list(df.grp)]

eff_log = [-1 for i in range(len(df))]
for n in set(list(df.ACT_USER)):
    for d in set(list(df.day)):
        boo = (df.day == d) & (df.ACT_USER == n)
        idx = df.loc[boo].index
        if len(idx) == 0: continue
        for i in range(len(idx) - 1):
            if df.loc[idx[i], 'ACT_ACTION'] == u'LOGIN':
                act = df.loc[idx[i + 1], 'ACT_ACTION']
                if act == u'LOGIN' or act == u'LOGOUT':
                    eff_log[idx[i]] = 0 #non_effective login
                else:
                    eff_log[idx[i]] = 1 #effective login
        if df.loc[idx[-1], 'ACT_ACTION'] == u'LOGIN':
            eff_log[idx[-1]] = 0
df['eff_log'] = eff_log

idx = df.loc[df.grp2 == 'okm'].index
df.loc[idx, 'grp2'] = ['kua' for i in range(len(idx))]
idx = df.loc[df.grp2 == 'pen'].index
df.loc[idx, 'grp2'] = ['air' for i in range(len(idx))]
idx = df.loc[df.grp2 == ''].index
df = df.drop(idx).reset_index(drop=True)
fname = 'day_lev.csv'
pv1 = pivot_table(df.loc[df.eff_log == 1], index=['day', 'lev'], values='eff_log',
                  aggfunc='count').reset_index().sort_values(['day', 'lev']).reset_index(drop=True)
#fill zero
for d in set(list(df.day)):
    a = pv1.loc[pv1.day == d]
    for i in set(list(df.lev)):
        if i in set(list(a.lev)): continue #with data, skip
        pv1 = pv1.append(DataFrame({'day': [d], 'lev': [i], 'eff_log': [0]}), ignore_index=True)
pv1 = pv1.sort_values(['day', 'lev']).reset_index(drop=True)
beg = 1
for s in set(list(pv1.lev)):
    pvj = pv1.loc[pv1.lev == s].reset_index(drop=True)
    col = ['day', 'eff_log']
    pvj = pvj[col]
    col = ['day', s]
    pvj.columns = col
    if beg == 1:
        beg = 0
        pv2 = pvj
        continue
    else:
        pv2 = merge(pv2, pvj, on=['day'])
pv2.set_index('day').to_csv('M2' + fname)

fname = 'day_eff.csv'
pv1 = pivot_table(df.loc[df.eff_log == 1], index=['day', 'grp2'], values='eff_log',
                      aggfunc='count').reset_index().sort_values(['day', 'grp2']).reset_index(drop=True)
for d in set(list(df.day)):
    a = pv1.loc[pv1.day == d]
    if len(a) == 4: continue
    for i in set(list(df.grp2)):
        if i in set(list(a.grp2)): continue
        pv1 = pv1.append(DataFrame({'day': [d], 'grp2': [i], 'eff_log': [0]}), ignore_index=True)
pv1 = pv1.sort_values(['day', 'grp2']).reset_index(drop=True)
beg = 1
for s in set(list(pv1.grp2)):
    pvj = pv1.loc[pv1.grp2 == s].reset_index(drop=True)
    col = ['day', 'eff_log']
    pvj = pvj[col]
    col = ['day', s]
    pvj.columns = col
    if beg == 1:
        beg = 0
        pv2 = pvj
        continue
    else:
        pv2 = merge(pv2, pvj, on=['day'])
pv2.set_index('day').to_csv('M2' + fname)
