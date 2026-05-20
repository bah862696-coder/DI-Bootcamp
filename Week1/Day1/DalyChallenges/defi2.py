# Écrivez un programme qui demande une chaîne de caractères à l'utilisateur
# et affiche une nouvelle chaîne sans les lettres consécutives identiques.

user_word = input("Entrez une chaîne de caractères : ")

result = ""
for i, char in enumerate(user_word):
    if i == 0 or char != user_word[i - 1]:
        result += char

print(result)