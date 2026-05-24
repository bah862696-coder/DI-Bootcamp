import random
class Game:
    def get_user_item(self):
        while True:
            user_choice = input(
                "Choisissez pierre, feuille ou ciseaux : "
            ).lower()
            if user_choice in ["pierre", "feuille", "ciseaux"]:
                return user_choice
            print("Choix invalide. Réessayez.")
    def get_computer_item(self):
        items = ["pierre", "feuille", "ciseaux"]
        return random.choice(items)
    def get_game_result(self, user_item, computer_item):
        if user_item == computer_item:
            return "draw"
        elif (
            (user_item == "pierre" and computer_item == "ciseaux")
            or
            (user_item == "feuille" and computer_item == "pierre")
            or
            (user_item == "ciseaux" and computer_item == "feuille")
        ):
            return "win"
        else:
            return "loss"
    def play(self):
        user_item = self.get_user_item()
        computer_item = self.get_computer_item()
        result = self.get_game_result(
            user_item,
            computer_item
        )
        print(f"\nVous avez choisi : {user_item}")
        print(f"L'ordinateur a choisi : {computer_item}")
        if result == "win":
            print(" Vous avez gagné !")
        elif result == "loss":
            print(" Vous avez perdu !")
        else:
            print(" Match nul !")
        return result