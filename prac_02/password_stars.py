MIN_LENGTH = 8
def main():
    """Prompt and print the password"""
    password = input("Enter password: ")
    password = get_password(password)
    print_asterics(password)

def get_password(password):
    """Checks password meets minimum length requirement."""
    while len(password) < MIN_LENGTH:
        print("Password too short! Try again.")
        password = input("Enter password (minimum {} characters): ".format(MIN_LENGTH))
    return password
def print_asterics(password):
    """Print asteriks to the password."""
    print("*" * len(password))

main()