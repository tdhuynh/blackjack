# dealer shuffles
# deal 1 card at a time, total of two per player
# dealer's second card is hidden
# check for 21 after deal
# each time a hit happens, check for win

from random import choice
from random import shuffle

suits = ('Clubs', 'Spades', 'Diamonds', 'Hearts')
characters = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')


class Person:
    def __init__(self, name):
        self.name = name

# class Cards:
#     def __init__(self, suits, characters):
#         self.suits = choice(suits)
#         self.characters = choice(characters)
#
#     def get_card(self):
#         random_card = self.suits, self.characters
#         return random_card


class Deck:
    def __init__(self):
        self.cards = [(suit, character) for suit in suits for character in characters]

    def shuffle_deck(self):
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)


class Hand:
    def __init__(self):
        self.hand = []

    def add_card_to_hand(self, card):
        self.hand.append(card)
        return self.hand


player1 = Person("Player 1")
dealer = Person("Dealer")
deck = Deck()
player1_hand = Hand()
dealer_hand = Hand()

deck.shuffle_deck()

player1_hand.add_card_to_hand(deck.deal_card())
dealer_hand.add_card_to_hand(deck.deal_card())
player1_hand.add_card_to_hand(deck.deal_card())
dealer_hand.add_card_to_hand(deck.deal_card())

print(player1_hand.hand)
print(dealer_hand.hand)
