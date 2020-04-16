#mphyspy/quantum/schrodinger.py
import sympy as sy
import numpy as np
import mphyspy.qmechanic.constants as ct

def test():
    print("This is schrodinger module test")

#get Schrodinger wave function in 1D
def wavefunction(L,n):
    x = sy.Symbol('x')
    f=sy.sqrt(L/2)*sy.sin(n*sy.pi*x/L)
    return f

#Schrodinger's Probability Function
def prob(function,a,b):
    x = sy.Symbol('x')
    prob = sy.integrate(function, (x, a,b))
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
