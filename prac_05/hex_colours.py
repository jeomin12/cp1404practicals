COLORS = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "Aqua": "#00ffff", "Aquamarine": "#7fffd4",
          "Azure": "#f0ffff", "Beige": "#f5f5dc", "Bisque": "#ffe4c4", "Black": "#000000", "BlanchedAlmond": "#ffebcd",
          "Blue": "#0000ff"}

color = input("Enter a color name: ").lower()
while color != "":
    try:
        print(color, "is", COLORS[color])
    except KeyError:
        print("Invalid color name")
    color = input("Enter a color name: ").lower()
