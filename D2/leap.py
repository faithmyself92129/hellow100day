year = int(input('请输入年份：'))
#
# is_leap = (year%4 == 0 and year %100 != 0 or year%400 == 0)
# print(is_leap)

if (year%4 == 0 and year% 100!= 0 ):
    print("ture")
elif year%400 ==0 :
    print("ture")
else:
    print("false")

