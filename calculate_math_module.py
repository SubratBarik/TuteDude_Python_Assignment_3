"""
Using math module calculate below:
a) Square root of a number
b) Natural logarithm (log base e) of a number
c) Sine of the number (in radians)
"""

import math

num = float(input("Enter a number: "))

if num <= 0:
    print("Only positive number allowed")
else:
    sqr_root = math.sqrt(num)
    log = math.log(num)
    sine = math.sin(num)

    print(f"Square of {num} is {sqr_root}")
    print(f"Logarithm of {num} is {log}")
    print(f"Sine of {num} is {sine}")