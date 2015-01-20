from models import cities
from models import city_data
from models import players
from models import cards
from models import game
from models import diseases

EPIDEMIC = 'Epidemic'
GOVERNMENT_GRANT = 'Government_Grant'
AIRLIFT = 'Airlift'
ONE_QUIET_NIGHT = 'One_Quiet_Night'
FORECAST = 'Forecast'
RESILIENT_POPULATION = 'Resilient_Population'

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

def infectCity(infection_deck, infection_discard_pile, num):
    card = infection_deck.takeTopCard()
    infection_discard_pile.addCardToTop(card)
    city = g.getCity(card)
    disease = city.native_disease
    city.infect(disease, num)

def setupBoard(infection_deck, infection_discard_pile):
    for num in [3, 2, 1]:
        for x in range(3):
            infectCity(infection_deck, infection_discard_pile, num)

def directFlight(player, city):
    card = player.directFlight(city)
    if card is not None:
        player_discard_pile.addCardToTop(card)
    else:
        print 'City card not in hand'

g = cities.CityGraph(city_data.CITY_LIST, city_data.CONNECTION_LIST)
player_deck = cards.CardDeck()
player_discard_pile = cards.CardDeck()
infection_deck = cards.CardDeck()
infection_discard_pile = cards.CardDeck()

EVENT_CARDS = [GOVERNMENT_GRANT, AIRLIFT, ONE_QUIET_NIGHT,
               FORECAST, RESILIENT_POPULATION]
HAND_SIZES = {2: 4, 3: 3, 4: 2}

player_list = [players.Player('Ellen'), players.Player('Tom')]
epidemics = 4

"""
print "Welcome to Pandemic. Will you be able to save humanity?"

num_players = int(raw_input("Enter number of players (up to 4 players): "))
num = 1
player_list = []

while num <= num_players:
    name = raw_input("Enter the name of Player " + str(num) + ": ")
    num += 1
    role = raw_input("Choose a role for your player (medic, scientist, "
                     "researcher, quarantine, operations, dispatcher): ")
    p = players.Player(name, role)
    player_list.append(p)

epidemics = int(raw_input("Choose your difficulty level (4,5, or 6): "))
"""
for city in g.cities():
    player_deck.addCardToTop(city.name)
    infection_deck.addCardToTop(city.name)
for card in EVENT_CARDS:
    player_deck.addCardToTop(card)

player_deck.shuffle()
infection_deck.shuffle()
distributeHand(player_list, player_deck)
setupPlayerDeck(player_deck, epidemics)

game_state = game.GameState(player_list)
g.getCity('Atlanta').research_station = True
setupBoard(infection_deck, infection_discard_pile)

p1 = player_list[0]
p2 = player_list[1]

p1.current_city = g.getCity('Atlanta')
p2.current_city = g.getCity('Atlanta')

