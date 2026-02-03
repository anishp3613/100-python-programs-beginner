# Exercise 12: Calculate income tax

# For example, suppose the income is 45000, and the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000

# Practice Problem: Calculate income tax for a given income based on these rules:

# First $10,000: 0% tax
# Next $10,000: 10% tax
# Remaining income: 20% tax
# Exercise Purpose: This exercise introduces “Tax Brackets” logic, a classic example of complex conditional branching. It shows how to calculate values cumulatively instead of applying a single percentage to the entire amount.

# Given Input: income = 45000

# Expected Output: Total income tax to pay is 6000


income = 45000
tax_payable = 0
print("Given income", income)

if income <= 10000:
    tax_payable = 0
elif income <= 20000:
    x = income - 10000
    tax_payable = x * 10 / 100
else:
    tax_payable = 0
    tax_payable = 10000 * 10 / 100
    tax_payable += (income - 20000) * 20 / 100

print("Total tax to pay is", tax_payable)