import statistics
from collections import Counter


class CarList:
    def __init__(self):
        self.cars = []

    def add(self, car):
        self.cars.append(car)
    
    def __getitem__(self, index):
        if 0 <= index < len(self.cars):
            return self.cars[index]
        else:
            raise IndexError("Index out of range")

    def calculate_average_price(self):
        if not self.cars:
            return 0  # Return 0 if the list is empty

        total_price = sum(car.price for car in self.cars)
        avg_price = int(total_price / len(self.cars))
        print(f"Avrage price is equal to {avg_price}zł based on {len(self.cars)} cars")
        return avg_price
    
    def calculate_average_year(self):
        if not self.cars:
            return 0  # Return 0 if the list is empty

        total_year = sum(car.year for car in self.cars)
        avg_year = int(total_year / len(self.cars))
        print(f"Avrage year is equal to {avg_year} based on {len(self.cars)} cars")
        return avg_year
    
    def calculate_median_capacity(self):
        if not self.cars:
            return 0  # Return 0 if the list is empty

        capacities = [car.capacity for car in self.cars]
        median_capacity = statistics.median(capacities)
        print(f"Median capacity is equal to {median_capacity} cm3 based on {len(self.cars)} cars")
        return median_capacity

    def calculate_gearbox_distribution(self):
        if not self.cars:
            return Counter()  # Return an empty Counter if the list is empty

        gearbox_counter = Counter(car.gearbox for car in self.cars)
        total_cars = len(self.cars)

        for gearbox, count in gearbox_counter.items():
            percentage = (count / total_cars) * 100
            print(f"{gearbox}: {count} cars ({percentage:.2f}%)")

        return gearbox_counter
    
    def calculate_fuel_type_distribution(self):
        if not self.cars:
            return Counter()  # Return an empty Counter if the list is empty

        fuel_type_counter = Counter(car.fuel_type for car in self.cars)
        total_cars = len(self.cars)

        for fuel_type, count in fuel_type_counter.items():
            percentage = (count / total_cars) * 100
            print(f"{fuel_type}: {count} cars ({percentage:.2f}%)")

        return fuel_type_counter