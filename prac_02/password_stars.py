MIN_LENGTH = 8
def main():
    password = input("Enter password: ")

    password = get_password(password)

    print("*" * len(password))


def get_password(password):
    while len(password) < MIN_LENGTH:
        print("Password too short! Try again.")
        password = input("Enter password (minimum {} characters): ".format(MIN_LENGTH))
    return password


main()