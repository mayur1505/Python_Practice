#implement Remote control class that allows you to press "next" button to go to next TV channel
class RemoteControl():
    def __init__(self):
        self.channels=["HBO","cnn","abc","espc"]
        self.index=-1 # to see on which channel we are at , so -1 means TV is off

    #to implement iterator we have to define iter built in method, this iter build in method
    #will return the self object
    def __iter__(self):
        return self #when we call RemoteControl class object for __iter__, it will return same class object
    
    #when we have iterator ready then we need to define our next method
    def __next__(self):
        self.index+=1
        if self.index==len(self.channels):
            raise StopIteration

        
        return self.channels[self.index]
    

r= RemoteControl()

itr=iter(r)

print(next(itr))
print(next(itr))
print(next(itr))
print(next(itr))
# print(next(itr))


