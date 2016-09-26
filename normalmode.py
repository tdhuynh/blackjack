
import sys
from random import shuffle

suits = ('Clubs', 'Spades', 'Diamonds', 'Hearts')
characters = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
values = {'A': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10, 'Q': 10, 'K': 10}


class Person:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def add_card_to_hand(self, card):
        self.hand.append(card)
        return self.hand

    def check_values(self):
        value = 0
        ace = False
        for card in self.hand:
            char = card[1]
            value += values[char]
            if char == 'A' and value < 12:
                value += 10
                ace = True
            else:
                if ace is True and value > 21:
                    value -= 10
                    ace = False
        return value

    def check_blackjack_or_bust(self):
        if 21 == self.check_values():
            print("Blackjack! {} wins!".format(self.name))
            sys.exit()
        elif 21 < self.check_values():
            print("Bust! {} loses!".format(self.name))
            sys.exit()

    def get_info(self):
        print(self.name)
        print(self.hand)
        print("Total Value: {}".format(self.check_values()))

    def partial_info(self):
        print(self.name)
        print(self.hand[0])

    def turn(self):
        self.add_card_to_hand(deck.deal_card())
        self.get_info()
        self.check_blackjack_or_bust()


class Deck:
    def __init__(self):
        self.cards = [(suit, char) for suit in suits for char in characters]

    def shuffle_deck(self):
        shuffle(self.cards)

    def deal_card(self):
        return self.cards.pop(0)


def check_win(player, dealer):
    if 21 >= player.check_values() > dealer.check_values():
        print("Player wins!")
        sys.exit()
    elif 21 >= dealer.check_values() > player.check_values():
        print("Dealer wins!")
        sys.exit()
    else:
        print("Dealer wins!")


player = Person("Player")
dealer = Person("Dealer")
deck = Deck()
deck.shuffle_deck()
for i in range(2):
    dealer.add_card_to_hand(deck.deal_card())
    player.add_card_to_hand(deck.deal_card())
player.get_info()
dealer.partial_info()
player.check_blackjack_or_bust()

while True:
    hit_or_stand = input("[H]it or [S]tand? ")
    if hit_or_stand.upper() == 'H':
        player.turn()
    else:
        dealer.get_info()
        dealer.check_blackjack_or_bust()
        while dealer.check_values() < 17:
            dealer.turn()
        check_win(player, dealer)
