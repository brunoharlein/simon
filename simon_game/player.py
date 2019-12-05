# coding: utf-8

class Player():
    """Class representing a player
    - name : a string for the name of the player
    - is_right : a boolean to know if the player guesses the right number, True by default"""
    def __init__(self, name = False):
        self.name = name
        self.is_right = True
