import random
from decimal import *
getcontext().prec = 1000
counter = 0

N = 100000 #試行回数であって桁数ではない
for i in range(N):
    x = Decimal(random.random())
    y = Decimal(random.random())
    if x*x + y*y < Decimal(1.0):
        counter += 1
print(Decimal(4.0)*Decimal(counter)/Decimal(N))
    
