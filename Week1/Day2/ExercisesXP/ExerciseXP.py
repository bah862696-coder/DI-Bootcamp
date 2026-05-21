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

import random

keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

result = dict(zip(keys, values))
print(result)

# Exercise 2: Cinemax nï¿½ 2
# Principaux sujets en Python :
#
# Parcourir les dictionnaires
# Les conditionnelles
# Calculs
#
# Instructions
#
# ï¿½crivez un programme qui calcule le coï¿½t total des billets de cinï¿½ma pour une famille en fonction de l'ï¿½ge de ses membres.
#
# L'ï¿½ge des membres de la famille est stockï¿½ dans un dictionnaire.
# Les rï¿½gles de tarification des billets sont les suivantes :
# Moins de 3 ans : gratuit
# De 3 ï¿½ 12 ans : 10 $
# Plus de 12 ans : 15 $
#
# Donnï¿½es familiales :
#
# family = {"rick": 43, 'beth': 13, 'morty': 5, 'summer': 8}
#
# Parcourez le dictionnaire family pour calculer le coï¿½t total.
# Imprimez le prix du billet pour chaque membre de la famille.
# Imprimez le coï¿½t total ï¿½ la fin.
#
# Prime:
#
# Permettez ï¿½ l'utilisateur de saisir les noms et ï¿½ges des membres de sa famille, puis calculez le coï¿½t total du billet.

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

print(f"Coï¿½t total des billets : {total_cost} $")

# Exercise 3: Zara
# Principaux sujets en Python :
#
# Crï¿½ation de dictionnaires
# Accï¿½der aux ï¿½lï¿½ments du dictionnaire et les modifier
# Les mï¿½thodes de dictionnaire comme .pop() et .update()
#
# Instructions
#
# Crï¿½er et manipuler un dictionnaire contenant des informations sur la marque Zara.
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
# Crï¿½ez un dictionnaire contenant les donnï¿½es fournies.
# Modifiez et accï¿½dez au dictionnaire comme suit :
# Modifiez la valeur de number_stores ï¿½ 2.
# Imprimez une phrase dï¿½crivant les clients de Zara en utilisant la lï¿½gende type_of_clothes.
# Ajoutez une nouvelle clï¿½ country_creation avec la valeur Spain.
# Vï¿½rifiez si international_competitors existe et, si oui, ajoutez ï¿½ Desigual ï¿½ ï¿½ la liste.
# Supprimez la clï¿½ creation_date.
# Imprimez le dernier ï¿½lï¿½ment dans international_competitors.
# Imprimez les principales couleurs aux ï¿½tats-Unis.
# Affichez le nombre de clï¿½s dans le dictionnaire.
# Imprimez toutes les clï¿½s du dictionnaire.
#
# Prime:
#
# Crï¿½ez un autre dictionnaire appelï¿½ more_on_zara avec creation_date et number_stores. Fusionnez ce dictionnaire avec le dictionnaire original brand et affichez le rï¿½sultat.

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
print(f"Zara vend des vï¿½tements pour {', '.join(brand['type_of_clothes'])}.")
brand['country_creation'] = 'Spain'

if 'international_competitors' in brand:
    brand['international_competitors'].append('Desigual')

brand.pop('creation_date', None)
print(f"Dernier concurrent international : {brand['international_competitors'][-1]}")
print(f"Couleurs principales aux ï¿½tats-Unis : {', '.join(brand['major_color']['US'])}")
print(f"Nombre de clï¿½s dans le dictionnaire : {len(brand)}")
print(f"Clï¿½s du dictionnaire : {list(brand.keys())}")

more_on_zara = {
    'creation_date': 1975,
    'number_stores': 10000
}
brand.update(more_on_zara)
print('Dictionnaire Zara aprï¿½s fusion :', brand)

# Exercise 4: Un peu de gï¿½ographie
# Objectif : Crï¿½er une fonction qui dï¿½crit une ville et son pays.
#
# Principaux sujets en Python :
#
# Fonctions ï¿½ plusieurs paramï¿½tres
# valeurs des paramï¿½tres par dï¿½faut
# formatage de chaï¿½nes
#
# ï¿½tape 1 : Dï¿½finir une fonction avec des paramï¿½tres
#
# Dï¿½finissez une fonction nommï¿½e describe_city().
# Cette fonction doit accepter deux paramï¿½tres : city et country.
# Attribuez au paramï¿½tre country une valeur par dï¿½faut, telle que "Inconnu".
#
# ï¿½tape 2 : Imprimer un message
#
# ï¿½ l'intï¿½rieur de la fonction, configurez le code pour afficher une phrase comme "<city> is in <country>".
# Remplacez <city> et <country> par les valeurs des paramï¿½tres.
#
# ï¿½tape 3 : Appeler la fonction
#
# Appelez la describe_city() fonction avec diffï¿½rentes combinaisons de ville et de pays.
# Essayez de l'appeler avec et sans fournir l'argument pays pour voir la valeur par dï¿½faut en action.
# Exemple : describe_city("Reykjavik", "Iceland") et describe_city("Paris").
#
# Rï¿½sultat attendu :
#
# Reykjavik is in Iceland.
# Paris is in Unknown.

def describe_city(city, country='Unknown'):
    print(f"{city} is in {country}.")

# Appels de test
describe_city('Reykjavik', 'Iceland')
describe_city('Abidjan')
# Exercise 5: Alï¿½atoire
# Objectif : Crï¿½er une fonction qui gï¿½nï¿½re des nombres alï¿½atoires et les compare.
#
# Principaux sujets en Python :
#
# random module
# random.randint() fonction
# Instructions conditionnelles (if, else)
#
# ï¿½tape 1 : Importer le random module
#
# Au dï¿½but de votre script, utilisez cette fonction import random pour accï¿½der aux fonctions de gï¿½nï¿½ration de nombres alï¿½atoires.
#
# ï¿½tape 2 : Dï¿½finir une fonction avec un paramï¿½tre
#
# Crï¿½ez une fonction qui accepte un nombre compris entre 1 et 100 comme paramï¿½tre.
#
# ï¿½tape 3 : Gï¿½nï¿½rer un nombre alï¿½atoire
#
# ï¿½ l'intï¿½rieur de la fonction, utilisez random.randint(1, 100) pour gï¿½nï¿½rer un entier alï¿½atoire compris entre 1 et 100.
#
# ï¿½tape 4 : Comparer les nombres
#
# S'ils sont identiques, afficher un message de rï¿½ussite. Sinon, afficher un message d'ï¿½chec et les deux nombres.
#
# ï¿½tape 5 : Appeler la fonction
#
# Appelez la fonction avec un nombre compris entre 1 et 100.
#
# Rï¿½sultat attendu :
#
# Success! (if the numbers match)
# Fail! Your number: 50, Random number: 23 (if they don't match)

def compare_with_random(user_number):
    random_number = random.randint(1, 100)
    if user_number == random_number:
        print('Success!')
    else:
        print(f'Fail! Your number: {user_number}, Random number: {random_number}')

# Exemple d'appel
compare_with_random(50)

# Exercise 6: Crï¿½ons des t-shirts personnalisï¿½s !
# Objectif : Crï¿½er une fonction permettant de dï¿½crire la taille et le message d'un t-shirt, avec des valeurs par dï¿½faut.
#
# Principaux sujets en Python :
#
# Fonctions avec paramï¿½tres et valeurs par dï¿½faut
# Arguments clï¿½s
#
# ï¿½tape 1 : Dï¿½finir une fonction avec des paramï¿½tres
#
# Dï¿½finissez une fonction appelï¿½e make_shirt().
# Cette fonction doit accepter deux paramï¿½tres : size et text.
#
# ï¿½tape 2 : Imprimer un message rï¿½capitulatif
#
# Configurez la fonction pour afficher une phrase rï¿½sumant la taille et le message du t-shirt.
#
# ï¿½tape 3 : Appeler la fonction
#
# ï¿½tape 4 : Modifier la fonction avec les valeurs par dï¿½faut
#
# Modifiez la make_shirt() fonction afin qu'elle size ait une valeur par dï¿½faut de ï¿½ large ï¿½ et text qu'elle ait une valeur par dï¿½faut de ï¿½ J'adore Python ï¿½.
#
# ï¿½tape 5 : Appeler la fonction avec les valeurs par dï¿½faut et les valeurs personnalisï¿½es
#
# Commandez make_shirt() un grand t-shirt avec le message par dï¿½faut.
# Commandez make_shirt() un t-shirt de taille moyenne avec le message par dï¿½faut.
# Appelez make_shirt() pour commander un t-shirt de n'importe quelle taille avec un message diffï¿½rent.
#
# ï¿½tape 6 (Bonus) : Arguments par mots-clï¿½s
#
# Appelez make_shirt() en utilisant des arguments nommï¿½s (par exemple, make_shirt(size="small", text="Hello!"))).
#
# Rï¿½sultat attendu :
#
# The size of the shirt is large and the text is I love Python.
# The size of the shirt is medium and the text is I love Python.
# The size of the shirt is small and the text is Custom message.

def make_shirt(size='large', text="I love Python"):
    print(f"The size of the shirt is {size} and the text is {text}.")

# Appels de test
make_shirt()
make_shirt('medium')
make_shirt('small', 'Custom message')
make_shirt(size='small', text='Hello!')

# Exercise 7: Conseils sur la tempï¿½rature
# Objectif : Gï¿½nï¿½rer une tempï¿½rature alï¿½atoire et fournir des conseils en fonction de cette plage de tempï¿½ratures.
#
# Principaux sujets en Python :
#
# Fonctions
# Conditionnelles (if/elif)
# nombres alï¿½atoires
# Nombres ï¿½ virgule flottante (Bonus)
# Gestion des saisons (Bonus)
#
# ï¿½tape 1 : Crï¿½er la get_random_temp() fonction
#
# Crï¿½ez une fonction get_random_temp() qui renvoie un entier alï¿½atoire compris entre -10 et 40 degrï¿½s Celsius.
#
# ï¿½tape 2 : Crï¿½er la main() fonction
#
# Crï¿½ez une fonction appelï¿½e main(). ï¿½ l'intï¿½rieur de cette fonction :
# Appelez get_random_temp() pour obtenir une tempï¿½rature alï¿½atoire.
# Stockez la tempï¿½rature dans une variable et affichez un message convivial comme :
# "La tempï¿½rature actuelle est de 32 degrï¿½s Celsius."
#
# ï¿½tape 3 : Fournir des conseils basï¿½s sur la tempï¿½rature
#
# ï¿½ l'intï¿½rieur de main(), donnez des conseils en fonction de la tempï¿½rature :
# En dessous de 0ï¿½C : par exemple, "Brrr, il fait un froid de canard ! Mets des vï¿½tements supplï¿½mentaires aujourd'hui."
# Entre 0ï¿½C et 16ï¿½C : par exemple, "Il fait assez froid ! N'oublie pas ton manteau."
# Entre 16ï¿½C et 23ï¿½C : par exemple, "Beau temps".
# Entre 24ï¿½C et 32ï¿½C : par exemple, "Il fait un peu chaud, pensez ï¿½ bien vous hydrater."
# Entre 32ï¿½C et 40ï¿½C : par exemple, "Il fait vraiment chaud ! Reste au frais."
#
# ï¿½tape 4 : Tempï¿½ratures ï¿½ virgule flottante (Bonus)
#
# Modifier get_random_temp() pour renvoyer un nombre ï¿½ virgule flottante avec random.uniform().
#
# ï¿½tape 5 : Saisons mensuelles (Bonus)
#
# Vous pouvez ï¿½galement appeler get_random_temp(month) avec un mois (1-12)
# pour prendre en compte des plages de tempï¿½ratures diffï¿½rentes selon les saisons.

def get_random_temp(month=None):
    if month is None:
        return round(random.uniform(-10, 40), 1)

    month = int(month)
    if month in [12, 1, 2]:
        low, high = -10, 20
    elif month in [3, 4, 5]:
        low, high = 0, 25
    elif month in [6, 7, 8]:
        low, high = 15, 40
    else:
        low, high = -5, 30

    return round(random.uniform(low, high), 1)


def main():
    temp = get_random_temp()
    print(f"The temperature right now is {temp} degrees Celsius.")

    if temp < 0:
        print("Brrr, il fait un froid de canard ! Mets des vï¿½tements supplï¿½mentaires aujourd'hui.")
    elif temp <= 16:
        print("Il fait assez froid ! N'oublie pas ton manteau.")
    elif temp <= 23:
        print("Beau temps.")
    elif temp <= 32:
        print("Il fait un peu chaud, pensez ï¿½ bien vous hydrater.")
    else:
        print("Il fait vraiment chaud ! Reste au frais.")


# Appel principal
main()
