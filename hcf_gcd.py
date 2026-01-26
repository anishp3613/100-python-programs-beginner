def hcf(x,y):
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x%i==0)and(y%i==0)):
            hcf=i
    return hcf
n1=int(input("enter num 1: "))
n2=int(input("enter num2: "))
print("the hcf of the given nummbers is",hcf(n1,n2))