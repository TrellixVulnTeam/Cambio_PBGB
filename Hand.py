import Actions


class Hand:
    def __init__(self, user_name="user"):
        self.user_name = user_name
        self.hand = []
        self.locations = []

    def size(self):
        """ Returns the size of the hand list *including null places*"""
        return len(self.hand)

    def get_user_name(self):
        return self.user_name

    def cards_mum(self):
        """ Return the number of cards in the hand *without null places*"""
        count = 0  # counter for the cards
        for card in self.hand:
            if card is not None:
                count += 1
        return count

    def add_card(self, card, card_index=-1):
        """ Adds a card (Tuple) to the hand #to first null spot or to the end or to given location#"""
        if card_index == -1:
            for i in range(self.size()):  # checks if there is an empty card spot in the list - if yes than put card there
                if self.hand[i] is None:
                    self.hand[i] = card
                    #self.locations[i] = self.new_location()
                    return True
        else:
            self.hand[card_index] = card
            return True

        self.hand.append(card)
        return False

    def new_location(self):
        """ Returns a tuple of location for the new card """
        pass

    def get_location(self, card_index):
        """ Gets an index for a card in the hand and returns it's location as a tuple """
        return self.locations[card_index]

    def get_deck_locations(self):
        """ Returns a list with all the card's locations """
        return self.locations

    def set_location(self, card_index, location):
        """ Gets a card index and a location and sets the location in the card """
        self.locations[card_index] = location

    def set_card(self, card, index):
        """ Replaces a card (Tuple in the hand in a specific index"""
        self.hand[index] = card

    def get_card(self, index):
        """ Returns the card (Tuple) that is in the top of the deck without removing it"""
        if self.size() > 0:
            return self.hand[index]

    def take_card(self, index):
        """ Returns and remove the card that in end of the"""
        if self.size() >= index:
            temp_card = self.hand[index]
            self.hand[index] = None
            #self.locations[index] = None
            return temp_card

    def get_hand_sum(self):
        """ Returns the sum of all the numbers in the hand"""
        sum_nums = 0  # saves the sum of the card's numbers
        for card in self.hand:
            if card is not None:
                sum_nums += Actions.get_number(card)
        return sum_nums

    def print_hand(self):
        """ Prints the hand (with null slots)"""
        print("Hand:")
        for card in self.hand:
            if card is not None:
                card.print_card()
            else:
                print("None!")

    # Extra functions, no need for Cambio game

    def sort_hand_by_num(self):
        """Sorts the cards in the hand by numbers values"""
        self.hand = sorted(self.hand, key=lambda x: x[0])

    def sort_hand_by_shape(self):
        """Sorts the cards in the hand by shape values"""
        self.hand = sorted(self.hand, key=lambda x: x[1])

    def sort_hand_by_color(self):
        """Sorts the cards in the hand by color values"""
        self.hand = sorted(self.hand, key=lambda x: x[2])

    def del_nones(self):
        """Deletes all the 'Nones' in the hand"""
        self.hand = filter(lambda a: a is not None, self.hand)
