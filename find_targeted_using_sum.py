# input: [2,11,7,15]
# target=9
# output:[0,1]
# explaination: nums[0]+nums[2]==9


nums=[5,16,13,10,1,24,4]
target=9
i=0
j=0
for n1 in nums:
    for n2 in nums:
        if n1+n2==target and i != j:
            print([j,i])
        else:
            i=i+1
            break








# Input list of numbers
nums = [5, 16, 13, 10, 1, 24, 4]
# Target sum to find
target = 9
# Initializing indices (note: this approach needs adjustment to work correctly)
i = 0
j = 0

# Outer loop to select the first number (n1)
for n1 in nums:
    # Inner loop to select the second number (n2)
    for n2 in nums:
        # Check if the sum of the two numbers equals the target
        # AND ensured we are not using the same element at the same index
        if n1 + n2 == target and i != j:
            # If pair is found, print their indices
            print([i,j])
        else:
            # This logic increments j based on the inner loop,
            # but is unconventional for finding two-sum indices
            j = j + 1
        break # Break the inner loop



# ---------------------------------------------------------------------------



items=[4,1,2,1,2]

for i in items:
    if items.count(i)==1:
     print(i)




items=[4,1,2,1,2]
# Iterate over each element in the list
for i in items:
    # Check if the current element appears exactly once in the entire list
    if items.count(i)==1:
        # If it is unique, print the element
        print(i)
