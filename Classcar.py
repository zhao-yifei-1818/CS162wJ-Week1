#!/usr/bin/env python3
import random
class Car:
    # Define a car
    def __init__(self, name, exterior_color = "no color", mileage = 0, year = "0000", brand = "Brand", ignition = False):
        self.name = name
        self.exterior_color = exterior_color
        self.mileage = mileage
        self.year = year
        self.brand = brand
        self.ignition = ignition
    def to_string(self): 
    # Have things printed out
        result = f"\t name: {self.name}\n"
        result += f"\t exterior color: {self.exterior_color}\n"
        result += f"\t mileage: {self.mileage}\n"
        result += f"\t year: {self.year}\n"
        result += f"\t brand: {self.brand}\n"
        result += f"\t ignition: {self.ignition}\n"
        return result
    def turn_on_the_car(self):
    # Turning ignition on or ask user to input a car first if there is no car
            # My porpose is to let engine status appears "true"
        self.ignition = True
        return self.ignition
    def drive(self):
    # Check if this car's engine is on, return a random driving location as a string.
        if self.ignition == False:
            result = (f"{self.brand} is unable to drive because engine is off, click turn-on-the-car(3) option!")
            print(result)
        if self.ignition:
        # Random drive time below
            rand = random.randrange(0, 2)
            location = "Drive to Corvallis"
            if rand == 0:
                location = "Drive to Albany"
            return location
def create_car():
    # Here are the section of creating an object
    name = input("Give you car a name to start")
    exterior_color = input("What's the exterior color of the car? ")
    mileage = int(input("In integer, what's the mileage of the car? "))
    year = input("In which year was the car made in? ")
    brand = input("What's the brand of this car? ")
    ignition = False

    new_car = Car(name, exterior_color, mileage, year, brand, ignition)
    return new_car
