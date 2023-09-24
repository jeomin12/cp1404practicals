MENU = """
(G)et a valid score (must be 0-100 inclusive)
(P)rint result
(S)how stars 
(Q)uit
"""

def main():
    """Get user's choice and performs corresponding actions"""
    score = get_valid_score()
    print(MENU)
    choice = input("Enter your choice: ").upper()
    while choice != "Q":

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(get_score_result(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid choice. Please try again.")
        print(MENU)
        choice = input("Enter your choice: ").upper()

    print("Farewell! Have a great day!")


def get_valid_score():
    """Prompt user for a valid score between 0 and 100 inclusive."""
    score = float(input("Enter score (0-100): "))
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100 inclusive.")
        score = float(input("Enter score (0-100): "))

    return score


def get_score_result(score):
    """Determine the result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score <= 90:
        return "Passable"
    else:
        return "Excellent"


def print_stars(score):
    """Prints as many stars as the score."""
    print('*' * int(score))


main()