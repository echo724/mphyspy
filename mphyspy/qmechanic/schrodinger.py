#mphyspy/quantum/schrodinger.py
import sympy as sy
import numpy as np
import mphyspy.tool.constants as ct
from mphyspy import test

test.check()

#get Schrodinger wave function in 1D
def wavefunction(L,n):
    x = sy.Symbol('x')
    f=sy.sqrt(2/L)*sy.sin(n*np.pi*x/L)
    return f

def normalize(f):
    nf=r**2*np.abs(f)**2
    return nf

#average radius of 3D Schrodinger Equation
def ave_radius(f):
    r = sy.Symbol('r')
    a = sy.Symbol('a')
    ave= sy.integrate(r*normalzie(f),(r,0,sy.oo))
    return ave

def prob_radius(f,b,c):
    r = sy.Symbol('r')
    a = sy.Symbol('a')
    prob = sy.integrate(normalize(f),(x,b,c))
    return prob

#Schrodinger's Probability Function
def prob(function,a,b):
    x = sy.Symbol('x')
    normal = np.abs(function)**2
    prob = sy.integrate(normal, (x, a,b))
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
