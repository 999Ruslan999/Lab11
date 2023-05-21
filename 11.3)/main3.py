class Restaurant:
    def __init__(self, name, cuisine_type, rating):
        self.name = name
        self.cuisine_type = cuisine_type
        self.rating = rating

    def describe_restaurant(self):
        print(f"{self.name} - {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")

    def open_restaurant(self):
        print(f"{self.name} открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating

restaurant1 = Restaurant("Русский двор", "Русская кухня", 4.5)
restaurant2 = Restaurant("Французская пекарня", "Французская кухня", 4.8)
restaurant3 = Restaurant("Японский сад", "Японская кухня", 4.3)

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

restaurant1.update_rating(4.7)
restaurant1.describe_restaurant()