import numpy as np
from mphyspy import test

test.check()

#Voulme
def sphere_v(r):
    v = (4/3)*np.pi*r**3
    return v
#Surface Area
def sphere_a(r):
    a = 4*np.pi*r**2
    return a
#Area
