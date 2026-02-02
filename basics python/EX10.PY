# Exercise 10: Merge two lists using the following condition

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []

for i in list1:
    if i%2!=0:
        list3.append(i)
for i in list2:
    if i%2==0:
        list3.append(i)
print(list3)

# __________________________________________________________
# print two list one of even and one of odd

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
list3 = []
list4 = []
for i in list1:
    if i%2!=0:
        list3.append(i)
    else:
        list4.append(i)
for i in list2:
     if i%2!=0:
        list3.append(i)
     else:
        list4.append(i)
print(list3)
print(list4)

# ---------------------------

# alternate way

list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

combined = list1 + list2
list3 = [i for i in combined if i % 2 != 0]  # Odd
list4 = [i for i in combined if i % 2 == 0]  # Even

print(list3)
print(list4)