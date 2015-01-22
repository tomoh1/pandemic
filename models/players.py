from models import cities
from models import diseases

class Player(object):
    def __init__(self, name):
        self.name = name
        self.current_city = None
        self.hand = []

    def treat(self, disease):
        self.current_city.cubes[disease] -= 1
        disease.returnCubes(1)

    def directFlight(self, city):
        if city.name in self.hand:
            index = self.hand.index(city.name)
            card = self.hand.pop(index)
            self.setCity(city)
            return card

    def charterFlight(self, city):
        current_city = self.current_city.name
        if current_city in self.hand:
            index = self.hand.index(current_city)
            card = self.hand.pop(index)
            self.setCity(city)
            return card

    def shuttleFlight(self, city):
        if city.research_station and self.current_city.research_station:
            self.setCity(city)

    def buildStation(self):
        current_city = self.current_city.name
        if (not self.current_city.research_station
            and self.current_city.name in self.hand):
            self.current_city.research_station = True
            index = self.hand.index(current_city)
            card = self.hand.pop(index)
            return card

    def setCity(self, city):
        self.current_city = city

    def discoverCure(self, disease, cards):
        for card in cards:
            if card not in self.hand:
                return
        for card in cards:
            self.hand.remove(card)
        disease.cure()
        return cards

    def giveKnowledge(self, card):
        self.hand.remove(card)

    def takeKnowledge(self, card):
        self.hand.append(card)