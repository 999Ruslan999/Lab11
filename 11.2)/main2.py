class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.name} - {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.name} открыт!")

restaurant1 = Restaurant("Русский двор", "Русская кухня")
restaurant2 = Restaurant("Французская пекарня", "Французская кухня")
restaurant3 = Restaurant("Японский сад", "Японская кухня")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()