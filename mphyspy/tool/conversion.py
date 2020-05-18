from mphyspy import test

test.check()

#change mass(u) to binding energy(Mev)
def u_to_Mev(u):
    Mev = 931.5*u
    return Mev

#Mev to u
def Mev_to_u(Mev):
    u = Mev/931.5
    return u

#J to eV
def j_to_ev(joul):
    return joul/(1.602176634*pow(10,-19))
#eV to J
def ev_to_joul(ev):
    return 1.602176634*pow(10,-19)*ev

#kg to u
def kg_to_u(kg):
    u = kg*6.022*10**26
    return u

#u to kg:
def u_to_kg(u):
    kg = 1.66054*10**-27*u
    return kg
