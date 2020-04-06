"""定义和使用学生类"""
class Student(object):
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def study(self, course_name):
        self._course_name = course_name
        print('%s 正在学习%s.' % (self._name, self._course_name))

    def watch_av(self):
        if self._age < 18:
            print('%s 正在看熊出没。' % self._name)
        else:
            print('%s 正在看岛国大片。' % self._name)

def main():
    stu1 = Student('罗浩', 29)
    stu1.study('python 程序设计')
    stu1.watch_av()

    stu2 = Student('王大锤', 10)
    stu2.study('ssssss')
    stu2.watch_av()

if __name__ == '__main__':
    main()

