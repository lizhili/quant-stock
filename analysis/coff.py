import sys
sys.path.append("..")

from utils.select import *
import pandas as pd
import numpy as np



size = 300

sd = getDataFromTable('stock_day')
date = np.sort(sd.idate.unique())[-size:][::-1]

count, fetch = sql.exceQuery('select stock_id from stock_day group by stock_id having count(*) > {}'.format(size))
sids = getDataFromFetch(['id'], fetch)
sids.to_csv('sids_{}.csv'.format(size))
#sids = pd.read_csv('sids_300.csv')

oo = pd.DataFrame(index=sids.id.values, columns=date)

for i in sids.id:
    for d in date:
        print(i, d)
        a = sd.loc[(sd['stock_id'] == i) & (sd['idate'] == d)]
        if a.shape[0] == 1:
            oo.loc[i][d] = a.close_price.values[0]

print(oo.head())

oo.to_csv('{}.csv'.format(size))

oo = pd.read_csv('{}.csv'.format(size))

oo = oo.T
oo = oo.drop(3124, 1)
corr = oo.corr()
corr = corr.replace(to_replace=1, value=0)
print(corr.head())
cov = oo.cov()


