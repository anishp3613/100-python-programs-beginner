# EXERCISE 3: PRINT CHARACTERS PRESENT AT AN EVEN INDEX NUMBER.

# SOLUTION ONE

s=str(input("enter string: "))
print(f"original string is {s}")
print(f"printing only even index character string from {s}")
for i in range(0,len(s),2):
    print(s[i])

# SOLUTION TWO

s=str(input("enter string: "))
print("original string: ",s)
x=list(s)
for i in x[0::2]:
    print(i)

    