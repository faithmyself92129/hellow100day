"""输出10行杨辉三角"""

def main():
    num = 5
    yh = [[]]* num
    for row in range(len(yh)):
        yh[row] = [None] * (row + 1)
        for col in range(len(yh[row])):
            if col ==0 or col ==row:
                yh[row][col] =1
            else:
                yh[row][col] = yh[row-1][col] + yh[row - 1][col - 1]
            print(yh[row][col], end='\t')
        print()

if __name__ == '__main__':
    main()





