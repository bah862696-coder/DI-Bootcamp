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
        #
        #
        #from game import Game
def get_user_menu_choice():
    print("\n=== MENU ===")
    print("(g) Jouer")
    print("(s) Voir les scores")
    print("(q) Quitter")
    choice = input("Votre choix : ").lower()
    while choice not in ["g", "s", "q"]:
        print("Choix invalide.")
        choice = input("Votre choix : ").lower()
    return choice
def print_results(results):
    print("\n===== SCORES =====")
    print(f"Victoires : {results['win']}")
    print(f"Défaites : {results['loss']}")
    print(f"Matchs nuls : {results['draw']}")
    print("\nMerci d'avoir joué ")
def main():
    results = {
        "win": 0,
        "loss": 0,
        "draw": 0
    }
    while True:
        user_choice = get_user_menu_choice()
        if user_choice == "g":
            game = Game()
            result = game.play()
            results[result] += 1
        elif user_choice == "s":
            print_results(results)
        elif user_choice == "q":
            print_results(results)
            break
main()