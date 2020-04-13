"""读取csv文件"""

import csv
filename = 'example.csv'

try :
    with open(filename) as f:
        readr = csv.reader(f)
        data = list(readr)

except FileNotFoundError:
    print('无法打开文件:',filename)
else:
    for item in data:
        print('%-30s%-20s%-10s'%(item[0],item[1],item[2]))




