#sharing data between processes using queue
#please refer to word file named "multiprocessing_2" in Theory folder
#queue is basically shared memory

import multiprocessing

#process 2:child process
def calc_square(numbers, q):#queue variable is passed 

    for n in numbers:
        q.put(n*n)#queue is data structure which is first in first out(FIFO)
                 #in queue we insert data from the end and pull from the front

#process 1:parent Process
if __name__ == "__main__":
    arr = [2,3,8]
    q = multiprocessing.Queue()#queue variable created using multiprocessing queue class
    #queue will be used to share data between both the processes
    p1 = multiprocessing.Process(target=calc_square, args=(arr,q))
    p1.start()
    p1.join()

    while q.empty() is False: #empty is a method in queue which tells wheather the queue is empty or not
        print(q.get())

#In Python there is one module named "queue" and it is different than "multiprocessing Queue"
#check the word file named "multiprocessing_2" in Theory folder
