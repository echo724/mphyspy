#mphyspy/quantum/schrodinger.py
import scipy.integrate as integrate
import numpy as np
import mphyspy.qmechanic.constants as ct

def test():
    print("This is schrodinger module test")

#Schrodinger's Probability Function
def prob(function,a,b):
    prob = integrate.quad(function,a,b)
    return prob

#Return uncertainty when one of values is given
def uncertainty(x):
    y = ct.barh/(2*x)
    return y

#Return velocity from uncertainty eq
def vel(m,x):
    v = ct.barh/(2*m*x)
    return v

#Return Kinetic energy from mass and momentum
def kinetic(p,m):
    k = p**2/(2*m)
    return k

#Return energy from given quantum number
def energy(n,m,l):
    e = n**2*np.pi**2*ct.hbar**2/(2*m*(l**2))
    return e
