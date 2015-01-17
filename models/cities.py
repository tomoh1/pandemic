import networkx as nx
from models import diseases


class City(object):
    def __init__(self, name, population, disease, x, y):
        self.name = name
        self.population = population
        self.native_disease = disease
        self.research_station = False
        self.cubes = {}
        self.protected = False
        self.city_pos = (x, y)


class CityGraph():
    def __init__(self, city_list, connection_list):
        self.name_dict = {}
        self.graph = nx.Graph()
        for name, population, color, x, y in city_list:
            disease = diseases.colormap[color]
            city = City(name, population, disease, x, y)
            self.name_dict[name] = city
            self.graph.add_node(city)

        for name1, name2 in connection_list:
            city1 = self.findCity(name1)
            city2 = self.findCity(name2)
            self.addConnection(city1, city2)

    def addCity(self, city):
        self.name_dict[city.name] = city
        if city in self.graph:
            raise RuntimeError('%s already in graph' % city.name)

    def addConnection(self, city1, city2):
        if self.graph.has_edge(city1, city2):
            raise RuntimeError('There is already a connection between %s and '
                               '%s' % (city1, city2)
        self.graph.add_edge(city1, city2, attr_dict)

    def findCity(self, name):
        city = self.name_dict.get(name)
        if city is None:
            raise RuntimeError('No city named %s.' % name)
        return city
