import math
a = 1.0
b = math.sqrt(2.0) / 2.0
t = 0.25
p = 1.0

for i in range(4):
    a1 = (a + b) / 2.0
    b1 = math.sqrt(a * b)
    t1 = t - p * (a - a1) **2
    p1 = 2.0 * p

    a = a1
    b = b1
    t = t1
    p = p1

    print((a + b) **2 / 4.0 / t)
