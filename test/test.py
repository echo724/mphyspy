from mphyspy.matrix import matrix
from mphyspy.quantum import atom
from mphyspy.quantum import constants
from mphyspy.quantum import quantum
from mphyspy.quantum import schrodinger
from mphyspy.srelativity import srelativity

def test():
    matrix.test()
    atom.test()
    constants.test()
    quantum.test()
    schrodinger.test()
    srelativity.test()

if __name__ == '__main__':
    test()
