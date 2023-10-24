#Use of shared memeory in a process using an value
#value is similar to array but it's jst a single value
import multiprocessing


def calc_square(v):
 #shared memory has different set of methods, so append is not one of them 
    v.value=5.67#some arbitrary value

    print('inside child process ' + str(v.value))

if __name__ == "__main__": 
    v=multiprocessing.Value('d',0.0)#d is double
    p1 = multiprocessing.Process(target=calc_square, args=(v,))#here we have passed value as v

    p1.start()
    p1.join()
    print("outside process i.e.parent process " + str(v.value))
#output
# inside child process 5.67
# outside process i.e.parent process 5.67
#so whatever value was assigned to v inside child process, we were able to access it in parent process as well