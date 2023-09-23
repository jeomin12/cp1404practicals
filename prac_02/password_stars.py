MIN_LENGTH = 8
def main():
    password = input("Enter password: ")

    while len(password) < MIN_LENGTH:
        print("Password too short! Try again.")
        password = input("Enter password (minimum {} characters): ".format(MIN_LENGTH))

    print("*" * len(password))


main()