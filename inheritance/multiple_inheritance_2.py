class Father():
    def skills(self):
        print("gardening,programming")

class Mother():
    def skills(self):
        print("cooking,art")

#now we will define child class from above two parent classes        
class Child(Father,Mother):
    def skills(self):
        Father.skills(self)
        Mother.skills(self)
        print("sports")



c=Child()
c.skills()#this child has inherited all the skills of father and mother