def main():
    numbers = get_numbers()
    print_stats(numbers)

    security_checker()

def get_numbers():
    """Get user input of 5 numbers."""
    numbers = []
    for i in range(5):
        number = int(input("Number: "))
        numbers.append(number)
    return numbers
def print_stats(numbers):
    """ Print out statistics on the list of numbers."""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers)}")

def security_checker():
    """ Check username against list of approved users."""
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye',
                 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command',
                 'ExecState', 'InteractiveConsole', 'InterpreterInterface',
                 'StartServer', 'bob']

    username = input("Enter username: ")
    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")
main()