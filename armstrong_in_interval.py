n1=int(input("enter number 1: "))
n2=int(input("enter number 2: "))


for i in range(n1,n2+1):
    sum=0
    x=len(str(i))
    temp=i
    while temp>0:
        digit=temp%10
        sum+=digit**x
        temp//=10
    if i==sum:
        print(i)