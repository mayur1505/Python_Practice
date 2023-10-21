#Finally statement
#the finally will execute the code in that block no matter what!
#We will see how finally is used 
#for e.x. if the code is too big, then we can't specify every exception
#suppose we open file using f.open() and if error occurs and f.close() doesn't run as code stopped in between
#so the cleanup of resources will not happen, so to avoid this we will use "finally"

def process_file():
    try:
        f=open("C:\\Users\\HP\\Desktop\\Preparation\\Python_Practice\\RaiseExceptions_Finally\\finally.txt",'w')
        x=1/0 #let's assume we have not handled this exception
    except FileNotFoundError as e:
        print("inside except")
    finally:
        print("cleaning up file")
        f.close()#though we are getting error for zerodivision still f.close() will run
        #f.close() will cleanup all the resources

process_file()