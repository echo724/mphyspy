#mphyspy/quantum/atom.py
import mphyspy.qmechanic.constants as ct
import numpy as np

def test():
    print("This is atom module test")

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
