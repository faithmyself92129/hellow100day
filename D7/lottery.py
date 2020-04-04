"""双色球随机选号程序"""

from random import randrange, randint, sample

def display(balls):
    """输出列表中的双色球号码"""
    for ball in balls:

 #       if index == len(balls)-1:
 #           print('|', end=' ')

        print('|%02d' % ball, end=' ')
    print()

def random_select():
    """随机选择一组号码"""
    red_balls = [x for x in range(1, 34)]
    selected_balls = []
  #  for _ in range(1):
    index = randrange(len(red_balls))
    selected_balls.append(index)
    del red_balls[index]
        #上面的for循环可以写成sample下的random函数 selected_balls = sample（red_balls,6)
  #  selected_balls.sort()
    selected_balls.append(randint(1, 16))

    return  selected_balls

def main():
    n = 3
    for _ in range(n):
        display(random_select())

if __name__ == '__main__':
    main()


