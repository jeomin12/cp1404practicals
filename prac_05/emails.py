"""
Word Occurrences
Estimate: 20 minutes
Actual: 18 minutes
"""

def main():
    emails = {}
    email = input("Email: ")
    while email != "":
        name = get_name(email)
        confirm = input(f"Is your name {name}? (Y/n) ")
        if confirm.lower() != "" and confirm.lower() != "y":
            name = input("Name: ")
        emails[email] = name
        email = input("Email: ")

    for email, name in emails.items():
        print(f"{name} ({email})")
def get_name(email):
    """Extracts the user's name from the email address."""
    name = email.split('@')[0].split('.')[0].title()
    return name


main()
