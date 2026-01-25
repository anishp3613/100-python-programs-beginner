n1=float(input("enter number 1: "))
n2=float(input("enter number2: "))
n3=float(input("enter number3: "))

if n1>n2 and n1>n3:
    print("first number is greater.")
elif n2>n1 and n2>n3:
    print("second number is greater.")
else:
    print("third number is greater.")