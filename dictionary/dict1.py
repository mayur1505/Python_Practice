# dictionary allows us to store key, value pairs
# They are also known as Maps, Hashtables, Associate Arrays

# classical example of dictionary is telephone directory

dic={"Mayur":489002340,"Kalyani":39028543084032,"Shimpi":389028490324}
#here Mayur is the key and the number written is the value of that key
# with using that key we can retrieve the value
#in List we retrieve value using index 
print(dic["Mayur"])

#adding new key-pair in dictionary
dic["Gaurav"]=38383

print(dic)

#deleting key-pair

del dic["Gaurav"]

print(dic)

#iterating through the dictionary

for item in dic: 
    print("The name of the key is",item,"Number or Value is ",dic[item])

# another way to iterate 

for k,v in dic.items():
    print("The key is",k,"The value is",v)


#checking if specific person is in the dic

for name in dic:
    if name=="Sunny":
        print("Sunny has found")
        break
else:
    print("Sunny is not in the list")

print("Shimpi" in dic) #it will return true

#for clearing dic
dic.clear()