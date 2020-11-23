from Card import Card
from Deck import Deck
from Card import Card
import Actions

class Hand:
    def __init__(self):
        self.hand = []

    def size(self):
        """returns the size of the hand list *including null places*"""
        return len(self.hand)

    def cards_mum(self):
        """return the number of cards in the hand *without null places*"""
        count = 0       # counter for the cards
        for card in self.hand:
            if card is not None:
                count += 1
        return count

    def add_card(self, card):
        """adds a card to the hand #Not specific place#"""
        for i in range(self.size()):  # checks if there is an empty card spot in the list
            if self.hand[i] is None:
                self.hand[i] = card
                return True
        self.hand.append(card)

    def set_card(self, card, index):
        """adds a card to the hand to a specific index"""
        self.hand[index] = card

    def get_card(self, index):
        """returns the card that is in the top of the deck without removing it"""
        if self.size() > 0:
            return self.hand[index]

    def take_card(self, index):
        """returns and remove the card that in end of the"""
        if self.size() > 0:
            temp_card = self.hand[index]
            self.hand[index] = None
            return temp_card
        False

    def get_hand_sum(self):
        """returns the sum of all the numbers in the hand"""
        sum_nums = 0     # saves the sum of the card's numbers
        for card in self.hand:
            if card is not None:
                sum_nums += card.get_number()
        return sum_nums

    def print_hand(self):
        """prints the hand (with null slots)"""
        print("Hand:")
        for card in self.hand:
            if card is not None:
                card.print_card()
            else:
                print("None!")
        print("*********************")
