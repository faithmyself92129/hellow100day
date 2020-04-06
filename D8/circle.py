"""修一个游泳池"""
import math
class Circle(object):
    def __init__(self, radius):
        self._radius = radius

    def radius(self):
        return  self._radius

    def radius(self, radius):
        self._radius = radius if radius > 0 else 0

    def perimeter(self):
        return 2* math.pi *self._radius

    def area(self):
        return math.pi*self._radius*self._radius

if __name__ == '__main__':
    radius = float(input("请输入游泳池的半径："))
    small = Circle(radius)
    big = Circle(radius + 3)
    wall = big.perimeter()*32.5
    road =(big.area() - small.area())*25
    print('围墙的造价为：%.1f元' % wall)
    print('过道的造价为：%.2f元' % road)







