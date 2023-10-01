"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
# A ValueError will occur when either the numerator or denominator entered by the user is invalid integer.
For example, bob (string) or 5.1 (float) is entered, ValueError occurs.

2. When will a ZeroDivisionError occur?
#  A ZeroDivisionError will occur if the user enters 0 as the denominator

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
#  Yes, It can be done by first checking if the denominator is 0 before doing the division:
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")