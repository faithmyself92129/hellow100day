"""函数的参数"""

def f1(a, b=5, c =10):
    return a+b*2+c*3
print(f1(1,2,3))
print(f1(100,200))
print(f1(100))
print(f1(c=2, b= 3, a=1))

def f2(*args):
    sum = 0
    for num in args:
        sum += num
    return  sum
print(f2(1,2,3))
print(f2(1,2,3,4,5))
print(f2())


#关键字参数
def f3(**kw):
    if 'name' in kw:
        print('欢迎你%s' % kw['name'])
    elif 'tel' in kw:
        print('你的联系电话是：%s' % kw['tel'])
    else:
        print('没有找到你的个人信息！')

param = {'name':'zhaojianghua', 'age':27}
f3(**param)
f3(name='zhaojianghua',age=27,tel="123456789")
f3(user="zhaojianghua",age=27,tel='123456789')
f3(user='zhaojianghua', age =27, mobile='123456789')




