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
