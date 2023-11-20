from unreliable_car import UnreliableCar

def main():
    """Main function for Unreliable car test program"""
    # Create an UnreliableCar object
    my_unreliable_car = UnreliableCar("Old Clunker", 100, 50)  # 50% reliability

    # Try to drive the car for a distance
    distance_driven = my_unreliable_car.drive(30)
    print(f"Attempted to drive 30km. Distance driven: {distance_driven}km")

    # Print the car's details
    print(my_unreliable_car)

if __name__ == "__main__":
    main()
