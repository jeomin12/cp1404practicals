COLORS = {"Alizarin Crimson": "#f0f8ff", "Amber": "#faebd7", "Aqua": "#00ffff", "Aquamarine": "#7fffd4",
          "Azure": "#f0ffff", "Beige": "#f5f5dc", "Bisque": "#ffe4c4", "Black": "#000000", "Bitter Lemon": "#ffebcd",
          "Blue": "#0000ff"}

color = input("Enter a color name: ").title().strip()
while color != "":
    if color in COLORS:
        print(f"{color} is  {COLORS[color]}")
    else:
        print("Invalid color name")

    color = input("Enter a color name: ").title().strip()