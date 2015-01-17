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

    def __str__(self):
        return self.name

    def __repr__(self):
        return '<City> %s' % self.name


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
                               '%s' % (city1, city2))
        self.graph.add_edge(city1, city2, attr_dict)

    def getCity(self, city):
        """
        Return the city object, doing a lookup if necessary. If the name is
        invalid or a city object that is not part of this CityGraph is passed
        in, raise a RuntimeError.

        @param city: the city. If this is the city name, we do a lookup. If not
        we just return the same city.
        @type city: str or City

        @return: the city object
        @rtype: City
        """
        if isinstance(city, City):
            if self.graph.has_node(city):
                return city
            else:
                raise RuntimeError('City object %s is not in the graph.' % city)
        city = self.name_dict.get(name)
        if city is None:
            raise RuntimeError('No city named %s.' % name)
        return city

    def getNeighbors(self, city):
        city = self.getCity(city)
        return self.graph.neighbors(city)






