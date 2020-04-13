"""多个线程共享数据- 没有锁的情况"""

from time import sleep
from threading import  Thread,Lock

class Account(object):
    def __init__(self):
        self._balance = 0
        self._lock = Lock()

    def deposit(self, money):
        #先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            new_balance = self._balance + money
            sleep(0.01)
            self._balance = new_balance
        finally:
            #这段代码房子finally中保证释放锁的操作一定能够要执行
            self._lock.release()

    def balance(self):
        return self._balance
class AddMoneyThread(Thread):
    def __init__(self, account, money):
        super().__init__()
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)

def main():
    account = Account()
    threads = []
    #创建100个存储的线程想同一个账号中存钱
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
        #等所有存款的线程都执行完
    for t in threads:
        t.join()
    print("账户余额为：￥%d元" % account.balance())
if __name__ == '__main__':
    main()





