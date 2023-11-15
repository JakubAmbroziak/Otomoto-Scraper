import statistics

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

