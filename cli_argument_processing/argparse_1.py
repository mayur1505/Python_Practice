import argparse

#there are two types of arguments that argparse supports
#1)Positional Arguments
#2)Optional Arguments

#we are writing a program that takes 3 inputs
#1)First number
#2)Second Number
#3)Operation("add","subtract","multiply")
#it should return result of operation based on inputs
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help="first number")
    parser.add_argument("number2", help="second number")
    parser.add_argument("operation", help="operation")
    #number1, number2 and operation are positional arguments and they are compulsory to be passed
    args=parser.parse_args()#so "args" is the object which we get back once we pass the arguments through cli which has the value of arguments 
    print(args.number1)
    print(args.number2)
    print(args.operation)

#for running this code using cli
#type py.exe or python or python.exe and the python file name and -h and hit enter
#for ex. py.exe .\argparse_1.py -h
#for giving inputs to number1, number2 and operation
#py.exe .\argparse_1.py 4 5 add
#when we give inputs from cli, it is by default string, we need to convert into int if we want

n1=int(args.number1)
n2=int(args.number2)
result=None
if args.operation=="add":
    result=n1+n2
elif args.operation=="subtract":
    result=n1-n2
elif args.operation=="multiply":
    result=n1*n2

print("The result is ",result)
#running from cli
# PS C:\Users\HP\Desktop\Preparation\Python_Practice\cli_argument_processing> py.exe .\argparse_1.py 4 5 add     
# 4
# 5
# add
# The result is  9
