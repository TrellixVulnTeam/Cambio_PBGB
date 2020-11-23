from Deck import Deck
from Hand import Hand
from Card import Card


def deck_to_hand(deck, hand):
    """gets a hand and a deck and take the top card from the deck and adds it to the hand"""
    if deck.size() > 0:
        hand.add_card(deck.take_card())
        return True
    return False


def deck_to_deck(from_deck, to_deck):
    """gets two decks and take the top card from one deck and adds it to the other deck"""
    if from_deck.size() > 0:
        to_deck.add_card(from_deck.take_card())
        return True
    return False


def hand_to_deck(hand, hand_index, deck):
    """gets a deck and a hand and takes a card from the hand and adds it to the deck"""
    if hand.size() > 0:
        deck.add_card(hand.take_card(hand_index))
        return True
    return False


def hand_to_hand(from_hand, index, to_hand):
    """gets to hand and take one card from one hand and adds it to the other"""
    if from_hand.size() > 0:
        to_hand.add_card(from_hand.take_card(index))


def switch_cards(hand1, index1, hand2, index2):
    """gets to hands and switch between two cards"""
    card1 = hand1.take_card(index1)
    card2 = hand2.take_card(index2)
    hand1.set_card(card2, index1)
    hand2.set_card(card1, index2)


def peek(hand, index):
    """peeks (looks) a card in hand"""
    return hand.get_card(index)


def stick(hand, index, deck):
    """sticks a card in hand to deck, returns true if stick succeed and false if failed"""
    if hand.get_card(index).get_number() == deck.get_card().get_number():
        hand_to_deck(hand, index, deck)
        return True
    return False
