# import csv
#
# # Load data from CSV file
# def load_data(file_name):
#   with open(file_name) as file:
#     rows = list(csv.reader(file))
#     headers = rows[0]
#     data = rows[1:]
#   return headers, data
#
# # Format row data for printing
# def format_row(row):
#   name, capital, pop, perc = row
#   return f"{name:-<20} -{capital:-<10} {pop:>12} ({perc})"
#
# # Sort data on given column
# def sort_data(data, column):
#   data.sort(key=lambda x: x[column])
#   return data
#
# headers, data = load_data("countries.csv")
#
# # Print header
# print(format_row(headers))
#
# # Print rows sorted by different columns
# for col in range(1, len(headers)):
#   print()
#   sorted_data = sort_data(data, col)
#   for row in sorted_data:
#     print(format_row(row))

import csv

def read_data(filename):
    """Reads the CSV file and returns data as a list of lists."""
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        # Skip the header
        next(reader)
        data = [row for row in reader]
    return data

def sort_data(data, column_index):
    """Sorts the data based on the provided column index."""
    # For sorting by numbers
    if column_index in [2]:
        return sorted(data, key=lambda x: int(x[column_index].replace(',', '')), reverse=True)
    # For sorting by names or capital
    return sorted(data, key=lambda x: x[column_index])

def display_data(data):
    """Prints the formatted data."""
    for row in data:
        country, capital, population, percent, _ = row
        # Format and print the data
        print(f"{country:<20} -{capital:<15} {population:<10} ({percent})")

# Using the functions
filename = "countries.csv"
data = read_data(filename)
sorted_data = sort_data(data, 0)  # Sort by country name (Change index to sort by other columns)
display_data(sorted_data)
