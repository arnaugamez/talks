from z3 import *
x = BitVec('x', 8)
y = BitVec('y', 8)
E = (x ^ y) + 2*(x & y)
E_simp = x + y
prove (E == E_simp)
