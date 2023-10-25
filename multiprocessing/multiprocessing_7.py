#multiprocessing Lock
#why do we need lock in real life?
#"Bathroom": if one person is inside bathroom then other person can't enter into it because the door is locked
#so bathroom is shared resource with a lock
# similarly in programming world whenever two processes or threads are trying to access a shared resource
# such as a shared memory, file or a database. it can create a problem. so you need to protect that access with a lock

#what happens with we don't provide lock
#let's understand from below code
#this is a banking software program
import time
import multiprocessing

def deposit(balance):#depositing money into bank
    for i in range(100):#we are adding 100 dollars to 200 initial balance
        time.sleep(0.01)
        balance.value = balance.value + 1 #at evey iteration 1 dollar will added


def withdraw(balance):#withdrawing money from the bank
    for i in range(100):#100 dollars will be withdrawn
        time.sleep(0.01)
        balance.value = balance.value - 1 #at evey iteration 1 dollar will withdrawn


if __name__ == '__main__':
    balance = multiprocessing.Value('i', 200)#we are starting with 200 dollers balance
    #multiprocessing.Value is shared memeory resource
    d = multiprocessing.Process(target=deposit, args=(balance,))
    w = multiprocessing.Process(target=withdraw, args=(balance,))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)#printing final balance
    #so ideally we should have 200 dollars left after depositing 100 and withdrawing 100
    #but everytime we run this code , it will print different balance values
    #this happened because balance is shared resource between deposit and withdraw processes and
    #they are tring to access it at the same time, so balance value is not updating in a right way
    #this can be solved using Lock
    #check multiprocessing_8.py

