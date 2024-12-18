class Smartphone:
    def __init__(self, brand, model, storage, battery):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.__battery = battery 

    def call(self, number):
        print(f"{self.brand} {self.model} is calling {number}...")

    def get_battery_status(self):
        return f"Battery level: {self.__battery}%"

    def charge(self):
        self.__battery = 100
        print(f"{self.brand} {self.model} is now fully charged!")

class Smartwatch(Smartphone):
    def __init__(self, brand, model, storage, battery, strap_material):
        super().__init__(brand, model, storage, battery)
        self.strap_material = strap_material

    def track_fitness(self):
        print(f"{self.brand} {self.model} is tracking your steps and heart rate.")

class Animal:
    def move(self):
        pass

class Bird(Animal):
    def move(self):
        print("Flying high in the sky! ✈️")

class Fish(Animal):
    def move(self):
        print("Swimming through the water! 🐟")

class Cat(Animal):
    def move(self):
        print("Walking gracefully on the ground! 🐾")

if __name__ == "__main__":
    # Assignment 1 demonstration
    print("Assignment 1: Smartphone and Smartwatch\n")
    phone = Smartphone("Apple", "iPhone 14", "128GB", 80)
    watch = Smartwatch("Samsung", "Galaxy Watch 5", "32GB", 60, "Silicone")

    phone.call("123-456-7890")
    print(phone.get_battery_status())
    phone.charge()

    watch.track_fitness()
    print(watch.get_battery_status())
    watch.charge()

    print("\nActivity 2: Polymorphism Challenge\n")
    # Activity 2 demonstration
    animals = [Bird(), Fish(), Cat()]
    for animal in animals:
        animal.move()
