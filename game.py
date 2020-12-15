from Deck import Deck
from Hand import Hand
import Actions

"""
The Class that contains all the information of the current game in the server
such as: games_ID, decks, players hands, cards and more
"""

class Game:
    def __init__(self, id):
        self.id = id  # The ID of the current game
        self.players_num = 0  # Number of players connected to current game
        self.ready = False  # If the game has started or still waiting for players
        self.turn = 0  # Which player's turn it is
        self.waiting = True  # Are we waiting for a player to do something
        self.players = []  # The list of the players in current game
        self.game_deck = Deck(1)  # The game Deck
        self.game_deck.shuffle()
        self.dump_deck = Deck(0)  # The empty deck players dump cards in

    def add_player(self):
        """ Gets a new player's hand class and adds it to the players list """
        self.players.append(Hand())

    def remove_player(self, player_index):
        """ Get's a player index and remove it from the game """
        self.players[player_index] = None

    def get_turn(self):
        """" Returns whos which player's turn it is """
        return self.turn

    def get_game_deck(self):
        """ Returns the game's deck """
        return self.game_deck

    def get_dump_deck(self):
        """ Returns the dump deck """
        return self.dump_deck

    def next_turn(self):
        """ Called when player finished turn and updates the next player's turn """
        #if self.turn == len(self.players):
        self.turn == 0
        #else:
        self.turn += 1

    def play(self, player_id, data):
        """ Updates the game status
        get: (player index, type of move, game_Deck, dump_deck, Card1 / hand1, Deck)
        """
        self.next_turn()

    def reset(self):
        self.id = id  # The ID of the current game
        self.players_num = 0  # Number of players connected to current game
        self.ready = False  # If the game has started or still waiting for players
        self.turn = 0  # Which player's turn it is
        self.waiting = True  # Are we waiting for a player to do something
        self.players = []  # The list of the players in current game
        self.game_deck = Deck(1)  # The game Deck
        self.game_deck.shuffle()
        self.dump_deck = Deck(0)  # The empty deck players dump cards in
