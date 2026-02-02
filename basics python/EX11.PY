# Exercise 11: Get each digit from a number in the reverse order.

n=int(input("ENTER NUMBER: "))
while n>0:
    d=n%10
    n=n//10
    print(d,end=" ")
