
class Player():
    """Class representing a player
    - name : a string for the name of the player
    - is_right : a boolean to know if the player guesses the right number, True by default

    - name: une chaîne de caractères pour le nom du joueur
    - is_right: un booléen pour savoir si le joueur devine le bon nombre, True par défaut """
    def __init__(self, name = False):
        self.name = name
        self.is_right = True
