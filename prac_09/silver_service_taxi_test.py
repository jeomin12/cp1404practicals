from silver_service_taxi import SilverServiceTaxi

def main():
    """Test the silver_side_taxi class"""
    luxury_taxi = SilverServiceTaxi("Hummer", 200, 2)  # Fanciness of 2

    # Drive the taxi 18 km
    luxury_taxi.drive(18)
    print(luxury_taxi)
    print(f"Total fare for 18km trip: ${luxury_taxi.get_fare():.2f}")

if __name__ == "__main__":
    main()

