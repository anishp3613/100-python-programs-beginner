# EXERCISE 4: REMOVE FIRST N CHARACTERS FROM A STRING.

s=str(input("Enter the original string: "))
n= int(input("Enter the number of characters to remove from the beginning: "))
print('Original string:',s)
x=s[n:]
print('String after removing characters:',x)
