from decimal import *
getcontext().prec = 5000


a = Decimal(1.0)
b = Decimal(2.0).sqrt() / Decimal(2.0)
t = Decimal(0.25)
p = Decimal(1.0)

for i in range(100):
    a1 = (a + b) / Decimal(2.0)
    b1 = Decimal(a * b).sqrt()
    t1 = t - p * (a - a1) ** Decimal(2)

    a = a1
    b = b1
    t = t1
    p = Decimal(2.0) * p

print((a + b) ** Decimal(2) / Decimal(4.0) / t)
