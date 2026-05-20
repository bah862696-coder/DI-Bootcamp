# Exercice 9 : Être assez grand pour faire des montagnes russes
# Instructions:
# - Demandez à l'utilisateur sa taille en centimètres.
# - S'ils mesurent plus de 145 cm, imprimez un message indiquant qu'ils sont assez grands pour monter à bord.
# - S'ils ne sont pas assez grands, imprimez un message indiquant qu'ils doivent encore grandir pour pouvoir monter à cheval.

height_str = input("Entrez votre taille en centimètres : ")
try:
    height = int(height_str)
    if height > 145:
        print("Vous êtes assez grand(e) pour monter à bord !")
    else:
        print("Vous devez encore grandir pour pouvoir monter à cheval.")
except ValueError:
    print("Entrée invalide : veuillez saisir un nombre entier en centimètres.")
