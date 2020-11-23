def new_card(number, shape, color):
    """Creates a new Tuple that represents a card
    :returns - (Number, Shape, Color)
    """
    return number, shape, color

def get_number(card):
    """Returns the number value of the card [0]"""
    return card[0]

def get_shape(card):
    """Returns the shape value of the card [1]"""
    return card[1]

def get_color(card):
    """Returns the color value of the card [2]"""
    return card[2]