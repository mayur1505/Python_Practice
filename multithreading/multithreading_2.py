#execute multithreading to improve speed of the code
import time
import threading

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)#for only learning purpose we have kept cpu waiting
        print('square:',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:',n*n*n)

arr = [2,3,8,9]

t = time.time()

t1= threading.Thread(target=calc_square, args=(arr,))#target is function or work that we want to execute
t2= threading.Thread(target=calc_cube, args=(arr,))#args is tuple and we are passing it as input. we can pass multiple arguments with this thats why ',' is there after args

#due to this both fn will be executed parallely
t1.start()
t2.start()

t1.join()#it will be executed when square fun will be executed completely
t2.join()#it will be executed when cube fun will be executed completely

print("done in : ",time.time()-t)
print("Hah... I am done with all my work now!")
#both the functions will run in parallel and square and cubes will be printed randomely
#multithreading is used when in our program cpu has to wait