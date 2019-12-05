import os
import time

from simon_game.sequence import Sequence
from simon_game.player import Player
from savings.saving import Saving

class Game():
    """General class to manage the game execution and the related objects.
    player : an instance of the player object
    sequence : an instance of a sequence object"""
    def __init__(self):
        self.player = Player()
        self.sequence = Sequence()
        self.saving = Saving()

    def initialize_player(self):
        """Function to ask for the player name and store it in the player object"""
        player_name = input('Quel est votre nom de joueur ? ')
        self.player.name = player_name
        self.saving.name = player_name
        print("OK {}, il ne nous reste plus qu'un dernier réglage".format(self.player.name))

    def initialize_difficulty(self):
        """Function to ask for the choosen difficulty and store it in the sequence object"""
        difficulty = ''
        while self.sequence.set_game_difficulty(difficulty.lower()) is False:
            difficulty = input('Quelle difficulté de jeux ? (Facile, Moyen ou Difficile)')
        self.saving.difficulty = self.sequence.difficulty
        print("Le jeux va démarrer dans quelques instants, préparez-vous à retenir le nombre présenté")

    def start_game(self):
        """Function to show the sequence of numbers while the player's guess is right"""
        while self.player.is_right:
            self.sequence.play()
            # We ask for a number for each number in the sequence
            for i in range(0, len(self.sequence.numbers)):
                nombre = self.ask_number()
                os.system('clear')
                # if the player fails the loops stops
                if nombre != self.sequence.numbers[i]:
                    print("Ce n'est pas le bon nombre malheureusement...")
                    self.saving.save()
                    self.play_again()
                    self.transition()
                    break;
            self.saving.score += 1

    def ask_number(self):
        """Function to ask for a number and check it is valid"""
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
        time.sleep(3)
        os.system('clear')

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
