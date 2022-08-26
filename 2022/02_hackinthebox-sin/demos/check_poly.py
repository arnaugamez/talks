from z3 import *
X = BitVec('X', 8)

def P(X): return 97*X + 248*X*X
def Q(X): return 161*X + 136*X*X

prove(P(Q(X)) == X)