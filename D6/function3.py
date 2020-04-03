"""python的内置函数"""

def myfilter(mystr):
    return len(mystr) == 6

print(chr(0x9a86))
print(hex(ord('骆')))
print(abs(-1.2345))

print(pow(1.2345, 5))
print(round(-1.6))
fruits = ['orange', 'durian', 'watermlon']
print(fruits[slice(1,3)])
fruits2 = list(filter(myfilter, fruits))
print(fruits)
print(fruits2)

