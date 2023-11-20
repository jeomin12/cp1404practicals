class Band:
    """Band class for managing a group of musicians."""

    def __init__(self, name=""):
        """Initialize a Band with a name and an empty list of musicians."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of the Band."""
        musicians_str = ', '.join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musicians_str})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician in the band playing their instrument."""
        return '\n'.join(musician.play() for musician in self.musicians)
