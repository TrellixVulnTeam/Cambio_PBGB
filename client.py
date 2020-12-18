from network import *
from game import *
import time
import threading
from Hand import Hand

n = Network()
n.connect()
my_id = int(n.get_player())  # Player's ID

def send_action(data):
    n.send(data)
    time.sleep(0.05)

def data_deck_to_hand(card_index):
    """ player_ID, action, card_index """
    global my_id
    code = "deck_to_hand" + ',' + str(my_id) + ',' + str(card_index)
    return str(code)


def data_dump_to_hand(card_index):
    """ action, player_ID, card_index """
    global my_id
    code = "dump_to_hand" + ',' + str(my_id) + ',' + str(card_index)
    return str(code)

#game = n.send("deal")

while True:
    x = input("Enter: ")
    game = n.send(x)