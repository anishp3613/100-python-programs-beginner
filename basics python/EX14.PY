# Exercise 14. Downward Half-Pyramid Pattern
# Practice Problem: Print a downward half-pyramid pattern using stars (*).

# Exercise Purpose: Learn about reverse indexing. Controlling loop boundaries in reverse is important for algorithms that process data from end to beginning.


# Given Input: Rows: 5

# Expected Output:

# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

n=int(input("enter number: "))

for i in range(1,n+1):
    for j in range(i-1,n):
        print("*", end=" ")
    print()