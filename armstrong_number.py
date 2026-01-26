n=int(input("enter number: "))
x=len(str(n))
sum=0
temp=n
while temp>0:
    digit=temp%10
    sum+=digit**x
    temp//=10
if sum==n:
    print("its a armstrong number")
else:
    print("its not armstrong number.")
