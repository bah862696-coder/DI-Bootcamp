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

# Exercise 2: Cinemax n� 2
# Principaux sujets en Python :
#
# Parcourir les dictionnaires
# Les conditionnelles
# Calculs
#
# Instructions
#
# �crivez un programme qui calcule le co�t total des billets de cin�ma pour une famille en fonction de l'�ge de ses membres.
#
# L'�ge des membres de la famille est stock� dans un dictionnaire.
# Les r�gles de tarification des billets sont les suivantes :
# Moins de 3 ans : gratuit
# De 3 � 12 ans : 10 $
# Plus de 12 ans : 15 $
#
# Donn�es familiales :
#
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#
# Parcourez le dictionnaire family pour calculer le co�t total.
# Imprimez le prix du billet pour chaque membre de la famille.
# Imprimez le co�t total � la fin.
#
# Prime:
#
# Permettez � l'utilisateur de saisir les noms et �ges des membres de sa famille, puis calculez le co�t total du billet.

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

print(f"Co�t total des billets : {total_cost} $")

# Exercise 3: Zara
# Principaux sujets en Python :
#
# Cr�ation de dictionnaires
# Acc�der aux �l�ments du dictionnaire et les modifier
# Les m�thodes de dictionnaire comme .pop() et .update()
#
# Instructions
#
# Cr�er et manipuler un dictionnaire contenant des informations sur la marque Zara.
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
# Cr�ez un dictionnaire contenant les donn�es fournies.
# Modifiez et acc�dez au dictionnaire comme suit :
# Modifiez la valeur de number_stores � 2.
# Imprimez une phrase d�crivant les clients de Zara en utilisant la l�gende type_of_clothes.
# Ajoutez une nouvelle cl� country_creation avec la valeur Spain.
# V�rifiez si international_competitors existe et, si oui, ajoutez � Desigual � � la liste.
# Supprimez la cl� creation_date.
# Imprimez le dernier �l�ment dans international_competitors.
# Imprimez les principales couleurs aux �tats-Unis.
# Affichez le nombre de cl�s dans le dictionnaire.
# Imprimez toutes les cl�s du dictionnaire.
#
# Prime:
#
# Cr�ez un autre dictionnaire appel� more_on_zara avec creation_date et number_stores. Fusionnez ce dictionnaire avec le dictionnaire original brand et affichez le r�sultat.

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
print(f"Zara vend des v�tements pour {', '.join(brand['type_of_clothes'])}.")
brand['country_creation'] = 'Spain'

if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

brand.pop('creation_date', None)
print(f"Dernier concurrent international : {brand['international_competitors'][-1]}")
print(f"Couleurs principales aux �tats-Unis : {', '.join(brand['major_color']['US'])}")
print(f"Nombre de cl�s dans le dictionnaire : {len(brand)}")
print(f"Cl�s du dictionnaire : {list(brand.keys())}")

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}
brand.update(more_on_zara)
print('Dictionnaire Zara apr�s fusion :', brand)

# Exercise 4: Un peu de g�ographie
# Objectif : Cr�er une fonction qui d�crit une ville et son pays.
#
# Principaux sujets en Python :
#
# Fonctions � plusieurs param�tres
# valeurs des param�tres par d�faut
# formatage de cha�nes
#
# �tape 1 : D�finir une fonction avec des param�tres
#
# D�finissez une fonction nomm�e describe_city().
# Cette fonction doit accepter deux param�tres : city et country.
# Attribuez au param�tre country une valeur par d�faut, telle que "Inconnu".
#
# �tape 2 : Imprimer un message
#
# � l'int�rieur de la fonction, configurez le code pour afficher une phrase comme "<city> is in <country>".
# Remplacez <city> et <country> par les valeurs des param�tres.
#
# �tape 3 : Appeler la fonction
#
# Appelez la describe_city() fonction avec diff�rentes combinaisons de ville et de pays.
# Essayez de l'appeler avec et sans fournir l'argument pays pour voir la valeur par d�faut en action.
# Exemple : describe_city("Reykjavik", "Iceland") et describe_city("Paris").
#
# R�sultat attendu :
#
# Reykjavik is in Iceland.
# Paris is in Unknown.

def describe_city(city, country='Unknown'):
    print(f"{city} is in {country}.")

# Appels de test
describe_city('Reykjavik', 'Iceland')
describe_city('Abidjan')