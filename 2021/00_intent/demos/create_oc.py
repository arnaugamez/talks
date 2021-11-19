from z3 import *

X = BitVec('X', 8)
def P(X): return 97*X + 248*X*X
def Q(X): return 161*X + 136*X*X

x = BitVec('x', 8)
y = BitVec('y', 8)
def E(x, y): return x-y + 2*(~x&y) - (x^y)

K = BitVecVal(123, 8)

# Opaque Constant
OC = P(E(x,y) + Q(K))

# Apply basic simplification rules
print (simplify(OC))
