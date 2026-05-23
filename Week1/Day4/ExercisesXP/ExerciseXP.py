
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
#
#
# Exercise 3 : Pet Dogs
import random
class Dog:
    # Constructor
    def __init__(self, name, age, weight):
        self.name = name
        self.age = age
        self.weight = weight
    # Bark method
    def bark(self):
        return f"{self.name} is barking"

# Child class : PetDog
class PetDog(Dog):
    # Constructor
    def __init__(self, name, age, weight):
        # Inherit attributes from Dog
        super().__init__(name, age, weight)
        self.trained = False
    # Train method
    def train(self):
        print(self.bark())
        self.trained = True
    # Play method
    def play(self, *args):
        dog_names = [self.name]
        for dog in args:
            dog_names.append(dog.name)
        print(f"{', '.join(dog_names)} all play together")
    # Random trick method
    def do_a_trick(self):
        if self.trained:
            tricks = [
                "does a barrel roll",
                "stands on his back legs",
                "shakes your hand",
                "plays dead"
            ]
            print(f"{self.name} {random.choice(tricks)}"
# Step 3 : Test PetDog methods
dog1 = PetDog("Fido", 2, 10)
dog2 = PetDog("Buddy", 3, 15)
dog3 = PetDog("Max", 4, 20)
# Train dog
dog1.train()
# Dogs play together
dog1.play(dog2, dog3)
# Dog does a trick
dog1.do_a_trick()
#
# Exercise 4 : Family and Person
# Step 1 : Create the Person class
class Person:
    # Constructor
    def __init__(self, first_name, age):
        self.first_name = first_name
        self.age = age
        self.last_name = ""
    # Method to check if person is 18 or older
    def is_18(self):
        return self.age >= 18
# Step 2 : Create the Family class
class Family:
    # Constructor
    def __init__(self, last_name):
        self.last_name = last_name
        self.members = []
    # Add a new family member
    def born(self, first_name, age):
        # Create Person object
        person = Person(first_name, age)
        # Give family name
        person.last_name = self.last_name
        # Add to members list
        self.members.append(person)
    # Check if member is allowed to go out
    def check_majority(self, first_name):
        # Search for the person
        for member in self.members:
            if member.first_name == first_name:
                # Check age
                if member.is_18():
                    print(
                        f"You are over 18, your parents Jane and John accept that you will go out with your friends"
                    )
                else:
                    print(
                        "Sorry, you are not allowed to go out with your friends."
                    )
                return
        # If person not found
        print("Person not found.")
    # Display family information
    def family_presentation(self):
        print(f"\nThe {self.last_name} family:\n")
        for member in self.members:
            print(
                f"Name: {member.first_name} {member.last_name} | Age: {member.age}"
            )
# Create family
my_family = Family("Smith")
# Add family members
my_family.born("John", 45)
my_family.born("Jane", 42)
my_family.born("Emma", 20)
my_family.born("Tom", 15)
# Check majority
my_family.check_majority("Emma")
my_family.check_majority("Tom")
# Display family information
my_family.family_presentation()