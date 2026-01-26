n=int(input("enter power which you want to take: "))

result=list(map(lambda x:2**x, range(n+1)))
print(result)

for i in range(n+1):
    print("value of 2 raised to power",i, "is",result[i])