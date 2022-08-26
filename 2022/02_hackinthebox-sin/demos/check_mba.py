from z3 import *
x = BitVec('x', 8)
y = BitVec('y', 8)

def E(x, y): return x-y + 2*(~x&y) - (x^y)

prove(E(x, y) == 0)