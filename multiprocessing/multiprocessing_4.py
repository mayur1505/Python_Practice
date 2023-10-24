#Use of shared memeory in a process using an array
#shared memory variable id different than regular variable
import multiprocessing


def calc_square(numbers,square_result):
 #shared memory has different set of methods, so append is not one of them  
    for idx, n in enumerate(numbers):#idx is index
        square_result[idx] = n*n
    print('inside child process ' + str(square_result[:]))

if __name__ == "__main__":
    arr = [2,3,8]
    square_result=multiprocessing.Array('i',3)#this is shared memory variable, here i means integer and d means double. 3 is the size of array
    p1 = multiprocessing.Process(target=calc_square, args=(arr,square_result))#here we will pass shared memory in args

    p1.start()
    p1.join()
    print("outside process i.e.parent process " + str(square_result[:]))#printing all the elements of array like square_result[:]

#output
# inside process [4, 9, 64]
# outside process [4, 9, 64]