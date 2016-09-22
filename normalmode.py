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


suit = (['Clubs'], ['Spades'], ['Diamonds'], ['Hearts'])
character = (['A'], ['2'], ['3'], ['4'], ['5'], ['6'], ['7'], ['8'], ['9'], ['10'], ['J'], ['Q'], ['K'])

class Cards:

    def __init__(self, suit, character):
        self.suit = choice(suit)
        self.character = choice(character)

    def get_card(self):
        random_card = [self.suit, self.character]
        return random_card



card = Cards(choice(suit), choice(character))
print(card.get_card())


#
#
# class Deck:
#     def __init__(self):
#         pass
