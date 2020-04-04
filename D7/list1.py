"""定义和使用列表"""

def main():
    fruits = ['grape', '@pple','strawberry', 'waxberry']
    print(fruits)
    #通过下标访问元素
    print(fruits[0])
    print(fruits[1])
    print(fruits[-1])
    print(fruits[-2])

    fruits[1] = 'apple'
    print(fruits)

    fruits.append('pitaya')
    fruits.insert(0, 'banana')
    print(fruits)

    del fruits[1]
    fruits.pop()
    fruits.pop(0)
    fruits.remove('apple')
    print(fruits)

if __name__ == "__main__":
    main()

