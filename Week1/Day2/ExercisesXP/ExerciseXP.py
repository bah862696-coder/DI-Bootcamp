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

# Exercise 3: Zara
# Principaux sujets en Python :
#
# Création de dictionnaires
# Accéder aux éléments du dictionnaire et les modifier
# Les méthodes de dictionnaire comme .pop() et .update()
#
# Instructions
#
# Créer et manipuler un dictionnaire contenant des informations sur la marque Zara.
#
# Informations sur la marque :
#
# name: Zara
# creation_date: 1975
# creator_name: Amancio Ortega Gaona
# type_of_clothes: men, women, children, home
# international_competitors: Gap, H&M, Benetton
# number_stores: 7000
# major_color:
#     France: blue,
#     Spain: red,
#     US: pink, green
#
# Créez un dictionnaire contenant les données fournies.
# Modifiez et accédez au dictionnaire comme suit :
# Modifiez la valeur de number_stores à 2.
# Imprimez une phrase décrivant les clients de Zara en utilisant la légende type_of_clothes.
# Ajoutez une nouvelle clé country_creation avec la valeur Spain.
# Vérifiez si international_competitors existe et, si oui, ajoutez « Desigual » à la liste.
# Supprimez la clé creation_date.
# Imprimez le dernier élément dans international_competitors.
# Imprimez les principales couleurs aux États-Unis.
# Affichez le nombre de clés dans le dictionnaire.
# Imprimez toutes les clés du dictionnaire.
#
# Prime:
#
# Créez un autre dictionnaire appelé more_on_zara avec creation_date et number_stores. Fusionnez ce dictionnaire avec le dictionnaire original brand et affichez le résultat.

brand = {
    'name': 'Zara',
    'creation_date': 1975,
    'creator_name': 'Amancio Ortega Gaona',
    'type_of_clothes': ['men', 'women', 'children', 'home'],
    'international_competitors': ['Gap', 'H&M', 'Benetton'],
    'number_stores': 7000,
    'major_color': {
        'France': 'blue',
        'Spain': 'red',
        'US': ['pink', 'green']
    }
}

brand['number_stores'] = 2
print(f"Zara vend des vêtements pour {', '.join(brand['type_of_clothes'])}.")
brand['country_creation'] = 'Spain'

if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

brand.pop('creation_date', None)
print(f"Dernier concurrent international : {brand['international_competitors'][-1]}")
print(f"Couleurs principales aux États-Unis : {', '.join(brand['major_color']['US'])}")
print(f"Nombre de clés dans le dictionnaire : {len(brand)}")
print(f"Clés du dictionnaire : {list(brand.keys())}")

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}
brand.update(more_on_zara)
print('Dictionnaire Zara après fusion :', brand)
