#we will see how to make optional arguments
#to make arguments optional just add -- in front of arguments name
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help="first number")#added -- to make optional argument
    parser.add_argument("--number2", help="second number")
    parser.add_argument("--operation", help="operation")
   
    args=parser.parse_args()#so "args" is the object which we get back once we pass the arguments through cli which has the value of arguments 
    print(args.number1)
    print(args.number2)
    print(args.operation)


n1=int(args.number1)
n2=int(args.number2)
result=None
if args.operation=="add":
    result=n1+n2
elif args.operation=="subtract":
    result=n1-n2
elif args.operation=="multiply":
    result=n1*n2
else:
    print("unsupported operation")


print("Result",result)

#to run optional argument code from cli we have to pass arguments also
#PS C:\Users\HP\Desktop\Preparation\Python_Practice\cli_argument_processing> py.exe .\argparse_2.py --number1 3 --number2 4 --operation add
# 3
# 4
# add
# Result 7