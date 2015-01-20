


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
            self.current_city = city
            return card
        else:
            return None
