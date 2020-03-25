import argparse

parser = argparse.ArgumentParser(description="Addition of 3 numbers")
parser.add_argument("-n1", help="number 1",dest="num1",type=int,required=True)
parser.add_argument("-n2" ,help="number 2",dest="num2",type=int,required=True)
parser.add_argument("-n3", help="number 3",dest="num3",type=int,required=True)
args = parser.parse_args()

print(args)

a = [args.num1][0]
b = [args.num2][0]
c = [args.num3][0]

s = a+b+c

print("Addition is  : " ,s)