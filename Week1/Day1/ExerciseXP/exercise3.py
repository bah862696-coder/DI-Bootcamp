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
