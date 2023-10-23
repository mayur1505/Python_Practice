

#for a given list of numbers print square and cube of every numbers

import time

def calc_square(numbers):
    print("calculate square numbers")
    for n in numbers:
        time.sleep(0.2)#cpu will wait for 0.2s and it will be idle
        print('square:',n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:',n*n*n)

arr = [2,3,8,9]

t = time.time()

calc_square(arr)
calc_cube(arr)

print("done in : ",time.time()-t)#overall how much time the code took to execute
#this code is taking almost 1.6 secods to execute
#let's use multithreading and improve this number
print("Hah... I am done with all my work now!")