import os
str = 'hello, world'
print('字符串的长度是：', len(str))
print("字符串首字母大写：", str.title())
print("字符串变大写：", str.upper())

print("字符串是不是大写：", str.isupper())
print("字符串是不是以hello开头：", str.startswith('hello'))
print('字符串是不是以hello结尾', str.endswith('3'))
print('字符串是不是以感叹号结尾：', str.endswith('fg'))
str2 = '- \u9a86\u660a'
str3 = str.title() + ''+ str2.lower()
print(str3)
