from Card import Card
import random


class Deck():
    """Creates a full 54 cards deck Unsorted"""
    def __init__(self):
        self.deck = []
        self.deck.append(Card(0, "Clover", "Black"))
        self.deck.append(Card(0, "Hearts", "Red"))

        for i in range(1, 14):  # adds all the cards to the deck
            self.deck.append(Card(i, "Pickes", "Black"))
            self.deck.append(Card(i, "Clover", "Black"))
            self.deck.append(Card(i, "Hearts", "Red"))
            self.deck.append(Card(i, "Tiles", "Red"))

    def size(self):
        """returns how many cards are in the deck (deck's size)"""
        return len(self.deck)

    def get_card(self):
        """returns the card that is in the top of the deck without removing it"""
        if self.size() > 0:
            return self.deck[-1]

    def take_card(self):
        """returns and remove the card that in the top of the deck"""
        if self.size() > 0:
            temp_card = self.deck[-1]
            self.deck.pop(-1)
            return temp_card

    def add_card(self, card):
        """gets a card and adds it to the top of the deck"""
        self.deck.append(card)

    def shuffle(self):
        """shuffles randomly all the cards in the deck"""
        shuffle_times = 100  # the number of times all the cards switch random places
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
