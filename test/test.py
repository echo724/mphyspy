from matrix import ma
from quantum import atom
from quantum import constants
from quantum import quantum
from quantum import schrodinger
from srelativity import srelativity

def test():
    ma.test()
    atom.test()
    constants.test()
    quantum.test()
    schrodinger.test()
    srelativity.test()

if __name__ == '__main__':
    test()
