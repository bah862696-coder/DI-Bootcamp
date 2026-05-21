# ==================================================
# Exercise 1 : Cats
# ==================================================
# Instructions:
# Create 3 cat objects using the Cat class.
# Create a function that finds the oldest cat.
# Print the oldest cat's name and age.
# Create the Cat class
class Cat:

    # Constructor
    def __init__(self, cat_name, cat_age):

        # Attributes
        self.name = cat_name
        self.age = cat_age
# ==================================================
# Step 1 : Create cat objects
# ==================================================
cat1 = Cat("Milo", 2)
cat2 = Cat("Luna", 5)
cat3 = Cat("Simba", 3)
#
# ==================================================
# Step 2 : Function to find the oldest cat
# ==================================================
def find_oldest_cat(cat1, cat2, cat3):
    # Assume cat1 is the oldest
    oldest_cat = cat1
    # Compare with cat2
    if cat2.age > oldest_cat.age:
        oldest_cat = cat2
    # Compare with cat3
    if cat3.age > oldest_cat.age:
        oldest_cat = cat3
    # Return the oldest cat
    return oldest_cat
# ==================================================
# Step 3 : Print oldest cat details
#
oldest = find_oldest_cat(cat1, cat2, cat3)
print(f"The oldest cat is {oldest.name} and is {oldest.age} years old.")
#
#
# ==================================================
# Exercise 2 : Dogs
# ==================================================
# Instructions:
# Create a Dog class.
# Create methods for barking and jumping.
# Create dog objects.
# Print their information.
# Compare their sizes.
# ==================================================
# Step 1 : Create the Dog class
# ==================================================
class Dog:

    # Constructor
    def __init__(self, name, height):

        # Attributes
        self.name = name
        self.height = height

    # Bark method
    def bark(self):

        print(f"{self.name} goes woof!")

    # Jump method
    def jump(self):

        print(f"{self.name} jumps {self.height * 2} cm high!")
# ==================================================
# Step 2 : Create dog objects
# ==================================================
davids_dog = Dog("Rex", 50)
sarahs_dog = Dog("Bella", 40)
# ==================================================
# Step 3 : Print dog information
# ==================================================
print(f"{davids_dog.name} is {davids_dog.height} cm tall.")
davids_dog.bark()
davids_dog.jump()
print()
print(f"{sarahs_dog.name} is {sarahs_dog.height} cm tall.")
sarahs_dog.bark()
sarahs_dog.jump()
# ==================================================
# Step 4 : Compare dog sizes
# ==================================================
if davids_dog.height > sarahs_dog.height:

    print(f"{davids_dog.name} is taller than {sarahs_dog.name}.")

elif sarahs_dog.height > davids_dog.height:

    print(f"{sarahs_dog.name} is taller than {davids_dog.name}.")

else:

    print("Both dogs are the same height.")