class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def describe(self):
        return f"Vehicle Make: {self.make}, Model: {self.model}"
class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def describe(self):  # Overriding method
        return f"Car Make: {self.make}, Model: {self.model}, Doors: {self.num_doors}"

class Bike(Vehicle):
    def __init__(self, make, model, bike_type):
        super().__init__(make, model)
        self.bike_type = bike_type

    def describe(self):  # Overriding method
        return f"Bike Make: {self.make}, Model: {self.model}, Type: {self.bike_type}"
class Car(Vehicle):
    def __init__(self, make, model, num_doors, price):
        super().__init__(make, model)
        self.num_doors = num_doors
        self.__price = price  # Private attribute

    def get_price(self):
        return f"Car price: ${self.__price}"

    def set_price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Invalid price!")
vehicles = [
    Car("Toyota", "Corolla", 4, 25000),
    Bike("Yamaha", "MT-07", "Sport"),
    Vehicle("Ford", "Transit")
]

for v in vehicles:
    print(v.describe())  # Calls the overridden method based on the object type
