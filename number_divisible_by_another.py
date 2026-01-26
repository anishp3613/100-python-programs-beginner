# using for loop find number divisible by another number
print("numbers divisible by 13 are: ")

for i in range(1,100):
    if i % 13==0:
        print(i)  

#now using lambda function and filter function

l=[39,48,26,98,33,67,87]
n=int(input("enter number: "))
result=list(filter(lambda x:x%n==0, l))
print(result)