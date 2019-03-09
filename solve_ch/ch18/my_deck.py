import random

class Card:
    """
    Represents a standart playing card
    """
    
    def __init__(self, suit=0, rank=2):
        self.suit = suit
        self.rank = rank
    
    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10',
                 'Jack', 'Queen', 'King']
    
    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])
    
    def __lt__(self, other):
        card1 = self.suit, self.rank
        card2 = other.suit, other.rank
        return card1 < card2


# Funcion de prueba
def less_or_greather(card1, card2):
    if card1 < card2:
        print(card1, end=' ')
        print("is less than", end=' ')
        print(card2)
    else:
        print(card1, end=' ')
        print("is greather than", end=' ')
        print(card2)


class Deck:
    """
    Represents a deck of cards
    """
    
    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank)
                self.cards.append(card)
    
    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)
    
    def pop_card(self):
        return self.cards.pop()
    
    def add_card(self, card):
        return self.cards.append(card)
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def sort(self):
        return self.cards.sort()


class Hand(Deck):
    """
    Represents a hand of playing cards.
    """
    
    def __init__(self, label=''):
        self.cards = []
        self.label = label

"""
if __name__ == '__main__':
    #card1 = Card(1, 12)
    #print(card1)
    #card2 = Card(1, 13)
    #print(card2)
    
    #less_or_greather(card1, card2)
    deck = Deck()
    #deck.shuffle()
    #print(deck)
    #deck.sort()
    #print()
    #print(deck)
    
    hand = Hand('new hand')
    hand.cards
    hand.label
"""