# Exercise 1: Converting Lists into Dictionaries
# Key Python Topics:
#
# Creating dictionaries
# Zip function or dictionary comprehension
#
# Instructions
#
# You are given two lists. Convert them into a dictionary where the first list contains the keys and the second list contains the corresponding values.
#
# Lists:
#
# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
#
# Expected Output:
#
# {'Ten': 10, 'Twenty': 20, 'Thirty': 30}

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)

# Exercise 2: Cinemax n° 2
# Principaux sujets en Python :
#
# Parcourir les dictionnaires
# Les conditionnelles
# Calculs
#
# Instructions
#
# Écrivez un programme qui calcule le coût total des billets de cinéma pour une famille en fonction de l'âge de ses membres.
#
# L'âge des membres de la famille est stocké dans un dictionnaire.
# Les règles de tarification des billets sont les suivantes :
# Moins de 3 ans : gratuit
# De 3 à 12 ans : 10 $
# Plus de 12 ans : 15 $
#
# Données familiales :
#
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#
# Parcourez le dictionnaire family pour calculer le coût total.
# Imprimez le prix du billet pour chaque membre de la famille.
# Imprimez le coût total à la fin.
#
# Prime:
#
# Permettez à l'utilisateur de saisir les noms et âges des membres de sa famille, puis calculez le coût total du billet.

family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}

total_cost = 0
for name, age in family.items():
    if age < 3:
        ticket_price = 0
    elif age <= 12:
        ticket_price = 10
    else:
        ticket_price = 15

    total_cost += ticket_price
    print(f"{name.title()} a {age} ans, prix du billet : {ticket_price} $")

print(f"Coût total des billets : {total_cost} $")
