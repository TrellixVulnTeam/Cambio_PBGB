class Card:
    """Creates a new Tuple that represents a card
     :returns - (Number, Shape, Color)
     """
    height = 107
    width = 54

    def __init__(self, number, shape, color, pos=(0, 0)):
        self.card = (number, shape, color)
        self.pos = pos

    def get_number(self):
        """Returns the number value of the card [0]"""
        return self.card[0]

    def get_shape(self):
        """Returns the shape value of the card [1]"""
        return self.card[1]

    def get_color(self):
        """Returns the color value of the card [2]"""
        return self.card[2]

    def get_pos(self):
        """Returns the location of the card as tuple (x, y)"""
        return self.pos

    def set_pos(self, pos):
        """Gets a new position and sets the card pos to this"""
        self.pos = pos

    def is_same_number(self, card2):
        """ Gets 2 cards and return true if they have the same number value or false if not """
        return self.card1[0] == card2[0].get_number()

    def is_same_shape(self, card2):
        """ Gets 2 cards and return true if they have the same shape value or false if not """
        return self.card1[1].__eq__(card2[1].get_shape())

    def is_same_color(self, card2):
        """ Gets 2 cards and return true if they have the same color value or false if not """
        return self.card1[2].__eq__(card2[2].get_color())

    def print_card(self):
        """Prints the card"""
        print(self.card)

    def is_card_location_pressedXXX(self, positions):
        """ Returns True if the location in inside the card """
        x1, y1 = self.pos[0] - 37, self.pos[1] - 53
        x2, y2 = positions[0], positions[1]
        if x1 <= x2 <= x1 + 75 and y1 <= y2 <= y1 + 107:
            return True
        return False

    def is_pressed(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        x2 = self.pos[0]
        y2 = self.pos[1]
        if x2 <= x1 <= x2 + self.width and y2 <= y1 <= y2 + self.height:
            return True
        else:
            return False

    def is_card_location_pressed(self, positions):
        """ Returns True if the location in inside the card """
        x1, y1 = self.pos[0], self.pos[1]
        x2, y2 = positions[0], positions[1]
        if x1 <= x2 <= x1 + 75 and y1 <= y2 <= y1 + 107:
            return True
        return False

    def __str__(self):
        text = str(self.card[0]) + " - " + self.card[1] + " - " + self.card[2]
        return text
