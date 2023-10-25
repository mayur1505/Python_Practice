#pool arguments
from multiprocessing import Pool


def f(n):
    return n*n

if __name__ == "__main__":
    p = Pool(processes=3)#processes=3 means that the pool will have three worker processes/cores that can execute tasks in parallel
    result = p.map(f,[1,2,3,4,5])
    for n in result:
        print(n)