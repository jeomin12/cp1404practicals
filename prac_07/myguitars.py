
from guitar import Guitar

def main():
    """ Main function for the program."""
    guitars = load_guitars("guitars.csv")
    guitars.sort()
    print_guitars(guitars)
    new_guitars = get_guitars()
    guitars.extend(new_guitars)
    save_guitars(guitars)



def load_guitars(file_name):
    """Read guitars from file into list."""
    guitars = []
    with open(file_name) as f:
        for line in f:
            name, year, cost = line.strip().split(",")
            guitar = Guitar(name, int(year), float(cost))
            guitars.append(guitar)
    return guitars


def print_guitars(guitars):
    """Print list of guitars."""
    print("My guitars:")
    for i, guitar in enumerate(guitars):
        vintage = "(vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i + 1}: {guitar} {vintage}")


def get_guitars():
    """Get user input for new guitars."""
    guitars = []
    name = input("\nName: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.")
        name = input("\nName: ")
    return guitars

def save_guitars(guitars):
    """ guitars: Saves the content to the file. """
    with open("guitars.csv", "w") as f:
        for guitar in guitars:
            f.write(f"{guitar.name},{guitar.year},{guitar.cost}\n")

main()