#Multiprocessing Pool (Map Reduce)

'''
def f(n):
    return n*n

if __name__ == "__main__":
    array=[1,2,3,4,5]

    result=[]
    for n in array:
        result.append(f(n))

    print(result)'''

#for theory check multiprocessing_3 in Theory folder

#now we wil implement multiprocessing pool

from multiprocessing import Pool


def f(n):
    return n*n

if __name__ == "__main__":
    array=[1,2,3,4,5]
    p=Pool()
    result = p.map(f,array)#when we do p.map, it will divide the work equally along available multiple cores of cpu. 
    #here in p.map, the first argument is function  and seconde argument is array
    print(result)#we will get the aggregate result

#in next code, we will check performance by measuring time