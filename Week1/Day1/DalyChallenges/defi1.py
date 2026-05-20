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