import sympy as sy
import numpy as np
import mphyspy.tool.constants as ct
from mphyspy import test

test.check()

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

def N(n):
    N = 2*(1/8)*((4/3)*np.pi*n**3)
    return N

def fermi_energy(m,N,L):
    Ef=ct.h**2/(8*m)*(3*N/(np.pi*L**3))**(2/3)
    return Ef

def average_energy(Ef):
    ave_e = 3/5*Ef
    return ave_e

def fermi_dirac_dist(E,Ef,T):
    f = 1/(np.exp((E-Ef)/(ct.kb*T))+1)
    return f
