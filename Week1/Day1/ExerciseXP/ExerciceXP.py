#EXERCISE1
# Imprimez le résultat suivant en utilisant une seule ligne de code :
print("Hello world\nHello world\nHello world\nHello world")
#EXERCISE2
# Écrivez un code qui calcule le résultat de :
#
 (99**3)*8

 # Exercice 3 : Quel est le résultat ?
# Instructions
# Prédisez le résultat des extraits de code suivants :
# indiquez votre prédiction en commentaire, puis exécutez le code et comparez.
#
# >>> 15 < 8    # False
# >>> 5 < 3     # False
# >>> 3 == 3    # True
# >>> 3 == "3"  # False
# >>> "3" > 3   # TypeError en Python (impossible de comparer int et str)
# >>> "Hello" == "hello"  # False

print(15 < 8)
print(5 < 3)
print(3 == 3)
print(3 == "3")
try:
    print("3" > 3)
except TypeError as error:
    print("TypeError:", error)
print("Hello" == "hello")
#
# Créez une variable computer_brand dont la valeur correspond à la marque de votre ordinateur.
# Remplacez la valeur de `computer_brand` par la marque réelle de votre ordinateur.

computer_brand = "HP Probook 445 14 inch G10"
print(f"I have a {computer_brand} computer.")

# Créez une variable computer_brand dont la valeur correspond à la marque de votre ordinateur.
# Remplacez la valeur de `computer_brand` par la marque réelle de votre ordinateur.

computer_brand = "HP Probook 445 14 inch G10"
print(f"I have a {computer_brand} computer.")
#
# Créez une variable computer_brand dont la valeur correspond à la marque de votre ordinateur.
# Remplacez la valeur de `computer_brand` par la marque réelle de votre ordinateur.

computer_brand = "HP Probook 445 14 inch G10"
print(f"I have a {computer_brand} computer.")
#
# Exercice 5 : Vos informations
# Instructions:
# - Créez une variable `name` et assignez-y votre nom.
# - Créez une variable `age` et assignez-y votre âge.
# - Créez une variable `shoe_size` et assignez-y votre pointure.
# - Créez une variable `info` contenant une phrase qui inclut les trois variables ci-dessus.
# - Affichez la variable `info`.

name = "Bah"
age = 24
shoe_size = 38

info = f"Je m'appelle {name}, j'ai {age} ans et ma pointure est {shoe_size}."
print(info)
#
# Exercice 6 : A et B
# Instructions:
# - Créez deux variables, a et b (valeurs numériques).
# - Si a est supérieure à b, afficher "Hello World".

a = 10
b = 5

if a > b:
    print("Hello World")
#
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
#
# Exercice 8 : Quel est votre nom ?
# Instructions:
# - Demandez à l'utilisateur son nom.
# - Vérifiez si l'utilisateur porte le même nom que vous.
# - Affichez un message humoristique selon le résultat.

my_name = "Bah"
user_name = input("Quel est votre nom ? ").strip()

if user_name.lower() == my_name.lower():
    print(f"Oh la coïncidence ! Nous nous appelons tous les deux {my_name} — sommes-nous des jumeaux cachés ? 😄")
else:
    print(f"Enchanté(e), {user_name} ! Moi, je m'appelle {my_name}. On fait une super équipe de noms différents ! 🤝")
#
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
