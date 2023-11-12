strings =["Bob", "Kim"]
for index, s in enumerate(strings, start=1):
    filename = s + ".txt"
    with open(filename, "w") as f:
        f.write(str(index))