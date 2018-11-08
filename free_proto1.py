import math
import time
from decimal import *

n = 5000
getcontext().prec = n  # ここで桁数を調整
starttime = time.clock()

a = Decimal(1.0)
b = Decimal(2.0).sqrt() / Decimal(2.0)
t = Decimal(0.25)
p = Decimal(1.0)

for i in range(int(math.log2(n))*2):  # log2(桁数)回より多めに繰り返しましょう
    a1 = (a + b) / Decimal(2.0)
    b1 = Decimal(a * b).sqrt()
    t1 = t - p * (a - a1) ** Decimal(2)

    a = a1
    b = b1
    t = t1
    p = Decimal(2.0) * p

endtime = time.clock()
print((a + b) ** Decimal(2) / Decimal(4.0) / t)

time = endtime - starttime

print("実行時間:%f" % time)
