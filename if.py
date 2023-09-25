#write a program that asks user to enter a number. program should then tell if number odd or even

# num = input("Enter a number: " ) #This will store in string, we will convert to int

# num = int(num)

# if num%2==0:
#     print("Numer is even")

# else:
#     print("Number is odd")

# write a program that ask a user to enter dish name and it should print which cuisine is that dish 
indian=['samosa','daal','naan']

chinese=['eggrole','pot sticker','fried rice']

italian=['pizza','pasta','risotto']

dish=input("Enter a dish name:")

if dish in indian:
    print("indian")
elif dish in chinese:
    print("chinese")
elif dish in italian:
    print("italian")
else:
    print("The dish:",dish,"is not the list provided")