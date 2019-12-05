from simon_game.game import Game

if __name__ == '__main__':
    # Start the object representing the game with a player object and a sequence of number
    game = Game()

    game.transition()
    print('Bienvenue sur ce jeux du Simon en version numérique')

    # Ask the player name and store it
    game.initialize_player()
    game.transition()

    # Ask to the player the choosen difficulty
    game.initialize_difficulty()
    game.transition()

    # Loop to display numbers to guess while the player is right
    game.start_game()
    game.end_game()
    game.transition()
