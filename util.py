from time import strftime

columns = ['', 'name', 'price', 'percent', 'high', 'low', 'time']

def print_down(s):
    print("\033[0;32;40m{}\033[0m".format(s))

def print_up(s):
    print("\033[0;31;40m{}\033[0m".format(s))

def print_same(s):
    print("\033[0;37;40m{}\033[0m".format(s))

def pp(df=None):
    t = strftime('%Y%m%d_%H%M%S')
    print(' \t{:<10}\tprice\tnow\thigh\tlow\ttime'.format('name'))
    df.percent = df.percent.astype('float')
    for index, row in df.iterrows():
        s = '{}\t{:<10}\t{}\t{}\t{}\t{}\t{}'.format(index, row['name'], row.price, row.percent, row.high, row.low, row.time)
        if row.percent > 0:
            print_up(s)
        elif row.percent < 0:
            print_down(s)
        else:
            print_same(s)

if __name__ == '__main__':
    pp()