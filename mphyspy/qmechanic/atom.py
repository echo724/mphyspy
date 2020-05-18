#mphyspy/quantum/atom.py
import mphyspy.tool.constants as ct
import numpy as np
from mphyspy import test

test.check()

def states(n):
    total = 0
    for i in range(n):
        total += 2 * i + 1
    states = total * 2
    return states

#Finding angular momentum
def angular_p(l):
    L = np.sqrt(l*(l+1))*ct.hbar
    return L

def spin_p(s):
    S = np.sqrt(s*(s+1))*ct.hbar
    return S

def energy(n):
    e=-13.6/n**2
    return e

def tunneling():
    E=float(input("Kinetic E: "))
    U=float(input("Potential E: "))
    m=float(input("Mass: "))
    L=float(input("Width: "))

    a=np.sqrt(2*m*(U-E))/ct.hbar
    T=16*(E/U)*(1-E/U)*np.exp(-2*a*L)
    return T

def bremsstrahlung():
    type=input("Z or f: ")
    if type == 'f':
        Z=int(input("Z: "))
        result=(3*13.6/(4*ct.h))*(Z-1)**2
    else:
        f=float(input("f: "))
        result=np.sqrt(f*4*ct.h/(3*13.6))+1
    print("{0}: {1}".format(type,result))
    return result
