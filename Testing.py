import threading
import multiprocessing
import time
from Deck import Deck
from game import *

game = Game(0)
game.add_player()

hand = game.get_hand(1)
game.deck_to_hand(1, 4)
hand.print_hand()
game.deck_to_hand(1, 1, 1)
hand.print_hand()