"""集合的常用操作"""

def main():
    set1 = set(range(1, 7))
    print(set1)

    set2 = set(range(2, 11,2))
    print(set2)
    set3 = set(range(1,  5))
    print(set1 & set2)
    set1.intersection(set2)
    print(set1 | set2)

    print(set1 -set2)

    print(set1 ^ set2)

    print(set2 <= set1)

    print(set3 <= set1)
    print(set3.issubset(set1))

    print(set1 >= set2)

    print(set1 >= set3)
    print(set1.issuperset(set3))

if __name__ == '__main__':
    main()




