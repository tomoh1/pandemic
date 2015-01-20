from random import shuffle

class GameCard(object):
    pass

class PlayerCard(GameCard):
    pass

class PlayerCityCard(PlayerCard):
    def __init__(self, city):
        self.city = city

class InfectionCard(GameCard):
    pass

class InfectionCityCard(InfectionCard):
    def __init__(self, city):
        self.city = city

class CardDeck(object):
    def __init__(self):
        self.cards = []

    def addCardToTop(self, card):
        self.cards.append(card)

    def takeTopCard(self):
        return self.cards.pop()

    def takeBottomCard(self):
        return self.cards.pop(0)

    def shuffle(self):
        shuffle(self.cards)

    def addDeckToTop(self, deck):
        self.cards.extend(deck.cards)

    def count(self):
        return len(self.cards)


class PlayerDeck(CardDeck):
    pass

class PlayerHand(CardDeck):
    pass