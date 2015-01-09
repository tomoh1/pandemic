import networkx as nx
from models import diseases


class City(object):
    def __init__(self, name, population, disease):
        self.name = name
        self.population = population
        self.native_disease = disease
        self.research_station = False
        self.cubes = {}
        self.protected = False
