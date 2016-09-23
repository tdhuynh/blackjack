# dealer shuffles
# deal 1 card at a time, total of two per player
# dealer's second card is hidden
# check for 21 after deal
# each time a hit happens, check for win

from random import choice
from random import shuffle

suits = ('Clubs', 'Spades', 'Diamonds', 'Hearts')
characters = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
scores = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}

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

    def get_score(self):

player1 = Person("Player 1")
dealer = Person("Dealer")

deck = Deck()
player_hand = Hand()
dealer_hand = Hand()
deck.shuffle_deck()


print(deck.cards)

for i in range(2):
    dealer_hand.add_card_to_hand(deck.deal_card())
    player_hand.add_card_to_hand(deck.deal_card())

print(dealer_hand.hand, player_hand.hand)

# check for win here

while True:
    hit_or_stand = input("[H]it or [S]tand? ")
    if hit_or_stand.upper() == 'H':
        player_hand.add_card_to_hand(deck.deal_card())
        print(player_hand.hand)
        # if value > 21:
        #     bust
    else:
        # check to see who wins
        if dealer.value <= 16:
            dealer_hand.add_card_to_hand(deck.deal_card())
        # else:
            # check for bust or win
