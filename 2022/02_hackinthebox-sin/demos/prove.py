from z3 import *
x = BitVec('x', 8)
y = BitVec('y', 8)

E1 = x + y
E2 = (x ^ y) + 2 * (x & y)
E3 = 151 * (39 * ((x ^ y) + 2 * (x & y)) + 23) + 111

prove (E1 == E2)
prove (E2 == E3)
prove (E3 == E1)

