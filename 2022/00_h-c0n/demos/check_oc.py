from z3 import *

x = BitVec('x', 8)
y = BitVec('y', 8)

def OC(x, y):
    return 195 + 97*x + 159*y +\
    194*~(x | ~y) + 159*(x ^ y) +\
    (163 + x + 255*y + 2*~(x | ~y) + 255*(x ^ y))*\
    (232 + 248*x + 8*y + 240*~(x | ~y) + 8*(x ^ y))

prove(OC(x, y) == 123)