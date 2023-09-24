"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""

# Get score input from the user
score = float(input("Enter score: "))

if score < 0 or score > 100:
    print("Invalid score")
else:
    if score < 50:1-
        print("Bad")
    elif score <= 90:
        print("Passable")
    else:
        print("Excellent")