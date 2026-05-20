# Défi 1
# Demandez à l'utilisateur un number et un length.
# Créez un programme qui affiche une liste de multiples du nombre
# jusqu'à ce que la longueur de la liste atteigne la longueur spécifiée.

number_str = input("Entrez un nombre : ")
length_str = input("Entrez la longueur de la liste : ")
try:
    number = int(number_str)
    length = int(length_str)
    if length < 0:
        print("La longueur doit être un entier positif.")
    else:
        multiples = [number * i for i in range(1, length + 1)]
        print(multiples)
except ValueError:
    print("Entrée invalide : veuillez entrer des entiers.")
    #
    # Écrivez un programme qui demande une chaîne de caractères à l'utilisateur
# et affiche une nouvelle chaîne sans les lettres consécutives identiques.

user_word = input("Entrez une chaîne de caractères : ")

result = ""
for i, char in enumerate(user_word):
    if i == 0 or char != user_word[i - 1]:
        result += char

print(result)