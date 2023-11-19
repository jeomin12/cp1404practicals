"""
CP1404/CP5632 Practical - Suggested Solution
Programming Language class with tests.
"""


# programming_language.py

class ProgrammingLanguage:
    """Represent information about a programming language."""

    def __init__(self, name, typing, reflection, pointer_arithmetic, year):
        """Construct a ProgrammingLanguage from the given values."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.pointer_arithmetic = pointer_arithmetic  # New field for pointer arithmetic
        self.year = year

    def __str__(self):
        """Return a string representation of a ProgrammingLanguage."""
        return (f"{self.name}, {self.typing} Typing, Reflection={str(self.reflection)}, "
                f"Pointer Arithmetic={str(self.pointer_arithmetic)}, First appeared in {self.year}")

    def __repr__(self):
        """Return string representation of a ProgrammingLanguage."""
        return (f"{self.__class__.__name__}({self.name}, {self.typing}, {self.reflection}, "
                f"{self.pointer_arithmetic}, {self.year})")

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


