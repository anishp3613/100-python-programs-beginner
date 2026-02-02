# EXERCISE 9: CHECK PALINDROME NUMBER
temp=0
n=int(input("enter number: "))
num=n
st=len(n)
while st>0:
    d=st%10
    temp=temp*10+d
    st//10
if temp==num:
    print("pal")
else:
    print("not pal")