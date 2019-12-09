import os
import time

from simon_game.sequence import Sequence
from simon_game.player import Player
from savings.saving import Saving

class Game():
    """General class to manage the game execution and the related objects.
    player : an instance of the player object
    sequence : an instance of a sequence object
    Classe générale pour gérer l'exécution du jeu et les objets associés.
     player: une instance de l'objet player
     séquence: une instance d'un objet séquence"""
    def __init__(self):
        self.player = Player()
        self.sequence = Sequence()
        self.saving = Saving()

    def initialize_player(self):
        """Function to ask for the player name and store it in the player object
            Fonction permettant de demander le nom du joueur et de le stocker dans l'objet joueur"""
        player_name = input('Quel est votre nom de joueur ? ')
        self.player.name = player_name
        self.saving.name = player_name
        print("OK {}, il ne nous reste plus qu'un dernier réglage".format(self.player.name))

    def initialize_difficulty(self):
        """Function to ask for the choosen difficulty and store it in the sequence object
            Fonction pour demander la difficulté choisie et la stocker dans l'objet séquence"""
        difficulty = ""
        while self.sequence.set_game_difficulty(difficulty.lower()) is False:
            difficulty = input('Quelle difficulté de jeux ? (Facile, Moyen ou Difficile)')
        self.saving.difficulty = self.sequence.difficulty
        print("Le jeux va démarrer dans quelques instants, préparez-vous à retenir le nombre présenté")

    def start_game(self):
        """Function to show the sequence of numbers while the player's guess is right
            Fonction permettant d'afficher la séquence de chiffres pendant que le joueur devine correctement"""
        while self.player.is_right:
            self.sequence.play()
            # We ask for a number for each number in the sequence
            for i in range(0, len(self.sequence.numbers)):
                nombre = self.ask_number()
                os.system("cls" if os.name == "nt" else "clear")
                # if the player fails the loops stops
                if nombre != self.sequence.numbers[i]:
                    print("Ce n'est pas le bon nombre malheureusement...")
                    self.saving.save()
                    self.play_again()
                    self.transition()
                    break;
            self.saving.score += 1

    def ask_number(self):
        """Function to ask for a number and check it is valid
            Fonction pour demander un numéro et vérifier qu'il est valide"""
        while True:
            try:
                nombre = int(input('nombre : '))
                break
            except:
                print("Ce n'est pas un nombre")
                continue
        return nombre

    def end_game(self):
        """Function to"""
        print('Fin du jeu !')

    def transition(self):
        """Function to make a break and clear the screen"""
        time.sleep(1)
        os.system("cls" if os.name =="nt" else "clear")

    def play_again(self):
        """Function to ask the player if he wants to play again"""
        answer = input('Voulez-vous rejouer ? o/n : ')
        if answer == 'o':
            # empty the sequence to start from the beginning
            self.sequence.numbers = []
            self.saving.score = 0
        else :
            # Will stop the while loop
            self.player.is_right = False
