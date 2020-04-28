import sympy as sy
import numpy as np
import constants as ct

class MS():
    def __init__(self):
        r_0 = 0
        cm = 0
        I = 0
        el = 0
        ev = 0

    def r(self,r):
        self.r_0 = r
        return self.r_0

    def cm(self,m1,m2):
        self.cm = m1*m2/(m1+m2)
        return self.cm

    def i(self,m):
        self.I = m*self.r_0**2

    def el(self,l):
        self.el = l*(l+1)*ct.hbar**2/(2*self.I)
        return self.el

    def ev(self,v,k):
        self.ev = (v+1/2)*ct.hbar*np.sqrt(k/self.cm)
        return self.ev

    def e(self):
        return self.ev+self.el
