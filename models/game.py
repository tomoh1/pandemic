import players
import cities
import city_data
import cards
import diseases

EPIDEMIC = 'Epidemic'
GOVERNMENT_GRANT = 'Government_Grant'
AIRLIFT = 'Airlift'
ONE_QUIET_NIGHT = 'One_Quiet_Night'
FORECAST = 'Forecast'
RESILIENT_POPULATION = 'Resilient_Population'
EVENT_CARDS = [GOVERNMENT_GRANT, AIRLIFT, ONE_QUIET_NIGHT,
               FORECAST, RESILIENT_POPULATION]
HAND_SIZES = {2: 4, 3: 3, 4: 2}

def distributeHand(player_list, player_deck):
    num_players = len(player_list)
    for player in player_list:
        for n in range(HAND_SIZES[num_players]):
            card = player_deck.takeTopCard()
            player.hand.append(card)

def setupPlayerDeck(player_deck, epidemics):
    temp_deck_size = int(player_deck.count()/epidemics)
    temp_deck = cards.CardDeck()
    new_player_deck = cards.CardDeck()
    for i in range(epidemics-1):
        for j in range(temp_deck_size):
            card = player_deck.takeTopCard()
            temp_deck.addCardToTop(card)
        temp_deck.addCardToTop(EPIDEMIC)
        temp_deck.shuffle()
        new_player_deck.addDeckToTop(temp_deck)
    player_deck.addCardToTop(EPIDEMIC)
    player_deck.shuffle()
    player_deck.addDeckToTop(new_player_deck)

def infectCity(infection_deck, infection_discard_pile, graph, num):
    card = infection_deck.takeTopCard()
    infection_discard_pile.addCardToTop(card)
    city = graph.getCity(card)
    disease = city.native_disease
    city.infect(disease, num)

class GameState(object):
    def __init__(self):
        self.player_list = [players.Player('p1'), players.Player('p2')]
        self.player1 = self.player_list[0]
        self.player2 = self.player_list[1]
        self.current_player = 0
        self.turn = 0
        self.outbreaks = 0
        self.infection_pos = 0
        self.infection_schedule = [2, 2, 2, 3, 3, 4, 4]
        g = cities.CityGraph(city_data.CITY_LIST, city_data.CONNECTION_LIST)
        self.city_graph = g
        self.player_deck = cards.CardDeck()
        self.player_discard_pile = cards.CardDeck()
        self.infection_deck = cards.CardDeck()
        self.infection_discard_pile = cards.CardDeck()
        self.epidemics = 4
        self.setup()

    def clear(self):
        pass
    
    def setup(self):
        for city in self.city_graph.cities():
            self.player_deck.addCardToTop(city.name)
            self.infection_deck.addCardToTop(city.name)
        for card in EVENT_CARDS:
            self.player_deck.addCardToTop(card)
        self.player_deck.shuffle()
        self.infection_deck.shuffle()
        distributeHand(self.player_list, self.player_deck)
        setupPlayerDeck(self.player_deck, self.epidemics)
        self.city_graph.getCity('Atlanta').research_station = True
        self.player1.current_city = self.city_graph.getCity('Atlanta')
        self.player2.current_city = self.city_graph.getCity('Atlanta')
        for num in [3, 2, 1]:
            for x in range(3):
                infectCity(self.infection_deck, self.infection_discard_pile, 
                           self.city_graph, num)

    def driveToCity(self, destination):
        neighbors = self.city_graph.getNeighbors(self.player1.current_city)
        next_city = self.city_graph.getCity(destination)
        if next_city not in neighbors:
            return RuntimeError
        self.player1.current_city = next_city

    def driveToCity2(self, destination):
        neighbors = self.city_graph.getNeighbors(self.player2.current_city)
        next_city = self.city_graph.getCity(destination)
        if next_city not in neighbors:
            return RuntimeError
        self.player2.current_city = next_city
