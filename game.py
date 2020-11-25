from Actions import Deck, Hand
import Actions

deck = Deck()
deck.shuffle()

hand1 = Hand()
hand2 = Hand()
hand3 = Hand()
hand4 = Hand()
Actions.deck_to_hand(deck, hand1, 2)
Actions.deck_to_hand(deck, hand2, 2)
hand1.print_hand()
hand2.print_hand()
Actions.switch_cards(hand1, 0, hand2, 0)
hand1.print_hand()
hand2.print_hand()

