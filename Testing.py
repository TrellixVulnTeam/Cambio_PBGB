import threading
import multiprocessing
import time
from Deck import Deck


t = time.time()
deck1 = Deck(0)
deck2 = Deck()
processes = []
""""
if __name__ == '__main__':
    for i in range(20):
        p = multiprocessing.Process(target=deck1.shuffle, args=(10000,))
        p.start()
        processes.append(p)
"""
