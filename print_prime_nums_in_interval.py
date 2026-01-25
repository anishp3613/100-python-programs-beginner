n1=int(input("enter starting number of range: "))
n2=int(input("enter ending number of range: "))

for i in range(n1,n2+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                print(f"the {i} is not a prime number.")
                break
        else:
            print(f"the number {i} is prime number.")