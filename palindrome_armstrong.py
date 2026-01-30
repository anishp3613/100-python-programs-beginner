n = int(input("enter number: "))

number = n
temp = 0

while n > 0:
    last = n % 10
    temp=(temp*10)+last
    n//=10
if temp==number:
    print("palindrome")
else:
    print("not palindrome")

#121
#1221

# take input n from user
# n stored into number for comparison if we directly take n then it will be 0 at the end and we can not compare it to our temp variable.
# in loop if n is greater than 0 then only we enter to loop otherwise exit the loop
# in last the given number 1221 is divided by 10 and answer is 122 and remender is 1 
# in temp variable we multiply that initially temp=0 so now (0*10) + 1 = 1
# our answer of that division is 122.1 and by floor division we did not consider the after decimal value (round up) so here 122.1 removed the 1 after decimal
# 122 will again go to loop because its greater than 0 so the loop work till the value of n becomes 0

# after all the iterations the temp variable which consists the reversed is compared with original number which user entered if this condition satisfy then print this is palindrome otherwise print this is not palindrome.




n = int(input("enter number: "))

number = n
temp = 0
sum=0
while number > 0:
    last = number % 10
    sum=sum+last**len(str(n))
    number//=10
if sum==n:
    print("armstrong")
else:
    print("not armstrong")

# error :-  we can not count lenght directly 
# we have to cnvert it into string. 