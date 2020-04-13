"""写入CSV文件"""

import csv

class Teacher(object):
    def __init__(self, name, age, title):
        self.__name = name
        self.__age = age
        self.__title = title
        self.__index = -1

    def name(self):
        return  self.__name

    def age(self):
        return  self.__age
    def title(self):
        return self.__title

filename = 'teacher.csv'
teachers = [Teacher('罗浩',38,'教授'), Teacher('狄仁杰',33, '判官')]
try:
    with open(filename, 'w') as f:
        writer = csv.writer(f)
        for teacher in teachers:
            writer.writerow([teacher.name(), teacher.age(), teacher.title()])
except BaseException as e:
    print('无法写入文件', filename)
else:
    print('保存数据完成！')



