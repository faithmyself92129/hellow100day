"""属性的使用"""

class Car(object):
    __slots__ = ('_brand', '_max_speed')

    def __init__(self, brand, max_speed):
        self. _brand = brand
        self._max_speed = max_speed

    # def brand(self):
    #     return self._brand

    # def brand(self, brand):
    #     self._brand = brand
    #
    # def brand(self):
    #
    #     del self._brand

    def max_speed(self):
        return  self._max_speed

    def max_speed(self, max_speed):
        if max_speed < 0:
            raise ValueError('Invalid max speed for car')
        self._max_speed = max_speed

    def __str__(self):
        return 'Car :[品牌=%s， 最高时速= %s]' % (self._brand, self._max_speed)

def main():
    car = Car('QQ', 120)
    print(car)

    car._max_speed = 320
    car._brand = 'Benz'

  #  car .current_speed = 80

    print(car)
    #del car._brand
    # 属性的实现
    print(Car.brand)
 #   print(Car.brand.fget)
 #   print(Car.brand.fset)
    print(property(Car.brand, Car.brand))
    # print(Car._brand.fdel)
 #   print(Car._brand(fset))

if __name__ == '__main__':
    main()






