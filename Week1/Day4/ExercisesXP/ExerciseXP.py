
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
#