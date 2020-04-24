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
    s = np.random.rand(10)-0.5 # array([ 0.29745375,  0.05835378, -0.20477995, -0.41623986, -0.44001312, 0.42641976,  0.29360252, -0.44805617,  0.19130221, -0.04300323])
    r = ReUnit()
    r.addDirect(1)
    r.addDirect(-1)
    r.addDirect(1)
    r.addDirect(-1)
    r.verify(s)
