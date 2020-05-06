import sympy as sy
import numpy as np
import mphyspy.qmechanic.constants as ct

class Molecule():
    def __init__(self):
        r_0 = 0
        cm = 0
        I = 0
        el = 0
        ev = 0
        w = 0

    def r(self,r):
        self.r_0 = r
        return self.r_0

    def cm(self,m1,m2):
        self.cm = m1*m2/(m1+m2)
        self.i(self,cm)
        return self.cm

    def i(self,m):
        self.I = m*self.r_0**2
        return self.I

    def el(self,l):
        self.el = l*(l+1)*ct.hbar**2/(2*self.I)
        return self.el

    def w(self,k):
        self.w = np.sqrt(k/cm)
        return w

    def ev(self,v):
        self.ev = (v+1/2)*ct.hbar*self.w
        return self.ev

    def e(self):
        return self.ev+self.el

m = Molecule()

def ave_e(T):
    e = 3/2*ct.kb*T
    return e
