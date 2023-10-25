#using lock to update balance rightly
import time
import multiprocessing

def deposit(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()#to put lock
        #below line/code is 'critical section'
        balance.value = balance.value + 1 #whatever part of code which is accessing shared resource which we want to protect is "critical section"
        lock.release()#to release lock

def withdraw(balance, lock):
    for i in range(100):
        time.sleep(0.01)
        lock.acquire()#to put lock
        #below line/code is 'critical section'
        balance.value = balance.value - 1  #whatever part of code which is accessing shared resource which we want to protect is "critical section"
        lock.release()#to release lock

if __name__ == '__main__':
    balance = multiprocessing.Value('i', 200)
    lock = multiprocessing.Lock() #this is the way to create the lock 
    d = multiprocessing.Process(target=deposit, args=(balance,lock))#passing the lock
    w = multiprocessing.Process(target=withdraw, args=(balance,lock))#passing the lock 
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)