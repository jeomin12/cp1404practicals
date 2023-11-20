from car import Car
import random

class UnreliableCar(Car):
    """A car that might not always drive."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if a random number is less than the car's reliability."""
        if random.randint(0, 100) < self.reliability:
            # Only drive if the random number is less than reliability
            return super().drive(distance)
        else:
            return 0
