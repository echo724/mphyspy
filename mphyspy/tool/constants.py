from mphyspy import test

test.check()

#mphyspy/quantum/constants.py
import numpy as np
#Constants

def test():
    print("This is constants module test")

#plank's constant
h = 6.62607015*pow(10,-34)

#reduced Plank's constant
hbar = h / (2*np.pi)

#charge of electron
elect_q = - 1.60217662*pow(10,-19)

#mass of electron in kg
elect_kg = 9.1093837015*pow(10,-31)
#mass of electron in atomic mass u
elect_u = 5.48579909070*10**-4

#mass of proton in kg
proton_kg = 1.672623*pow(10,-27)
#mass of proton in u
proton_u = 1.007276466621
#in Mev
proton_Mev = 0.9382720813*10**3

#speed of light in m/s
c = 2.99792458*pow(10,8)

#mass of neutron in kg
neutron_kg = 1.674929*pow(10,-27)
# mass of neutron in u
neutron_u = 1.008665
# in Mev
neutron_Mev=0.9395654133*10**3

# mass of hydrogen(u)
hydrogen_u=1.00782503207

#mass of Helium(u)
helium_u = 4.002603

#fine structure constant
g=2.002319

#bohr radius in m
bohr_r=0.0529*10**-9

#energy equivalent(eV)
#electron
elect_e=511*10**3
#proton_energy
proton_e=938*10**6

#hc value(eV*nm)
hc=1240

#coulomb's constant
ke=8.987551787*10**9

#boltzbam constant
kb=1.38*10**-23

##Particles(Gev)
#Muon
mu=0.105658

#Pion
pi_0=0.134977
pi_p=0.13957061
pi_n=0.13957061

#electron
elect_Gev=5.109989461*10**-4

#light-year(m)
ly=9.46*10**15

#Solar System mass
#Solar mass(kg)
sm = 1.98847*10**30
#Earth mass(kg)
em = 5.972*10**24

#Earth radius(km)
er = 6371

#Wein's Law Constant(m*K)
wl = 2.898*10**-3
