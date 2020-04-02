"""输入一个正整数判定他是不是素数"""
from math import  sqrt
num = int(input("输入一个正整数："))
end = int(sqrt(num))
is_prime = True
for i in range(2, end+1):
    if num % i == 0:
        is_prime = False
        break
if is_prime :
    print("是素数！")
else:
    print("不是素数！")


