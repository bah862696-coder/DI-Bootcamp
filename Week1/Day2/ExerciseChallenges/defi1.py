# ============================================
# Défi 1 : Dictionnaire d’index des lettres
# ============================================

# Fonction qui retourne les indices des lettres
def index_letters(word):

    result = {}

    for index, letter in enumerate(word):

        if letter in result:
            result[letter].append(index)

        else:
            result[letter] = [index]

    return result


# Test défi 1
word = input("Enter a word: ")
print(index_letters(word))


# ============================================
# Défi 2 : Articles abordables
# ============================================

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

wallet = int(wallet)

basket = []

# Parcours des articles
for item, price in items_purchase.items():

    # Nettoyage du prix
    clean_price = price.replace("$", "")
    clean_price = clean_price.replace(",", "")

    clean_price = int(clean_price)

    # Vérifie si l'article est achetable
    if clean_price <= wallet:

        basket.append(item)

        # Mise à jour du portefeuille
        wallet -= clean_price


# Affichage du résultat
if len(basket) == 0:
    print("Nothing")

else:
    print(sorted(basket))