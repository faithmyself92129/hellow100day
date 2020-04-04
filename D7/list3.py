"""生成列表"""

def fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b ,a+b
        yield a

def main():
    #用range创建数值列表
    gen = (m + n for m in 'ABCDEFG' for n in '12345')
    print(gen)

    for elem in gen:
        print(elem, end=' ')
    print()
    gen = fib(20)
    print(gen)

    for elem in gen:
        print(elem, end=' ')
    print()

if __name__ == "__main__":
    main()




