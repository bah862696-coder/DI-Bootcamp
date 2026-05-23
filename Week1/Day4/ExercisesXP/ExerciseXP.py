
# Exercise 1 : Pets

# Base class : Pets
class Pets():
    def __init__(self, animals):
        self.animals = animals
    def walk(self):
        for animal in self.animals:
            print(animal.walk())
# Base class : Cat
class Cat():
    is_lazy = True
    # Constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    # Walk method
    def walk(self):
        return f"{self.name} is just walking around"
# Bengal class
class Bengal(Cat):
    def sing(self, sounds):
        return f"{sounds}"
# Chartreux class
class Chartreux(Cat):
    def sing(self, sounds):
        return f"{sounds}"
# Step 1 : Create Siamese class
class Siamese(Cat):
    def sing(self, sounds):
        return f"{sounds}"

# Step 2 : Create cat objects
cat1 = Bengal("Leo", 2)
cat2 = Chartreux("Milo", 4)
cat3 = Siamese("Luna", 3)

# Create list of cats
all_cats = [cat1, cat2, cat3]
# Step 3 : Create Pets instance
sara_pets = Pets(all_cats)

# Step 4 : Walk the cats
sara_pets.walk()
#
#
# Exercise 2 : Dogs
# Step 1 : Create the Dog class
class Dog:
    # Constructor
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    # Bark method
    def bark(self):
        return f"{self.name} is barking"
    # Run speed method
    def run_speed(self):
        return (self.weight / self.age) * 10
    # Fight method
    def fight(self, other_dog):
        my_power = self.run_speed() * self.weight
        other_power = other_dog.run_speed() * other_dog.weight
        if my_power > other_power:
            return f"{self.name} wins the fight against {other_dog.name}"
        elif other_power > my_power:
            return f"{other_dog.name} wins the fight against {self.name}"
        else:
            return "It's a tie!"

# Step 2 : Create dog instances
dog1 = Dog("Rocky", 4, 20)
dog2 = Dog("Max", 5, 25)
dog3 = Dog("Buddy", 2, 15)
# Step 3 : Test methods
print(dog1.bark())
print(dog2.run_speed())
print(dog1.fight(dog2))