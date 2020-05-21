import mphyspy.tool.constants as ct
import mphyspy.tool.conversion as cv
import numpy as np
import sympy as sy

#Get totall mass of atom based on u(atomic mass)
def mass(Z,A):
    total_mass = (A-Z)*ct.neutron_u + Z*ct.hydrogen_u
    return total_mass

def radius(A):
    r_0 = 1.2*10**-15
    r = A**(1/3)*r_0
    return r

def be(Z,A):
    c =[15.8,17.8,0.71,23.7,11.18]
    be = c[0]*A-c[1]*A**(2/3)-c[2]*(Z*(Z-1))/(A**(1/3))-c[3]*(A-2*Z)**2/A
    if A % 2 == 0:
        if Z % 2 == 0:
            factor = 1
        else:
            factor = -1
    else:
        factor = 0
    be += factor*c[4]/(A**(1/2))
    return be

def decay_const(t):
    decay_const = np.log(2)/t
    return decay_const

def decay(n0,t_half,t):
    N = n0*np.exp(-decay_const(t_half)*t)
    return N

def reaction_energy(i,f):
    Q = cv.u_to_Mev(i-f)
    return Q

def alpha_decay(i,f):
    Q = cv.u_to_Mev(i-(f+ct.helium_u))
    return Q

def half_life(t):
    decay_rate = np.log(2)/t
    return decay_rate

def remaining_nuclei(N0,dr,t):
    N = N0*np.exp(-dr*t)
    return N
