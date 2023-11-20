from taxi import Taxi

class SilverServiceTaxi(Taxi):
    """Specialised version of a Taxi with added fanciness and a flagfall charge."""
    flagfall = 4.50  # class variable for additional charge

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance, based on parent class Taxi."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km = Taxi.price_per_km * self.fanciness  # Scale the price based on fanciness

    def __str__(self):
        """Return a string representation of a SilverServiceTaxi object."""
        return f"{super().__str__()} plus flagfall of ${self.flagfall}"

    def get_fare(self):
        """Calculate and return the price for the SilverServiceTaxi trip."""
        return super().get_fare() + self.flagfall
