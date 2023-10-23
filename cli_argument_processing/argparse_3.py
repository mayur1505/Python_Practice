#suppose we want to restrict user from putting unsupported operation
#for ex. suppose we only support add, subtract and multiply
#and we want our user to restrict from putting other operations
#then we can "choices"

import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--number1", help="first number")#added -- to make optional argument
    parser.add_argument("--number2", help="second number")
    parser.add_argument("--operation", help="operation", choices=["add","subtract","multiply"])
   
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



print("Result",result)