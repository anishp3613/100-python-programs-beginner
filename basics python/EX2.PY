# EXERCISE 2: PRINT THE SUM OF CURRENT NUMBER AND A PREVIOUS NUMBER

previous_num=0

for i in range(1,11):
    sum=i+previous_num
    print("current number: ",i,"previous number: ",previous_num, "sum is: ",sum)
    previous_num=i

