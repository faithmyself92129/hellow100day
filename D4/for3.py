"""输入非负整数n，计算N!"""
n = int(input("输入一个非负整数："))
m = 1
for i in range(1,  n+1):
    m *= i
print('%d!= %d' % (n, m))

