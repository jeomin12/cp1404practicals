from taxi import Taxi

def main():
    """Main function for the taxi test program"""
    my_taxi = Taxi("Prius 1", 100, 1.23)
    my_taxi.drive(40)
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")
    my_taxi.start_fare()

    my_taxi.drive(100)
    # Print the details and the current fare
    print(my_taxi)
    print(f"Current fare: ${my_taxi.get_fare():.2f}")

if __name__ == "__main__":
    main()
