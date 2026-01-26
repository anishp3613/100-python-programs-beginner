# method 1 to print fibonacci series.
n=int(input("enter number: "))
a=0
b=1
for i in range(n):
    a,b=b,a+b
    print(a)

# method 2 to print fibonacci series.

a=0
b=1
n=int(input("enter number: "))
if n==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(1,n+1):
        
        c=a+b
        a=b
        b=c
        print(c)