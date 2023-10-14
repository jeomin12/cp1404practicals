"""
Word Occurrences
Estimate: 20 minutes
Actual: 30 minutes
"""
import csv

def main():
    """Main function to read data, process and display."""
    data = read_data("wimbledon.csv")
    champs = get_champions(data)
    countries = get_countries(data)
    display_champs(champs)
    display_countries(countries)

def read_data(filename):
    """Read the Wimbledon CSV data into a list of lists."""
    with open(filename, encoding="utf-8-sig") as f:
        reader = csv.reader(f)
        data = list(reader)[1:] # skip header row
    return data

def get_champions(data):
    """Build a dict of {champion: wins} from the data."""
    champs = {}
    for row in data:
        name = row[2]
        if name in champs:
            champs[name] += 1
        else:
            champs[name] = 1
    return champs

def get_countries(data):
    """Build a set of country codes from the data."""
    countries = set()
    for row in data:
        countries.add(row[1])
    return countries

def display_champs(champs):
    """Print the champs with number of wins."""
    max_name_length = max(len(name) for name in champs)
    print("Wimbledon Champions:")
    for name, wins in champs.items():
        print(f"{name:{max_name_length}} - {wins}")

def display_countries(countries):
    """Print the countries alphabetically."""
    country_list = sorted(list(countries))
    print("\nThese countries have won Wimbledon:")
    print(", ".join(country_list))

main()