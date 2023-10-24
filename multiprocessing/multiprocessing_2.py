#now instead of printing results in multiprocessing_1.py, we will store them global variable

import time
import multiprocessing

square_result=[]
def calc_square(numbers):
    global square_result
    for n in numbers:
        print('square ' + str(n*n))
        square_result.append(n*n)
if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p1.start()
    p1.join()
    print("result" + str(square_result))#ideally this line should print 'result  4 9 64' but it will not print, it will print 'result[]'
#because when we create new process it will create a new copy of square_result, but if it would been the case of multithreading then we could have seent the square results
#Every process has its own address space (virtual memory). Thus program variables are not shared between two processes. You need to use
#interprocess communication (ipc) techniques if you want to share data between two processes
#so if we want to use square_result within process to print, it will print squre numbers
# def calc_square(numbers):
#     for n in numbers:
#         print('square ' + str(n*n))
#         square_result.append(n*n)
#     print("within a process:result" +str(square_result))
