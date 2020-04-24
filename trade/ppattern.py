class PPattern():
    def __init__(self):
        pass

class ReUnit():
    "+-"
    def __init__(self):
        self.direct = []
    
    def addDirect(self, v):
        self.direct.append(v)
    
    def verify(self, pl):
        flag = True
        p = pl[::-1][:len(self.direct)]
        d = self.direct[::-1]
        for i in range(len(d)):
            if d[i] * p[i] < 0:
                flag = False
                break
        return flag

class PrUnit(ReUnit):
    "+- and threshold"
    def __init__(self, d, t):
        ReUnit.__init__(self)
    
    def setThreshold(self, t):
        self.trh = t
    
    def verify(self, pl):
        ReUnit(self, pl)
  
 if __name__ == '__main__':
    r = ReUnit()
    r.addDirect(1)
    r.addDirect(-1)
    r.addDirect(1)
    r.addDirect(-1)
    r.verify(s)
