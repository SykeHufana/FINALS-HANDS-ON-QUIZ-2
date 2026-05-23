# shop/models.py
from django.db import models

# PART 1: Base Model
class Vehicle(models.Model):
    brand = models.CharField(max_length=255)
    price = models.FloatField()

    def vehicle_info(self):
        formatted_price = int(self.price) if self.price.is_integer() else self.price
        return f"{self.brand} costs {formatted_price}"

    def __str__(self):
        return self.brand

# PART 2: Child Models (Inheritance)
class Car(Vehicle):
    doors = models.IntegerField()

    def vehicle_info(self):
        formatted_price = int(self.price) if self.price.is_integer() else self.price
        return f"{self.brand} Car with {self.doors} doors costs {formatted_price}"

class Motorcycle(Vehicle):
    helmet_included = models.BooleanField(default=True)

    def vehicle_info(self):
        formatted_price = int(self.price) if self.price.is_integer() else self.price
        return f"{self.brand} Motorcycle costs {formatted_price}"