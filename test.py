from models import cities
from models import city_data


g = cities.CityGraph(city_data.CITY_LIST, city_data.CONNECTION_LIST)

print "Welcome"

