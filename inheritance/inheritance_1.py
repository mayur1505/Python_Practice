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
        #self.general_usage()
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
c.general_usage()
c.specific_usage()

m = MotorCycle()
m.general_usage()
m.specific_usage()
#print(issubclass(car,MotorCycle))
