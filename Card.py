class Card:
    def __init__(self, number, shape, color):
        """creates a "card" object with num, shape and color"""
        self.number = number
        self.shape = shape
        self.color = color

    def get_number(self):
        return self.number

    def get_shape(self):
        return self.shape

    def get_color(self):
        return self.color

    def get_card_tup(self):
        """returns a tuple with the card's apects: number, shape, color"""
        return self.number, self.shape, self.color


    def print_card(self):
        """prints the card stats"""
        print(self.get_card_tup())

