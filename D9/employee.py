"""抽象类/方法重写/多态"""

from  abc import ABCMeta,abstractmethod

class Employee(object, metaclass=ABCMeta):

    def __init__(self,name):
        self._name = name

    def name(self):
        return self._name

    def get_salary(self):
        pass

class Manager(Employee):

    def __init__(self,name):
        super().__init__(name)

    def get_salary(self):
        return 12000

class Programmer(Employee):
    def __init__(self,name):
        super().__init__(name)

    def set_working_hour(self, working_hour):
        self._working_hour = working_hour

    def get_salary(self):
        return 100*self._working_hour

class Salesman(Employee):
    def __init__(self, name):
        super().__init__(name)

    def set_sales(self, sales):
        self._sales = sales

    def get_salary(self):
        return 1500 + self._sales * 0.05

if __name__ == '__main__':
    emps = [Manager('武则天'), Programmer('狄仁杰'), Salesman('李元峰')]
    for emp in emps:
        if isinstance(emp, Programmer):
            working_hour = int(input("请输入%s工作多长时间：" % emp.name))
            emp.set_working_hour(working_hour)

        elif isinstance(emp, Salesman):
            sales = float(input("请输入%s销售额："% emp.name()))
            emp.set_sales(sales)
        print('%s本月月薪为：%.2f' % (emp.name(), emp.get_salary()))



