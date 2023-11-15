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
        return total_price / len(self.cars)

