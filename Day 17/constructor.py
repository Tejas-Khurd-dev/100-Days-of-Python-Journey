class car():
    def __init__(self, brand, seats):
        self.brand_name = brand
        self.car_seats = seats
        self.distance_covered = 0 # Default for all objects
        print(f"{self.brand_name} has {self.car_seats} seats")
        print(f"Distance covered: {self.distance_covered}")

car1 = car("bmw", 4)
print(f"{car1.brand_name} has {car1.car_seats} seats")
print(f"Distance covered: {car1.distance_covered}")

car2 = car("mercedes", 6)
print(f"{car2.brand_name} has {car2.car_seats} seats")
print(f"Distance covered: {car2.distance_covered}")

