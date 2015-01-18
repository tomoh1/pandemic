import os
from PyQt4 import QtGui, QtCore

from models import cities
from models import city_data


class BoardView(QtGui.QGraphicsView):
    pass

BSSuper = QtGui.QGraphicsScene
class BoardScene(BSSuper):
    def __init__(self, *args, **kwargs):
        BSSuper.__init__(self, *args, **kwargs)
        self.spot_radius = 10
        pixmap = QtGui.QPixmap('views\\map.jpg')
        self.pixmap_item = self.addPixmap(pixmap)
        self.setSceneRect(self.pixmap_item.boundingRect())
        self.highlight_spot = self.newHighlight()

    def newHighlight(self):
        r = self.spot_radius
        pen = QtGui.QPen(QtCore.Qt.white)
        brush = QtGui.QBrush(QtCore.Qt.white)
        s = self.addEllipse(0, 0, 2*r, 2*r, pen, brush)
        s.setVisible(False)
        return s

    def highlightPos(self, x, y, spot=None):
        if spot is None:
            spot = self.highlight_spot
        r = self.spot_radius
        spot.setVisible(True)
        spot.setPos(x-r, y-r)

BSuper = QtGui.QWidget
class Board(BSuper):
    def __init__(self, *args, **kwargs):
        BSuper.__init__(self, *args, **kwargs)
        self.main_layout = QtGui.QHBoxLayout()
        self.setLayout(self.main_layout)
        self.view = BoardView()
        self.scene = BoardScene()
        self.view.setScene(self.scene)
        self.main_layout.addWidget(self.view)
        g = cities.CityGraph(city_data.CITY_LIST, city_data.CONNECTION_LIST)
        self.city_graph = g
        self.spot_list = []

    def highlightCity(self, city, spot=None):
        city = self.city_graph.getCity(city)
        self.scene.highlightPos(*city.pos, spot=spot)

    def highlightAll(self):
        self.clearHighlights()
        self.spot_list = []
        for city in self.city_graph.cities():
            s = self.scene.newHighlight()
            self.spot_list.append(s)
            self.highlightCity(city, s)

    def clearHighlights(self):
        for spot in self.spot_list:
            self.scene.removeItem(spot)
        self.spot_list = []
        self.scene.highlight_spot.setVisible(False)


