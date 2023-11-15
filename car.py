class Car:
    def __init__(self, title, price, mileage, fuel_type, gearbox, year, capacity):
        self.title = title
        self.price = int(price.replace(' ', ''))
        self.mileage = int(mileage.replace(' ', '').replace('km', ''))
        self.fuel_type = fuel_type
        self.gearbox = gearbox
        self.year = int(year)
        self.capacity = float(capacity.replace(" cm3", "").replace(" ", "."))

    def __str__(self):
        return f"{self.title} {self.price} {self.mileage}km {self.fuel_type} {self.gearbox} {self.year}r {self.capacity}cm3"
    