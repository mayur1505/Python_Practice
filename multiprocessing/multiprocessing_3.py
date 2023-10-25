#sharing data between processes using array and value

import multiprocessing

square_result=[]
def calc_square(numbers):
    global square_result#it is referring to square_result=[] varaible
    for n in numbers:
        square_result.append(n*n)
    print('inside child process ' + str(square_result))
if __name__ == "__main__":
    arr = [2,3,8]
    p1 = multiprocessing.Process(target=calc_square, args=(arr,))
    p1.start()
    p1.join()
    print("outside process i.e.parent process " + str(square_result))

#output
# inside process [4, 9, 64]
# outside process [] 
# whenever you create a new process the new process will get its own address space at a
# space meaning the space where it stores all the variables

#see the theory in theory folder and file name is "multiprocessing_1"
#we will use shared memory for solving above issue. 
#Shared memory lives outside the processes hence we can access it. There’s two way of using shared memory. 
#First one is value and other is array.