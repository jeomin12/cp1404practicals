"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion
"""

MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
print(MENU)
# Get user choice and convert to uppercase
choice = input(">>> ").upper()
while choice != "Q":
    if choice == "C":
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32  # Convert celsius to fahrenheit
        print(f"Result: {fahrenheit:.2f} F")
    elif choice == "F":
        farenheit = float(input("Farenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)  # # Convert fahrenheit to celsius
        print(f"Result: {celsius:.2f} C")
    else:
        print("Invalid option")
    print(MENU)
    choice = input(">>> ").upper()
print("Thank you.")