from Deck import Deck
from Hand import Hand

"""
This is a library with functions needed to control the card game
Creating a card (Tuple type) and every handling of cards between
hands or decks is done with those functions
"""


def deck_to_hand(deck, hand, num_of_cards=1):
    """gets a hand and a deck and take the top card from the deck and adds it to the hand many times as given"""
    for i in range(num_of_cards):
        if deck.size() > 0:
            hand.add_card(deck.take_card())


def deck_to_deck(from_deck, to_deck, num_of_cards=1):
    """gets two decks and take the top card from one deck and adds it to the other deck"""
    for i in range(num_of_cards):
        if from_deck.size() > 0:
            to_deck.add_card(from_deck.take_card())


def hand_to_deck(hand, card_index, deck, num_of_cards=1):
    """gets a deck and a hand and takes a card from the hand and adds it to the deck"""
    for i in range(num_of_cards):
        if hand.size() > 0:
            deck.add_card(hand.take_card(card_index))


def hand_to_hand(from_hand, card_index, to_hand):
    """gets to hand and take one card from one hand and adds it to the other"""
    if from_hand.size() > 0:
        to_hand.add_card(from_hand.take_card(card_index))


def switch_cards(hand1, card_index1, hand2, card_index2):
    """gets to hands and switch between two cards"""
    card1 = hand1.take_card(card_index1)
    card2 = hand2.take_card(card_index2)
    hand1.set_card(card2, card_index1)
    hand2.set_card(card1, card_index2)


def peek(hand, card_index):
    """peeks (looks) a card in hand"""
    return hand.get_card(card_index)


def stick(hand, card_index, deck):
    """sticks a card in hand to deck, returns true if stick succeed and false if failed"""
    if hand.get_card(card_index)[0] == deck.get_card()[0]:
        hand_to_deck(hand, card_index, deck)
        return True
    return False


# ---------------------------------------------------------------------------------------------------------------------------------------------- !Card!


def new_card(number, shape, color):
    """Creates a new Tuple that represents a card
    :returns - (Number, Shape, Color)
    """
    return number, shape, color


def get_number(card):
    """Returns the number value of the card [0]"""
    return card[0]


def get_shape(card):
    """Returns the shape value of the card [1]"""
    return card[1]


def get_color(card):
    """Returns the color value of the card [2]"""
    return card[2]


def is_same_number(card1, card2):
    """ Gets 2 cards and return true if they have the same number value or false if not """
    return card1[0] == card2[0]


def is_same_shape(card1, card2):
    """ Gets 2 cards and return true if they have the same shape value or false if not """
    return card1[1].__eq__(card2[1])


def is_same_color(card1, card2):
    """ Gets 2 cards and return true if they have the same color value or false if not """
    return card1[2].__eq__(card2[2])


def is_same_card(card1, card2):
    return is_same_number(card1, card2) and is_same_shape(card1, card2) and is_same_color(card1, card2)

