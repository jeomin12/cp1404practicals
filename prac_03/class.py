# Read line thet start with a
#  Method 1
# filename = "sample.txt"
# with open(filename, 'r') as file:
#     content = file.read()
#     lines = content.split('\n')
#     for line in lines:
#         if line.startswith('#'):
#             print(line)

# Method 2
# filename = input("Filename: ")
# filename = "sample.txt"
# infile = open(filename, "r")
# for line in infile:
#     if line.startswith("#"):
#         print(line.strip())
# infile.close()

is_finished = False
while not is_finished:
    try:
        result = int(input("Enter a valid integer"))
        is_finished = True
    except ValueError:
        print("Please enter a valid integer.")
print("Valid result is:", result)