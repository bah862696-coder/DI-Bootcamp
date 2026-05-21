
# ==================================================
# Exercise : Old MacDonald's Farm
# ==================================================
# Instructions:
# Create a Farm class.
# The class should:
# - store animals in a dictionary
# - add animals
# - display farm information
# - sort animal names
# - create a short sentence about the farm
# ==================================================
# Step 1 : Create the Farm class
# ==================================================
class Farm:
    # Constructor
    def __init__(self, farm_name):
        # Attributes
        self.name = farm_name
        self.animals = {}

    # ==================================================
    # Step 3 : Add animals
    # ==================================================
    def add_animal(self, **kwargs):
        # Loop through animals
        for animal_type, count in kwargs.items():
            # If animal already exists
            if animal_type in self.animals:
                self.animals[animal_type] += count
            # Otherwise create it
            else:

                self.animals[animal_type] = count
    # ==================================================
    # Step 4 : Display farm information
    # ==================================================
    def get_info(self):
        info = f"{self.name}'s farm\n\n"
        # Display animals and counts
        for animal, count in self.animals.items():
            info += f"{animal} : {count}\n"
        info += "\nE-I-E-I-0!"
        return info
    # ==================================================
    # Step 6 : Return sorted animal names
    # ==================================================
    def get_animal_types(self):
        return sorted(self.animals.keys())
    # ==================================================
    # Step 7 : Short farm information
    # ==================================================
    def get_short_info(self):
        animal_list = self.get_animal_types()
        formatted_animals = []
        # Make plural if count > 1
        for animal in animal_list:
            if self.animals[animal] > 1:
                formatted_animals.append(animal + "s")
            else:
                formatted_animals.append(animal)
        # Create sentence
        animals_string = ", ".join(formatted_animals)

        return f"{self.name}'s farm has {animals_string}."
# ==================================================
# Step 5 : Test the code
# ==================================================
macdonald = Farm("McDonald")
macdonald.add_animal(
    cow=5,
    sheep=2,
    goat=12
)
print(macdonald.get_info())
print()
print(macdonald.get_short_info())