"""输入学生考试成绩计算平均分"""
import os
import time
def main():
    str = "Welcome to 1000 Phone Chengdu Campus "
    while True:
        print(str)
        time.sleep(1)
        str = str[1:] + str[0:1]

        os.system('cls')

if __name__ == '__main__':
    main()

