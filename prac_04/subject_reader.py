"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = get_data()
    display_subjects(data)
def get_data():
    """Read data from file and return as a list of lists."""
    data = []
    with open(FILENAME) as input_file:
        for line in input_file:
            line = line.strip() # Remove the \n
            parts = line.split(',') # Separate the data into its parts
            parts[2] = int(parts[2]) # Make the number an integer
            data.append(parts)
    return data
def display_subjects(data):
    """ Display subjects """
    for subject_data in data:
        print(f"{subject_data[0]} is taught by {subject_data[1]} and has {subject_data[2]} students")

main()