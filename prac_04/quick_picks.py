import random

NUM_PICKS = 6
MIN_NUMBER = 1
MAX_NUMBER = 45

def main():
    """Get user input, run quick picks program and print picks."""
    num_quick_picks = int(input("How many quick picks? "))
    picks = []
    for i in range(num_quick_picks):
        pick = generate_quick_pick()
        picks.append(pick)

    print_picks(picks)
def generate_quick_pick():
    """Generate list of quick pick number lists."""
    numbers = []
    while len(numbers) < NUM_PICKS:
        number = random.randint(MIN_NUMBER, MAX_NUMBER)
        # Ensure the number isn't already in the list
        if number not in numbers:
            numbers.append(number)

    numbers.sort()
    return numbers

def print_picks(picks):
    """ Print quick picks. """
    for pick in picks:
        for number in pick:
            print("{:2}".format(number), end=' ')
        print()

main()