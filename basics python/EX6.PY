# DISPLAY NUMBER DIVISIBLE BY 5

l1=input(" enter numbers separated by space:").split()

for i in l1:
    num=int(i)
    if num%5==0:
        print(num)
