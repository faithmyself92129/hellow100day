"""求最大公约数和最小公倍数的函数"""
import math
def gys(x, y):
    if x > y:
        x, y = y, x
    for i in range(int(math.sqrt(x))+1,1,-1 ):
        if x%i ==0 and y%i ==0:
            return i

def gbs(x, y):
    return x*y//gys(x, y)

print(gys(15,12))
print(gbs(15,12))


