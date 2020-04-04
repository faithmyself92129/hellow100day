"""元祖的定义和使用"""

def main():
    t = ('赵江华', 28, True, '河南郑州')
    print(t)

    print(t[0])
    print(t[1])
    print(t[2])
    print(t[3])

    for member in t:
        print(member)

    t = ('王大锤', 20, True, '云南昆明')
    print(t)

    #元祖和列表的转换
    person = list(t)
    print(person)
    person[0] = '李小龙'
    person[1] = 25
    print(person)

    fruits_list = ['apple', 'banana', 'orange']
    fruits_tuple = tuple(fruits_list)
    print(fruits_list)
    print(fruits_tuple)

    print(fruits_list[1])

if __name__ == '__main__':
    main()

