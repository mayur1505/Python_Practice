#in last two lecture we saw single inheritance
#now we will see multiple inheritance
#Here we will inherit a class from two different clsses
class Father():
    def gardening(self):
        print("I enjoy gardening")

class Mother():
    def cooking(self):
        print("I love cooking")

#now we will define child class from above two parent classes        
class Child(Father,Mother):
    def sports(self):
        print("I enjoy sports")


c=Child()

c.gardening()
c.cooking()
c.sports()
