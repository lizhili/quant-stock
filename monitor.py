import tushare as ts
from time import sleep, strftime
import os


from util import pp

olist = ['510300', '600036', '600280', 'sh']
slist = ['sh']

columns = ['name', 'price', 'percent', 'high', 'low', 'time']
f_c = ['price', 'high', 'low', 'pre_close']
r_c = ['high', 'low', 'percent', 'price']
def f2(x):
    return format(x, '.2f')

def get_price_min():
    t = strftime('%Y-%m-%d %H:%M:%S')
    df = ts.get_realtime_quotes(olist)
    for c in f_c:
        df[c] = df[c].astype('float')
    df['percent'] = (df.price/df.pre_close - 1)*100
    df['high'] = (df.high/df.pre_close - 1)*100
    df['low'] = (df.low/df.pre_close - 1)*100
    for c in r_c:
        df[c] = df[c].apply(f2)
    #print(df[columns].head())
    return df[columns]

def main_loop():
    while(1):
        os.system('clear')
        df = get_price_min()
        pp(df)
        sleep(5)

if __name__ == '__main__':
    main_loop()
