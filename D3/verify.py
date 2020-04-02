"""用户身份认证"""

import getpass
from getpass import getpass
from getpass import *

username = input("请输入用户名：")
password = input("请输入密码：")

#password = getpass.getpass("请输入口令：")
if username == "admin" and password == "12345":
    print("验证成功！")
else:
    print("验证失败！")
