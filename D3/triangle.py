"""判定输入的边长能否构建三角形"""
import math

a = float(input("第一个边长a："))
b = float(input('第二个边长b:'))
c = float(input('第三个边长c:'))

if a+b >c and  a+c >b and b+c >a  :
    print('周长：%f' % (a+b+c))
    p = (a+b+c)/2
    area = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print('面积%f' % area)
else:
    print('不构成三角形')


