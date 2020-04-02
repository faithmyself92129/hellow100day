"""掷骰子决定做什么事情"""
from random import randint
face = randint(1,6)
if face ==1:
    result = "唱首歌"
elif face == 2:
    result = "跳个舞"
else :
    result = "讲笑话"
print(result)
