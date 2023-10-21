#we will now create user defined exception. Exception is basically an instance/object of a class
#Always remember 
#User defined exceptions are always derived from Exception base class

#Let's define user defined exception class Accident
class Accident(Exception):
    def __init__(self,msg):
        self.msg=msg
    def print_exception(self):
        print("User defined exception: ",self.msg)


try:
    raise Accident("Crash between two cars")
except Accident as e:
    e.print_exception()        