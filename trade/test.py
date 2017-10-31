import sys
sys.path.append("..")
from utils.select import *
import pandas as pd
import numpy as np
from datetime import datetime
from strategy import *


sd = pd.read_csv('stock_day.csv')

l = sd[sd['stock_id']==2]


for i in range(1,30):
    ll = l[-20-i: -i]
    print(ll.tail(1))
    st = trendsg(10000, ll, 20, 5)
    print('R:',st.getR())
    print('Entry:',st.em())
    #print('Out:', st.om())
    #print('Position:', st.position())
    #print(ll.head(1)['close_price'].values[0])
