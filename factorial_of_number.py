# factorial using for loop

n=int(input("enter number : "))

fact=1
for i in range(1,n+1):
        fact*=i
print(fact)

# factorial using recursion

def fact(a):
        if a==0:
                return 1
        else:
                return ((a)*fact(a-1))
num=int(input("enter number: "))
result=fact(num)