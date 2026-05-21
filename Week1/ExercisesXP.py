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