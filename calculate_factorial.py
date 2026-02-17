"""
Write a function to take a number and return factorial value of it
"""

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num-1)

user_no = int(input("Enter a number: "))

result = factorial(user_no)

print(f"Factorial of {user_no} is: {result}")