#pool arguments
from multiprocessing import Pool


def f(n):
    return n*n

if __name__ == "__main__":
    p = Pool(processes=3)#at a time only 3 process will be created 
    result = p.map(f,[1,2,3,4,5])
    for n in result:
        print(n)