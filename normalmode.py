# dealer shuffles
# deal 1 card at a time, total of two per player
# dealer's second card is hidden
# check for 21 after deal
# each time a hit happens, check for win

from random import choice
from random import shuffle

class Person:
    def __init__(self):
        pass


suits = (['Clubs'], ['Spades'], ['Diamonds'], ['Hearts'])
characters = (['A'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9'], ['10'], ['J'], ['Q'], ['K'])

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


# card = Cards(choice(suits), choice(characters))
deck = Deck()
deck.shuffle_deck()
print(deck.cards)
