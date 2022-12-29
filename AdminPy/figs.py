#openkm@master ~/tomcat_sino4/scripts/rd_okmdb
#$ cat figs.py
#!/home/miniconda/envs/py37/bin/python
# -*- coding: utf-8 -*-
"""

 """
import matplotlib.pyplot as plt
from pandas import *
import MySQLdb, subprocess, os

fname = 'day_eff.csv'
try:
    pv2 = read_csv('M2' + fname)
except:
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
    eff_log = [-1 for i in range(len(df))]
    df['count'] = [1 for i in range(len(df))]
    email = read_csv('email.csv')
    email['nam'] = [i.split('@')[0] for i in email.email]
    nam, grp = [], []
    for i in df.ACT_USER:
        try:
            ii = int(i)
        except:
            nam.append(i)
            grp.append(i)
        else:
            nam.append(list(email.loc[email.empno == ii, 'nam'])[0])
            grp.append(list(email.loc[email.empno == ii, 'group'])[0])
    df['nam'], df['grp'] = nam, grp
    df['grp2'] = [i[:3] for i in list(df.grp)]
    df['date'] = [datetime(Timestamp(i).year, Timestamp(i).month, Timestamp(i).day)
                  for i in df.ACT_DATE]
    df['day'] = [(i - df.loc[len(df) - 1, 'date']).days for i in df.date]

    for n in set(list(df.nam)):
        for d in set(list(df.day)):
            boo = (df.day == d) & (df.nam == n)
            idx = df.loc[boo].index
            if len(idx) == 0: continue
            for i in range(len(idx) - 1):
                if df.loc[idx[i], 'ACT_ACTION'] == u'LOGIN':
                    act = df.loc[idx[i + 1], 'ACT_ACTION']
                    if act == u'LOGIN' or act == u'LOGOUT':
                        eff_log[idx[i]] = 0
                    else:
                        eff_log[idx[i]] = 1
            if df.loc[idx[-1], 'ACT_ACTION'] == u'LOGIN':
                eff_log[idx[-1]] = 0
    df['eff_log'] = eff_log

    idx = df.loc[df.grp2 == 'okm'].index
    df.loc[idx, 'grp2'] = ['kua' for i in range(len(idx))]
    idx = df.loc[df.grp2 == 'pen'].index
    df.loc[idx, 'grp2'] = ['air' for i in range(len(idx))]
    pv1 = pivot_table(df.loc[df.eff_log == 0], index=['day', 'grp2'], values='eff_log',
                      aggfunc='count').reset_index().sort_values(['day', 'grp2']).reset_index(drop=True)
    for d in set(list(df.day)):
        a = pv1.loc[pv1.day == d]
        if len(a) == 4: continue
        for i in set(list(df.grp2)):
            if i in set(list(a.grp2)): continue
            pv1 = pv1.append(DataFrame({'day': [d], 'grp2': [i], 'eff_log': [0]}), ignore_index=True)
    pv1 = pv1.sort_values(['day', 'grp2']).reset_index(drop=True)
    pv = pv1
    beg = 1
    for s in set(list(pv.grp2)):
        pvj = pv.loc[pv.grp2 == s].reset_index(drop=True)
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

# time series plot
fig, ax = plt.subplots()
plt.legend(loc='upper center')
plt.xlabel('Last Days of Working')
plt.ylabel("effective logins")
ints = [3, 6, 12, 24, 48, 72, 168]
intv = 3

ldays = max(set(list(pv2.day))) - min(set(list(pv2.day))) + 1
for i in range(6, -1, -1):
    if 5 <= ldays / ints[i] <= 20: intv = ints[i]
totalSeed = pv2.index.tolist()
for c in pv2.columns[1:]:
    ax.plot(totalSeed, pv2.loc[:, c], label=c)
xticks = list(range(0, len(totalSeed), intv))
#xlabels = [str(i) for i in xticks]
xlabels = [str(abs(list(pv2.day)[i])) for i in xticks]
xlabels.append(str(int(xlabels[-1]) + intv))
ax.set_xticks(xticks)
ax.set_xticklabels(xlabels, rotation=0, fontsize=8)
# ax.plot(df['DDHH'], df[SPNAM], label = stn[0])
ax.legend(bbox_to_anchor=(0., 1.08), loc=2, borderaxespad=0., fontsize=9, ncol=5)  # len(nam)
act = 's'
if act[0] == 'plot'[0]: plt.show()
if act[0] == 'save'[0]:
    name = '/home/py_exam/openKM_log/orquestra/eff_logs.png'
    plt.savefig(name)
