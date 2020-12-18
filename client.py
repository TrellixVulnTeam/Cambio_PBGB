from network import *
from game import *
import time
import threading
from Hand import Hand

n = Network()
n.connect()
my_id = int(n.get_player())  # Player's ID


def data_deck_to_hand(card_index):
    """ player_ID, action, card_index """
    global my_id
    code = "deck_to_hand" + ',' + str(my_id) + ',' + str(card_index) + ',' + '-1' + ',' + '-1'
    return code


def data_dump_to_hand(card_index):
    """ action, player_ID, card_index """
    global my_id
    code = "dump_to_hand" + ',' + str(my_id) + ',' + str(card_index) + ',' + '-1' + ',' + '-1'
    return code


def data_switch_cards(card1_index, hand2_id, card2_index):
    """ action, player_ID, card_index, player2_ID, card2_index """
    global my_id
    code = "switch_cards" + ',' + str(my_id) + ',' + str(card1_index) +',' + str(hand2_id) + ',' + str(card2_index)
    return code

game = n.send("deal")

while True:
    x = input("Enter: ")
    if x == "dump":
        game = n.send(data_dump_to_hand(0))
    elif x == "deck":
        game = n.send(data_deck_to_hand(0))
    elif x == "S":
        game = n.send(data_switch_cards(0, 2, 0))
    else:
        game = n.send(x)
