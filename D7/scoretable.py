"""学生成绩表"""

# def main():
#     names = ['关羽', '张飞' ]
#     subjs = ['语文', '数学']
#     scores = [[0]*2]*2
#
#     for row, name in enumerate(names):
#         print('请输入%s的成绩' % name)
#         for col, subj in enumerate(subjs):
#             scores[row][col] = float(input(subj+':'))
#     print(scores)
#
# if __name__ == '__main__':
#     main()


def main():
    names = ['关羽', '张飞', '赵云', '马超', '黄忠']
    subjs = ['语文', '数学', '英语']
    scores = [[0] * 3] * 5
    # for row, name in enumerate(names):
    #     print('请输入%s的成绩' % name)
    #     for col, subj in enumerate(subjs):
    #
    # print(scores)
    for row, name in enumerate(names):
      print('请输入%s的成绩' % name)
      scores[row] = [None] * len(subjs)
      for col, subj in enumerate(subjs):
          score = float(input(subj + ': '))
          scores[row][col] = score
    print(scores)

if __name__ == '__main__':
    main()


