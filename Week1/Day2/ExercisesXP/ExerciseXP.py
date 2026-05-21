# Exercise 1: Converting Lists into Dictionaries
# Key Python Topics:# ==================================================
# Exercise 1 : Creating Dictionaries
# ==================================================

# Instructions:
# You are given two lists.
# Convert them into a dictionary where the first list
# contains the keys and the second list contains
# the corresponding values.
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# Expected output:
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))

print(result)


# ==================================================
# Exercise 2 : Cinemax
# ==================================================

# Instructions:
# Write a program that calculates the total cost
# of movie tickets for a family.
#
# Ticket rules:
# - Under 3 years old: Free
# - Between 3 and 12 years old: $10
# - Over 12 years old: $15
#
# family = {
#     "rick": 43,
#     "beth": 13,
#     "morty": 5,
#     "summer": 8
# }
#
# Print the ticket price for each family member
# and the total cost.

family = {
    "rick": 43,
    "beth": 13,
    "morty": 5,
    "summer": 8
}

total_cost = 0

for name, age in family.items():

    if age < 3:
        ticket_price = 0

    elif age <= 12:
        ticket_price = 10

    else:
        ticket_price = 15

    total_cost += ticket_price

    print(f"{name.title()} has to pay ${ticket_price}")

print(f"Total cost: ${total_cost}")


# Bonus

family = {}
total_cost = 0

while True:

    name = input("Enter family member name (or 'done' to finish): ")

    if name.lower() == "done":
        break

    age = int(input(f"Enter age for {name}: "))

    family[name] = age

for name, age in family.items():

    if age < 3:
        ticket_price = 0

    elif age <= 12:
        ticket_price = 10

    else:
        ticket_price = 15

    total_cost += ticket_price

    print(f"{name.title()} has to pay ${ticket_price}")

print(f"Total cost: ${total_cost}")


# ==================================================
# Exercise 3 : Zara
# ==================================================

# Instructions:
# Create and manipulate a dictionary containing
# information about the Zara brand.
#
# Tasks:
# - Change number_stores to 2
# - Print the type of clothes
# - Add country_creation
# - Add Desigual to competitors
# - Remove creation_date
# - Print last competitor
# - Print US colors
# - Print number of keys
# - Print all keys
# - Merge another dictionary

brand = {
    "name": "Zara",
    "creation_date": 1975,
    "creator_name": "Amancio Ortega Gaona",
    "type_of_clothes": ["men", "women", "children", "home"],
    "international_competitors": ["Gap", "H&M", "Benetton"],
    "number_stores": 7000,
    "major_color": {
        "France": "blue",
        "Spain": "red",
        "US": ["pink", "green"]
    }
}

brand["number_stores"] = 2

print("Zara's clients are:",
      ", ".join(brand["type_of_clothes"]))

brand["country_creation"] = "Spain"

if "international_competitors" in brand:
    brand["international_competitors"].append("Desigual")

brand.pop("creation_date")

print(brand["international_competitors"][-1])

print(brand["major_color"]["US"])

print(len(brand))

print(brand.keys())

more_on_zara = {
    "creation_date": 1975,
    "number_stores": 10000
}

brand.update(more_on_zara)

print(brand)


# ==================================================
# Exercise 4 : Cities
# ==================================================

# Instructions:
# Create a function called describe_city().
#
# The function should accept:
# - city
# - country (default value = "Unknown")
#
# Print:
# "<city> is in <country>"

def describe_city(city, country="Unknown"):

    print(f"{city} is in {country}")


describe_city("Reykjavik", "Iceland")
describe_city("Paris")


# ==================================================
# Exercise 5 : Random Number
# ==================================================

# Instructions:
# Create a function that:
# - accepts a number between 1 and 100
# - generates a random number
# - compares both numbers
# - prints Success or Fail

import random


def compare_numbers(user_number):

    random_number = random.randint(1, 100)

    if user_number == random_number:
        print("Success!")

    else:
        print(f"Fail! Your number: {user_number}, Random number: {random_number}")


compare_numbers(50)


# ==================================================
# Exercise 6 : T-Shirts
# ==================================================

# Instructions:
# Create a function make_shirt().
#
# Parameters:
# - size
# - text
#
# Default values:
# - size = "large"
# - text = "I love Python"

def make_shirt(size="large", text="I love Python"):

    print(f"The size of the shirt is {size} and the text is '{text}'")


make_shirt()
make_shirt("medium")
make_shirt("small", "Custom message")
make_shirt(size="small", text="Hello!")


# ==================================================
# Exercise 7 : Temperature Advice
# ==================================================

# Instructions:
# Create a function get_random_temp()
# that returns a random temperature
# between -10 and 40.
#
# Display advice according to the temperature.

def get_random_temp():

    return random.randint(-10, 40)


def main():

    temp = get_random_temp()

    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr! It's freezing! Wear extra layers today.")

    elif temp <= 16:
        print("Quite chilly! Don't forget your coat.")

    elif temp <= 23:
        print("Nice weather.")

    elif temp <= 32:
        print("It's warm. Stay hydrated.")

    else:
        print("It's really hot! Stay cool.")


main()


# ==================================================
# Exercise 8 : Pizza Toppings
# ==================================================

# Instructions:
# Ask the user to enter pizza toppings.
#
# Stop when the user types "quit".
#
# Print:
# "I will add <topping> to your pizza."
#
# Calculate:
# - Base price = $10
# - Each topping = $2.50
#
# Print the final pizza cost.

pizza_toppings = []

while True:

    topping = input("Enter a pizza topping (or 'quit' to finish): ")

    if topping.lower() == "quit":
        break

    pizza_toppings.append(topping)

    print(f"I will add {topping} to your pizza.")

# Base price
pizza_cost = 10

# Add toppings price
pizza_cost += len(pizza_toppings) * 2.50

print(f"Your pizza toppings are: {', '.join(pizza_toppings)}")

print(f"Total cost: ${pizza_cost:.2f}")
