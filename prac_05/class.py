"""
Produce the following sorted and formatted output
Bob         = 612
Xavier      =  80
Chantanelle =   9
Derek       =   7
data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]"""

# from operator import itemgetter
# data = [['Derek', 7], ['Xavier', 80], ['Bob', 612], ['Chantanelle', 9]]
# # data.sort(key=itemgetter(1), reverse = True)
# # print(data)
# maximum_length = max(len(pair[0]) for pair in data)
# print(maximum_length)
# for pair in sorted(data, key = itemgetter(1), reverse = True):
#   print(f"{pair[0]:{maximum_length}} = {pair[1]}")

""" Dictionary """
# from operator import itemgetter
# name_to_number = {'Derek': 7, 'Xavier': 80, 'Bob': 612, 'Chantanelle': 9}
# max_name_length = max(len(name) for name in name_to_number.keys())
# max_number_length = max(len(str(number)) for number in name_to_number.values())
#
# for name, number in sorted(name_to_number.items(), key=itemgetter(1), reverse=True):
#   print(f"{name:{max_name_length}} = {number:{max_number_length}}")


""" Write a function that takes a list of strings and returns a dictionary of string: length of string pairs."""

# def main():
#     strings = ["bob", "derick", "xavi"]
#     print(strings_to_lengths(strings))
#
# def strings_to_lengths(strings):
#     return {string: len(string) for string in strings}
#
# main()


# def main():
#     strings = ["bob", "derick", "xavi"]
#     strings_to_length = convert_list_to_dictionary(strings)
#     print(strings_to_length)
#
# def convert_list_to_dictionary(strings):
#     string_to_length = {}
#     for string in strings:
#         string_to_length[string] = len(string)
#     return string_to_length

#
# import csv
# def main():
#   data = load_data('countries.csv')
#   display_data(data)
#
# def load_data(file_name):
#     """Load CSV data into a list of dicts"""
#     data = []
#     with open(file_name) as f:
#         reader = csv.reader(f)
#         for row in reader:
#             data.append(row)
#     return data
#
#
# def display_data(data):
#   """Display data nicely formatted and sorted by country"""
#   data.sort(key=lambda x: x['Country (or territory)'])
#   for row in data:
#     country = row['Country (or territory)']
#     capital = row['Capital']
#     population = row['Population']
#     percent = row['% of country']
#
#     print(f"{country:30} - {capital:20} {population:12} ({percent})")

import csv

FILENAME = "countries.csv"

def main():
  country_to_data = load_data(FILENAME)
  display_details(country_to_data)

def load_data(filename):
  country_to_data = {}
  with open(filename, 'r') as in_file:
    reader = csv.reader(in_file)
    next(reader)
    for record in reader():
      record[2] = int(record[2].replace(',', ''))
      record[3] = float(record[3][:-1])
      print(record)
      country_to_data[record[0]] = record[1:-1]



