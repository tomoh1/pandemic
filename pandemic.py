
from views import gameboard

from PyQt4 import QtGui

from models import cities
from models import city_data
from models import players
from models import cards
from models import game
from models import diseases

MWSuper = QtGui.QWidget
class MainWidget(MWSuper):
    def __init__(self, graph):
        MWSuper.__init__(self)
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)
        self.board = gameboard.Board(graph)
        layout.addWidget(self.board)
        self.city1_le = QtGui.QLineEdit()
        self.city1_le.editingFinished.connect(self.cityPicked1)
        self.city2_le = QtGui.QLineEdit()
        self.city2_le.editingFinished.connect(self.cityPicked2)
        self.output_lbl1 = QtGui.QLabel('Player 1')
        self.output_lbl2 = QtGui.QLabel('Player 2')
        layout.addWidget(self.output_lbl1)
        layout.addWidget(self.city1_le)
        layout.addWidget(self.output_lbl2)
        layout.addWidget(self.city2_le)

    def cityPicked1(self):
        text = self.city1_le.text()
        if text == 'all':
            self.board.highlightAll()
        elif text == 'clear':
            self.board.clearHighlights()
        elif text == 'p1':
            try:
                self.board.highlightCity(game_state.player1.current_city)
            except RuntimeError:
                return
        else:
            try:
                game_state.driveToCity(text)
                self.board.highlightCity(game_state.player1.current_city)
            except RuntimeError:
                return
        self.city1_le.setText('')

    def cityPicked2(self):
        text = self.city2_le.text()
        if text == 'all':
            self.board.highlightAll()
        elif text == 'clear':
            self.board.clearHighlights()
        else:
            try:
                game_state.driveToCity2(text)
                self.board.highlightCity(game_state.player2.current_city)
            except RuntimeError:
                return
        self.city2_le.setText('')
        
app = QtGui.QApplication([])
game_state = game.GameState()
main_widget = MainWidget(game_state.city_graph)
main_widget.showMaximized()
#app.exec_()
