import math
import time
from decimal import *

print("桁数を入力")
m = input(">>")  #入力を要求
n = int(m)   #整数型に変換
getcontext().prec = n  # ここで桁数を調整
print("checkpoint0")


a = Decimal(1.0)
b = Decimal(2.0).sqrt() / Decimal(2.0)
t = Decimal(0.25)
p = Decimal(1.0)
print("checkpoint1")

starttime = time.clock()
for i in range(int(math.log2(n))+2):  # log2(桁数)回より多めに繰り返しましょう
    print("%d回目の試行中" % i)
    a1 = (a + b) / Decimal(2.0)
    b1 = Decimal(a * b).sqrt()
    t1 = t - p * (a - a1) ** Decimal(2)

    a = a1
    b = b1
    t = t1
    p = Decimal(2.0) * p


endtime = time.clock()
print("checkpoint2")
print((a + b) ** Decimal(2) / Decimal(4.0) / t)

time = endtime - starttime

print("実行時間:%f" % time)
