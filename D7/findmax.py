"""找到列表中最大或是最小的元素"""

def main():
    fruits = ['grape', 'apple', 'strawberry', 'waxberry','pitaya']
    #使用内置函数max和min
    print(max(fruits))
    print(min(fruits))

    max_value = min_value = fruits[0]
    second_max = second_min = fruits[1]
    for index in range(1, len(fruits)):
        if fruits[index] > max_value:
            max_value = fruits[index]

        if fruits[index] < min_value:
            min_value = fruits[index]
    for index in range(1, len(fruits)):
        if second_max < fruits[index] <max_value:
            second_max = fruits[index]
    print('Max: ', max_value)
    print(fruits)
    print('second', second_max)
    print('Min: ', min_value)
    print(fruits)

if __name__ == '__main__':
    main()

