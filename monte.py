import random
from decimal import *
getcontext().prec = 1000
counter = 0

N = 1000000000
for i in range(N):
    x = Decimal(random.random())
    y = Decimal(random.random())
    if x*x + y*y < Decimal(1.0):
        counter += 1
    pi = Decimal(4.0)*Decimal(counter)/Decimal(N)
    print(Decimal(pi))
