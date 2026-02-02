# EXERCISE 1: CALCULATE THE MULTIPLICATION AND SUM OF TWO NUMBERS

n1=int(input("enter 1st number: "))
n2=int(input('enter 2nd number: '))

if n1*n2<1000:
    print(n1*n2)
else:
    print(n1+n2)

# in this program we need to calculate 
# if the product of two numbers are < 1000 then return their product otherwise return sum

# other solution using function
def multi_or_sum(n1,n2):
    product=n1*n2
    if product<=1000:
        return product
    else:
        return n1+n2
result=multi_or_sum(20,30)
print(result)
result=multi_or_sum(40,30)
print(result)
