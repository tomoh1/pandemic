from random import shuffle

class GameCard(object):
    pass

class PlayerCard(GameCard):
    pass

class PlayerCityCard(PlayerCard):
    def __init__(self, city, population, color):
        self.city = city
        self.population = population
        self.color = color

class InfectionCard(GameCard):
    pass

class InfectionCityCard(InfectionCard):
    def __init__(self, city):
        self.city = city
    
class CardDeck(object):
    def __init__(self, card_type):
        self.cards = []
        self.card_type = card_type

    def addCardToTop(self, card):
        self.cards.append(card)
    
    def topCard(self):
        return self.cards[-1]
    
    def bottomCard(self):
        return self.cards[0]
    
    def shuffle(self):
        shuffle(self.cards)
        
    def addDeckToTop(self, deck):
        self.cards.extend(deck)