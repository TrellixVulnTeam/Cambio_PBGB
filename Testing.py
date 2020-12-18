import threading
import multiprocessing
import time
from Deck import Deck
from game import *

game = Game(0)
game.add_player()
game.add_player()
game.start_deal()

game.get_hand(1).print_hand()
game.get_hand(2).print_hand()

game.switch_cards(1, 0, 2, 2)
game.get_hand(1).print_hand()
game.get_hand(2).print_hand()

