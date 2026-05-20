# Exercice 7 : Pair ou impair
# Instructions: Demandez à l'utilisateur un nombre et déterminez s'il est pair ou impair.

num_str = input("Entrez un nombre: ")
try:
    num = int(num_str)
    if num % 2 == 0:
        print(f"{num} est pair")
    else:
        print(f"{num} est impair")
except ValueError:
    print("Entrée invalide: veuillez entrer un nombre entier.")
