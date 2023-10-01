# Open a file and writes the name
name = input("Enter your name: ")
with open("name.txt", "w") as file:
    file.write(name)


# Reads name from file and prints it.
with open("name.txt", "r") as file:
    name = file.read()
print("Your name is", name)


# Reads and print sum of first two numbers
with open("numbers.txt", "r") as file:
    num1 = int(file.readline())
    num2 = int(file.readline())
    sum = num1 + num2
    print(f"Sum of first two numbers: {sum}")


# Reads and print sum of all numbers
with open("numbers.txt", "r") as file:
    total = 0
    for line in file:
        number = int(line)
        total += number
print(f"Total: {total}")
