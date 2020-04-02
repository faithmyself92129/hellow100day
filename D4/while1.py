"""用while循环实现1-100求和"""
sum = 0
num = 1
while num <= 100:
    sum += num
    num +=1
print(sum)

"""1-100偶数求和"""
sum = 0
num = 1
while num <= 100:
    if num %2 == 0:
        sum += num
        num += 1
    else:
        num += 1
        continue
print(sum)

