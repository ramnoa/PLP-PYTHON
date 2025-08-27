#activity 1 design your own class
'''Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
Add attributes and methods to bring the class to life!
Use constructors to initialize each object with unique values.
Add an inheritance layer to explore polymorphism or encapsulation.'''
class Superhero:
    def __init__(self, name, superpower, alias):
        self.name = name
        self.superpower = superpower
        self.alias = alias

    def display_info(self):
        return f"Superhero Name: {self.name}, Alias: {self.alias}, Superpower: {self.superpower}"
Noah = Superhero("NOAH", "Flight, Super Strength", "Cartel")
print(Noah.display_info())

class Villain(Superhero):
    def __init__(self, name, superpower, alias, evil_plan):
        super().__init__(name, superpower, alias)
        self.evil_plan = evil_plan

    def display_info(self):
        base_info = super().display_info()
        return f"{base_info}, Evil Plan: {self.evil_plan}"
LexLuthor = Villain("Lex Luthor", "Genius Intellect", "Lex", "World Domination")
print(LexLuthor.display_info())

#Activity 2: Polymorphism Challenge! 🎭
'''Create a program that includes animals or vehicles with the same action (like move()).
 However, make each class define move() differently (for example, Car.move() prints "Driving" 🚗, 
 while Plane.move() prints "Flying" ✈️).'''
class Car:
    def move(self):
        return "Driving 🚗"
class Plane:
    def move(self):
        return "Flying ✈️"
