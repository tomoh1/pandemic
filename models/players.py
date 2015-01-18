


class Player(object):
    def __init__(self, name, City, CardDeck, role):
        self.name = name
        self.current_city = City
        self.hand = CardDeck
        self.role = role

