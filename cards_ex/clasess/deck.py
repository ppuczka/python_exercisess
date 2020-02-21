from .card import Card
from random import shuffle

class Deck:

    def __init__(self):
        suits = ['Hearts','Diamonds','Clubs','Spades']
        values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        self.cards = [Card(suit, value) for suit in suits for value in values]
    
    def shuffle_deck(self):
        if len(self.cards) < 52:
            raise ValueError("Only full decks can be shuffled")
        shuffle(self.cards)
        return self
    
    def deal(self):
        if len(self.cards) == 0:
            raise ValueError("All cards have been dealt")
        return self.cards.pop()

    def __repr__(self):
        return (f"Cards remaining in deck: {len(self.cards)}")
    
    def __str__(self):
        return (str(len(self.cards)))