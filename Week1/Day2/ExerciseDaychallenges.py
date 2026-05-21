# Défi 1 : Dictionnaire d’index des lettres
# Objectif : Créer un dictionnaire qui stocke les indices
# (numéro de position) de chaque lettre d'un mot fourni par l'utilisateur.

# Principaux sujets en Python :
# - input()
# - dictionnaires
# - boucles for
# - conditions if / else
# - manipulation de chaînes
# - listes

# Instructions :
# 1. Demander à l'utilisateur de saisir un mot.
# 2. Parcourir chaque caractère du mot.
# 3. Vérifier si la lettre existe déjà dans le dictionnaire :
#    - Si oui, ajouter l’index dans la liste.
#    - Sinon, créer une nouvelle clé avec une liste contenant l’index.
# 4. Afficher le dictionnaire final.

# Demande du mot à l'utilisateur
mot = input("Entrez un mot : ")

# Création du dictionnaire vide
index_lettres = {}

# Parcours du mot avec les indices
for index, lettre in enumerate(mot):

    # Vérifie si la lettre existe déjà dans le dictionnaire
    if lettre in index_lettres:
        index_lettres[lettre].append(index)

    # Sinon on crée une nouvelle entrée
    else:
        index_lettres[lettre] = [index]

# Affichage du résultat
print(index_lettres)
#
# Défi 2 : Articles abordables
# Objectif : Créer un programme qui imprime une liste
# d'articles pouvant être achetés avec une somme d'argent donnée.

# Principaux sujets en Python :
# - Dictionnaires
# - Boucles for
# - Conditions if / else
# - Manipulation de chaînes (replace())
# - Conversion de type (int())
# - Listes
# - Tri (sorted())

# ---------------------------------------------------
# Instructions :
#
# 1. Stocker les données :
#    - Utiliser un dictionnaire items_purchase
#    - Utiliser une variable wallet
#
# 2. Nettoyage des données :
#    - Supprimer le signe $
#    - Supprimer les virgules
#
# 3. Déterminer les articles abordables :
#    - Ajouter les articles achetables dans une liste basket
#    - Mettre à jour le montant du portefeuille après achat
#
# 4. Si aucun article n'est achetable :
#    - Afficher "Nothing"
#
# 5. Sinon :
#    - Afficher la liste triée alphabétiquement
# ---------------------------------------------------

# Données
items_purchase = {
    "Water": "$1",
    "Bread": "$3",
    "TV": "$1,000",
    "Fertilizer": "$20"
}

wallet = "$300"

# Nettoyage du wallet
wallet = wallet.replace("$", "")
wallet = wallet.replace(",", "")

# Conversion en entier
wallet = int(wallet)

# Liste des articles achetables
basket = []

# Parcours du dictionnaire
for item, price in items_purchase.items():

    # Nettoyage du prix
    clean_price = price.replace
    clean_price = clean_price.replace(",", "")

    # Conversion en entier
    clean_price = int(clean_price)

    # Vérifie si l'article peut être acheté
    if clean_price <= wallet:
        basket.append(item)

        # Mise à jour du portefeuille
        wallet -= clean_price

# Vérifie si le panier est vide
if len(basket) == 0:
    print("Nothing")

else:
    # Trie alphabétique
    basket = sorted(basket)

    print(basket)