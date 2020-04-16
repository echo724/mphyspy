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
elect_m = 9.10938356*pow(10,-31)

#mass of proton in kg
proton_m = 1.6726219*pow(10,-27)

#speed of light in m/s
c = 2.99792458*pow(10,8)

#mass of neutron in kg
neutron_m = 1.674929*pow(10,-27)

#fine structure constant
g=2.002319

#bohr radius in m
bohr_r=0.0529*10**-9

#energy equivalent(eV)
#electron
elect_e=511*10**3
#proton_m
proton_e=938*10**6

#hc value(eV*nm)
hc=1240
