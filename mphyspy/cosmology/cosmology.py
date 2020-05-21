import mphyspy.tool.constants as ct
import mphyspy.tool.geometry as gm
from mphyspy import test

test.check()

#Relativistic Doppler Shift
#rds
#input: lambda_s, lambda_o
#output: velocity
def rds(s,o):
    rel=(o/s)**2
    v = ct.c*(rel-1)/(rel+1)
    return v

#Wein's Law
#wein
#input: Temperature or Wavelength
#output: Wavelength or Temperature
def wein(input):
    output = ct.wl / input
    return output

#Parsec Function
#input: distance from the star
#output: distance in parsec
def pc(distance):
    arcsec = 3.26/distance
    print("{0}".format(arcsec))
    pc = 1/arcsec
    return pc

#Average Density
#input: Star mass, radius
#output: density of star
def average_density(m,r):
    p = m/gm.sphere_v(r)
    return p
