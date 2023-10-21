#isinstance and issubclass methods
class vehicle:
    def general_usage(self):
        print("General use: Transportation")

#deriving a subclass from another class(inheritance)
class car(vehicle): #carclass is inherited from vehicle class
    def  __init__(self):
        print("I'm car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        #self.general_usage() # self is an object of car class and since it is derived from vehicle you'll be able to call general usage here
        print("specific use: commute to work, vacation with family")

class MotorCycle(vehicle):
    def __init__(self):
        print("I'm motor cycle")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        #self.general_usage()
        print("specific use: road trip, racing")


c=car()
m=MotorCycle()

#now we will learn how isinstance and issubclass methods works

#isinstance will check if object is an instance of a specific class or not.
print(isinstance(c,car))#true
print(isinstance(c,MotorCycle))#false

#issubclass will check if that one class is subclass of another class
print(issubclass(car,vehicle))#true because car is subclass of vehicle
