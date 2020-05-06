
#change mass(u) to binding energy(Mev)
def binding_energy(e):
    be = 931.5*e
    return be

#J to eV
def ev(joul):
    return joul/(1.602176634*pow(10,-19))
#eV to J
def joul(ev):
    return 1.602176634*pow(10,-19)*ev

#kg to u
def u(kg):
    u = kg*6.022*10**26
    return u

#u to kg:
def kg(u):
    kg = 1.66054*10**-27*u
    return kg
