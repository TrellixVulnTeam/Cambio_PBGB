from Card import Card
import random


class Deck():
    """Creates a full 54 cards deck Unsorted"""
    def __init__(self, status=1):
        if status == 1:
            self.deck = []
            self.deck.append(Card(0, "Clover", "Black"))
            self.deck.append(Card(0, "Hearts", "Red"))

            for i in range(1, 14):  # adds all the cards to the deck
                self.deck.append(Card(i, "Pikes", "Black"))
                self.deck.append(Card(i, "Clover", "Black"))
                self.deck.append(Card(i, "Hearts", "Red"))
                self.deck.append(Card(i, "Tiles", "Red"))
        elif status == 0:
            self.deck = []

    def size(self):
        """returns how many cards are in the deck (deck's size)"""
        return len(self.deck)

    def get_card(self, index=-1):
        """returns the card that is in the top of the deck without removing it"""
        return self.deck[index]

    def take_card(self):
        """returns and remove the card that in the top of the deck"""
        if self.size() > 0:
            return self.deck.pop(-1)

    def add_card(self, card):
        """gets a card (tuple) and adds it to the top of the deck"""
        self.deck.append(card)

    def shuffle(self, shuffle_times=25):
        """shuffles randomly all the cards in the deck, shuffle_times
         is the number of times all the cards switch random places"""
        for j in range(shuffle_times):
            for i in range(len(self.deck)):
                temp_card = self.deck.pop(i)
                random_num = random.randint(0, len(self.deck))
                self.deck.insert(random_num, temp_card)

    def empty_deck(self):
        """empties the deck"""
        self.deck.clear()

    def print_deck(self):
        """prints all the cards in the deck by order"""
        for card in self.deck:
            card.print_card()

    def sort_deck_by_num(self):
        """Sorts the cards in the deck by numbers values"""
        self.deck = sorted(self.deck, key=lambda x: x[0])

    def sort_deck_by_shape(self):
        """Sorts the cards in the deck by shape values"""
        self.deck = sorted(self.deck, key=lambda x: x[1])

    def sort_deck_by_color(self):
        """Sorts the cards in the deck by color values"""
        self.deck = sorted(self.deck, key=lambda x: x[2])
