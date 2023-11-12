
import csv
from collections import namedtuple
from programming_language import ProgrammingLanguage

def main():
    """Read file of programming language details, save as objects, display."""
    languages = []
    with open('languages.csv', 'r') as in_file:
        in_file.readline()  # Consume the first line (header)
        for line in in_file:
            parts = line.strip().split(',')
            # The order should be: name, typing, reflection, pointer_arithmetic, year
            reflection = parts[2] == "Yes"
            pointer_arithmetic = parts[3] == "Yes"  # Assumes the Pointer Arithmetic field is the fourth field
            language = ProgrammingLanguage(parts[0], parts[1], reflection, pointer_arithmetic, int(parts[4]))
            languages.append(language)

    for language in languages:
        print(language)

def using_csv():
    """Language file reader version using the csv module."""
    with open('languages.csv', 'r', newline='') as in_file:
        in_file.readline()  # Consume the first line (header)
        reader = csv.reader(in_file)  # Use default dialect, Excel
        for row in reader:
            if len(row) == 5:
                name, typing, reflection, pointer_arithmetic, year = row
                reflection = reflection == "Yes"
                pointer_arithmetic = pointer_arithmetic == "Yes"
                language = ProgrammingLanguage(name, typing, reflection, int(year), pointer_arithmetic)
                print(language)

def using_namedtuple():
    """Language file reader version using a named tuple."""
    with open('languages.csv', 'r', newline='') as in_file:
        file_field_names = in_file.readline().strip().split(',')
        Language = namedtuple('Language', file_field_names)
        reader = csv.reader(in_file)  # Use default dialect, Excel
        for row in reader:
            language = Language._make(row)
            print(language)

def using_csv_namedtuple():
    """Language file reader version using both csv module and named tuple."""
    with open('languages.csv', 'r', newline='') as in_file:
        in_file.readline()  # Consume the first line (header)
        Language = namedtuple('Language', 'name, typing, reflection, pointer_arithmetic, year')
        for language in map(Language._make, csv.reader(in_file)):
            print(f"{language.name} was released in {language.year}")
            print(language)

if __name__ == "__main__":
    main()

