import mphyspy.tool.constants as ct
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

#Parsec Function
#input: distance from the star
#output: distance in parsec
def pc(distance):
    arcsec = 3.26/distance
    print("{0}".format(arcsec))
    pc = 1/arcsec
    return pc
