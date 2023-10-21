#Find theory in Theroy folder

class Human:  #class is a keyword to define class in python 
    #we will define a spefical function called as init
    #self is a class itself
    def __init__(self, n, o) :#init will initialize properties of particular class when we later on create the instance
        self.name = n   #n & o are arguments to the function 
        self.occupation=o    #name & occupation are properties of class human

#here we have defined name and occupation as properties. We can have long list of properties
#second step in to define methods

    def do_work(self):
        if self.occupation == "tennis player":
            print(self.name,"Plays tennis")
        elif self.occupation == "actor":
            print(self.name,"shoots a film")

    def speaks(self):
        print(self.name,"says how ar you ?")


#so we have defined properties and methods for Human class. so Human class is ready
#so let's create some instances of the class
#Tom Cruise

tom = Human("tom cruise","actor") # only pass n and o , we don't have to pass self. In ython self is always implicitely taken
tom.do_work()
tom.speaks()

maria=Human("Maria Sharapova","tennis player")
maria.do_work()
maria.speaks()
