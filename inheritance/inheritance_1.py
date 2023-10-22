#find theory in Theory folder
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

c = car()
c.general_usage()  # we can call method or property from parent class using object of derived class
c.specific_usage()

m = MotorCycle()  
m.general_usage()
m.specific_usage()

# c and m are objects of derived classed


#Benefits of inheritance,
#1) code reuse
#2) Extensibility
#3) Readability