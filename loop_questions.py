# Exercise 1: Print first 10 natural numbers using while loop

i=0
while i<10:
    i+=1
    print(i)

# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10
# ________________________________________________________________

# Exercise 2: Print the following pattern
# Write a Python code to print the following number pattern using a loop.

# 1 
# 1 2 
# 1 2 3 
# 1 2 3 4 
# 1 2 3 4 5

n=5
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print("")


# ____________________________________________________________________________
# Exercise 3: Calculate sum of all numbers from 1 to a given number

 
n=int(input("enter number: "))
sum=0
for i in range(1,n+1):
    if i<=n:
        sum=sum+i
print("sum is like (1+2+3+4+5+6+.....): ",sum)
# ---------------------------------------------------
# alternative way

n = int(input("Enter number "))
# pass range of numbers to sum() function
x = sum(range(1, n + 1))
print('Sum is:', x)
# ________________________________________________________________________________

# Exercise 4: Print multiplication table of a given number

n=int(input("enter number: "))

for i in range(1,11):
    print(n*i)

# _______________________________________________________________________________


# Exercise 5: Display numbers from a list using a loop
# Write a Python program to display only those numbers from a list that satisfy the following conditions

# The number must be divisible by five
# If the number is greater than 150, then skip it and move to the following number
# If the number is greater than 500, then stop the loop
numbers = [12, 75, 150, 180, 145, 525, 50]

for i in numbers:
    if i>500:
        break
    elif i>150:
        continue
    elif i%5==0:
        print(i)
# ___________________________________________________________________________________

# Exercise 6: Count the total number of digits in a number

n=int(input('enter number:'))
counter=0
while n!=0:
    n=n//10
    counter+=1
print(counter)
# ____________________________________________________________________________________
# Exercise 7: Print the following pattern
# Write a Python program to print the reverse number pattern using a for loop.

# 5 4 3 2 1 
# 4 3 2 1 
# 3 2 1 
# 2 1 
# 1

n=5
k=5
for i in range(0,n+1):
    for j in range(k-i,0,-1):
        print(j,end=" ")
    print()
