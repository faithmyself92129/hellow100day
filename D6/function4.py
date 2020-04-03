import time
import shutil
import os

seconds = time.time()
print(seconds)
localtime = time.localtime(seconds)
print(localtime)
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)
asctime = time.asctime(localtime)
print(asctime)
strtime = time.strftime('%Y-%m-%d %H:%M:%S',localtime)
print(strtime)
mydate = time.strptime( '2018-1-1','%Y-%m-%d')
print(mydate)


shutil.copy('D:/test_11/m2.txt', 'D:/test_11/rr.txt')
os.system('ls -l')
os.chdir('D:/test_11/')
os.system('ls -l')
os.mkdir('test')


