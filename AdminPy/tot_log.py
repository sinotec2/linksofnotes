#openkm@master ~/tomcat_sino4/scripts/rd_okmdb
#$ cat tot_log.py
#!/home/miniconda/envs/py37/bin/python
# -*- coding: utf-8 -*-
"""

 """
import matplotlib.pyplot as plt
from pandas import *
import MySQLdb, subprocess, os, sys

fname = 'day_tot.csv'
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
    df['count'] = [1 for i in range(len(df))]
    df['date'] = [datetime(Timestamp(i).year, Timestamp(i).month, Timestamp(i).day)
                  for i in df.ACT_DATE]
    df['day'] = [(i - df.loc[len(df) - 1, 'date']).days for i in df.date]

    pv2 = pivot_table(df.loc[df.ACT_ACTION == 'LOGIN'], index=['day'], values='count',
                      aggfunc='count').reset_index().sort_values(['day']).reset_index(drop=True)
# time series plot
fig, ax = plt.subplots()
plt.legend(loc='upper center')
plt.xlabel('Last Days of Working')
plt.ylabel("Daily Total Logins")
ints = [3, 6, 12, 24, 48, 72, 168]
intv = 3

ldays = max(set(list(pv2.day))) - min(set(list(pv2.day))) + 1
for i in range(6, -1, -1):
    if 5 <= ldays / ints[i] <= 20: intv = ints[i]
totalSeed = pv2.index.tolist()
ax.plot(totalSeed, list(pv2['count']), label='count',alpha=0.7)
xticks = list(range(0, len(totalSeed), intv))
#xlabels = [str(i) for i in xticks]
xlabels = [str(abs(list(pv2.day)[i])) for i in xticks]
xlabels.append(str(int(xlabels[-1]) + intv))
ax.set_xticks(xticks)
ax.set_xticklabels(xlabels, rotation=0, fontsize=8)
ax.legend(bbox_to_anchor=(0., 1.08), loc=2, borderaxespad=0., fontsize=9, ncol=5)  # len(nam)
act = 's'
if act[0] == 'plot'[0]: plt.show()
if act[0] == 'save'[0]:
    name = '/home/py_exam/openKM_log/orquestra/static/tot_logs.png'
    plt.savefig(name)
