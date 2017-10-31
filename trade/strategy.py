import pandas as pd

class strategy():
    def __init__(self, total, lc):
        self._total = total
        self._lc = lc

    def em(self):
        pass

    def om(self):
        pass

    def getR(self):
        pass
    
    def position(self):
        pass


class trendsg(strategy):
    def __init__(self, total, l, big, small):
        self._total = total
        self._l = l
        self._lc = l['close_price'].values
        self._big = big
        self._small = small
        self.R = 0
        self._limit = 0.025

    def em(self):
        mb = pd.rolling_mean(self._lc, self._big)
        ms = pd.rolling_mean(self._lc, self._small)
        if mb[-1] <= ms[-1]:
            return False
        else:
            return True

    def om(self):
        if self.R == 0:
            print('you need computer R first by call self.getR')
            return 
        return self._lc[-1] - self.R

    def getR(self):
        for idx, one in self._l.iterrows():
            self.R = self.R + one['high'] - one['low'] - abs(one['open_price']-one['close_price'])
        self.R /= len(self._l)
        return self.R

    def position(self):
        if self.R == 0:
            print('you need computer R first by call self.getR')
            return 
        one = self.R * 100
        return (int)(self._total * self._limit/ one)
        
