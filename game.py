from Actions import Card, Deck, Hand
import Actions

deck = Deck()
hand = Hand()
hand2 = Hand()
deck.shuffle()

Actions.deck_to_hand(deck, hand)
Actions.deck_to_hand(deck, hand)
Actions.deck_to_hand(deck, hand)
Actions.deck_to_hand(deck, hand)
hand.print_hand()

Actions.hand_to_deck(hand, 0, deck)
hand.print_hand()