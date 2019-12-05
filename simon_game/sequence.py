import os
import time
import random

class Sequence():
    """Class to represent the random sequence of numbers generated by the computer
    - difficulty_levels : a list of the available levels of difficulty
    - numbers_ranges : a list of the available ranges between 0 and n in which the random numbers are goin to be generated
    - numbers : a list with the sequence of random numbers
    - difficulty : an intenger between 1 and 3 representing the seconds between two numbers, by default 3(easy)
    - numbers_range : an integer for the range in which the random numbers are goin to be generated """
    def __init__(self):
        self.difficulty_levels = ['difficile', 'moyen', 'facile']
        self.numbers_ranges = [100, 20, 10]
        self.numbers = []
        self.difficulty = 3
        self.numbers_range = 10

    def show_sequence(self):
        """Function to print to the screen all numbers in the sequence at a certain interval based on choosen difficulty"""
        for number in self.numbers:
            print('   ', end="\r")
            print(number, end="\r")
            time.sleep(self.difficulty)

    def add_number(self):
        """Function to add a random number in the sequence"""
        number = random.randint(1,self.numbers_range)
        self.numbers.append(number)

    def play(self):
        """Function to print the whole sequence after a random number has been added"""
        self.add_number()
        self.show_sequence()

    def set_game_difficulty(self, level):
        """Function set the difficulty based on it's index in the list and the number range"""
        try:
            self.difficulty = self.difficulty_levels.index(level) + 1
            self.numbers_range = self.numbers_ranges[self.difficulty - 1]
        except:
            return False
