from final.Cambio_pack.Deck import Deck
from final.Cambio_pack.Hand import Hand

"""
The Class that contains all the information of the current game in the server
such as: games_ID, decks, players hands, cards and more
"""


class Game:
    def __init__(self, id):
        self.id = id  # The ID of the current game
        self.ready = False  # If the game has started or still waiting for players
        self.turn = 1  # Which player's turn it is
        self.waiting = True  # Are we waiting for a player to do something
        self.players = {}  # The list/dict of the players in current game
        self.game_deck = Deck(1)  # The game Deck
        self.game_deck.shuffle()
        self.dump_deck = Deck(0)  # The empty deck players dump cards in

    def add_player(self, player_id):
        """ Gets a new player's hand class and adds it to the players list """
        self.players[player_id] = Hand(player_id)

    """ Deals every player 4 cards """

    def start_deal(self):
        self.turn = list(self.players.keys())[0]
        for i in range(4):
            for player_id, hand in self.players.items():
                hand.add_card(self.game_deck.take_card())

    def remove_player(self, player_id):
        """ Get's a player index and remove it from the game """
        self.players.pop(player_id)

    def get_player(self, player_index):
        return self.players[player_index]

    def get_turn(self):
        """" Returns whos which player's turn it is """
        return self.turn

    def get_game_deck(self):
        """ Returns the game's deck """
        return self.game_deck

    def get_dump_deck(self):
        """ Returns the dump deck """
        return self.dump_deck

    def get_hand(self, player_id):
        return self.players[player_id]

    def get_id(self):
        return self.id

    def players_num(self):
        return len(self.players)

    def next_turn(self):
        active_players = list(self.players.keys())
        self.turn += 1

        if self.turn not in self.players.keys():
            self.turn += 1

        if self.turn > active_players[-1]:
            self.turn = active_players[0]

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
        #self.deck_to_dump(1)

    """
    This is a library with functions needed to control the card game
    Creating a card (Tuple type) and every handling of cards between
    hands or decks is done with those functions
    """

    def deck_to_hand(self, player_id, num_of_cards, card_index=-1):
        """ takes a card from deck and replace with a card in the hand (card from hand goes to dump)"""
        hand = self.players[player_id]
        if card_index == -1:
            for i in range(num_of_cards):
                if self.game_deck.size() >= num_of_cards:
                    hand.add_card(self.game_deck.take_card())

        else:
            temp_card = self.game_deck.take_card()
            self.hand_to_dump(player_id, card_index)
            hand.add_card(temp_card, card_index)

    def deck_to_dump(self, num_of_cards=1):
        """gets two decks and take the top card from one deck and adds it to the other deck"""
        for i in range(num_of_cards):
            if self.game_deck.size() > 0:
                self.dump_deck.add_card(self.game_deck.take_card())

    def hand_to_dump(self, player_id, card_index):
        """takes a card from the hand and adds it to the dump"""
        if self.players[player_id].size() > 0:
            self.dump_deck.add_card(self.players[player_id].take_card(card_index))

    def dump_switch(self, player_id, card_index):
        """ switch a card from the hand with the top card in the dump """
        if self.dump_deck.size() > 0:
            temp_card = self.dump_deck.take_card()
            self.hand_to_dump(player_id, card_index)
            self.players[player_id ].add_card(temp_card, card_index)

    def hand_to_hand(self, from_player_id, card_index, to_player_id):
        """gets to hand and take one card from one hand and adds it to the other"""
        if self.players[from_player_id].size() > 0:
            self.players[to_player_id].add_card(self.players[from_player_id].take_card(card_index))

    def switch_cards(self, player1_id, card1_index, player2_id, card2_index):
        """ Switch between 2 cards in 2 hands """
        hand1 = self.players[player1_id]
        hand2 = self.players[player2_id]
        temp_card1 = hand1.take_card(card1_index)
        temp_card2 = hand2.take_card(card2_index)
        hand1.add_card(temp_card2, card1_index)
        hand2.add_card(temp_card1, card2_index)


    def peek(self, player_id, card_index):
        """peeks (looks) a card in hand"""
        return self.players[player_id].get_card(card_index)

    def stick(self, player_id, card_index):
        """sticks a card in hand to deck, returns true if stick succeed and false if failed"""
        if (self.players[player_id ].get_card(card_index)[0]).is_same_number(self.dump_deck.get_card()[0]):
            self.hand_to_dump(player_id, card_index)
            return True
        return False

    # ---------------------------------------------------------------------------------------------------------------------------------------------- !Card!

    def new_card(self, number, shape, color):
        """Creates a new Tuple that represents a card
        :returns - (Number, Shape, Color)
        """
        return number, shape, color

    def get_number(self, card):
        """Returns the number value of the card [0]"""
        return card[0]

    def get_shape(self, card):
        """Returns the shape value of the card [1]"""
        return card[1]

    def get_color(self, card):
        """Returns the color value of the card [2]"""
        return card[2]

    def is_same_number(self, card1, card2):
        """ Gets 2 cards and return true if they have the same number value or false if not """
        return card1[0] == card2[0]

    def is_same_shape(self, card1, card2):
        """ Gets 2 cards and return true if they have the same shape value or false if not """
        return card1[1].__eq__(card2[1])

    def is_same_color(self, card1, card2):
        """ Gets 2 cards and return true if they have the same color value or false if not """
        return card1[2].__eq__(card2[2])

    def is_same_card(self, card1, card2):
        return self.is_same_number(card1, card2) and self.is_same_shape(card1, card2) and self.is_same_color(card1,
                                                                                                             card2)
