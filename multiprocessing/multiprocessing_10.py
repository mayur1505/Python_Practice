#we will use some computationally intensive code to compare's pool's performance with serial processing
from multiprocessing import Pool
import time


def f(n):
    sum=0
    for x in range(1000):
        sum += x*x
    return sum

if __name__ == "__main__":

    t1=time.time()
    p=Pool()
    result=p.map(f,range(100000))
    p.close()
    p.join()

    print("Pool took:", time.time() - t1)

    t2 = time.time()
    result=[]
    for x in range(100000):
        result.append(f(x))
    
    print("Serial processing took:", time.time() - t2)

#we can compare times to see the performance
#so by seeing results we can say that using Pool can speed our process
