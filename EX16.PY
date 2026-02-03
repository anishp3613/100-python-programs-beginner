# Exercise 16. Check Palindrome Number
# Practice Problem: Write a program to check if a given number is a palindrome. A palindrome number remains the same when its digits are reversed (e.g., 121, 545).

# Exercise Purpose: This exercise teaches “Algorithmic Reversal.” While strings are easy to reverse in Python, reversing a number mathematically using the modulo (%) and floor division (//) operators deepens understanding of how integers are stored in memory and how to manipulate digits individually.

# Given Input: number = 121

# Expected Output:

# Original number 121
# Yes. given number is palindrome number

def palindrome(num):
    string=str(num)
    reverse_str=string[::-1]
    if num==reverse_str:
        print("palindrome")
    else:
        print("not palindrome")
palindrome(input("enter :"))