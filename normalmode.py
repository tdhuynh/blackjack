# dealer shuffles
# deal 1 card at a time, total of two per player
# dealer's second card is hidden
# check for 21 after deal
# each time a hit happens, check for win

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
        for card in self.hand:
            char = card[1]
            value += values[char]
            if char == 'A' and value < 12:
                value += 10
            else:
                continue
        return value

    def check_blackjack_or_bust(self):
        if 21 == self.check_values():
            print("Blackjack! {} wins!".format(self.name))
        elif 21 < self.check_values():
            print("Bust! {} loses!".format(self.name))


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
    elif 21 >= dealer.check_values() > player.check_values():
        print("Dealer wins!")


# class Hand:
    # def get_score(self):
    #     value = 0
    #     for card in self.hand:
    #         value += card[1]
    #     return value


player = Person("Player")
dealer = Person("Dealer")
deck = Deck()
deck.shuffle_deck()
for i in range(2):
    dealer.add_card_to_hand(deck.deal_card())
    player.add_card_to_hand(deck.deal_card())
print(dealer.hand, player.hand)
player.check_blackjack_or_bust()
dealer.check_blackjack_or_bust()


while True:
    hit_or_stand = input("[H]it or [S]tand? ")
    if hit_or_stand.upper() == 'H':
        player.add_card_to_hand(deck.deal_card())
        print(player.hand)
        print(player.check_values())
        player.check_blackjack_or_bust()
    else:
        # check to see who wins
        while dealer.check_values() <= 16:
            dealer.add_card_to_hand(deck.deal_card())
            print(dealer.hand)
            print(dealer.check_values())
            dealer.check_blackjack_or_bust()

        check_win(player, dealer)
