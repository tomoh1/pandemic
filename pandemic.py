
from views import gameboard

from PyQt4 import QtGui


MWSuper = QtGui.QWidget
class MainWidget(MWSuper):
    def __init__(self, *args, **kwargs):
        MWSuper.__init__(self, *args, **kwargs)
        layout = QtGui.QVBoxLayout()
        self.setLayout(layout)
        self.board = gameboard.Board()
        layout.addWidget(self.board)
        self.city_le = QtGui.QLineEdit()
        self.city_le.editingFinished.connect(self.cityPicked)
        layout.addWidget(self.city_le)

    def cityPicked(self):
        text = self.city_le.text()
        if text == 'all':
            self.board.highlightAll()
        elif text == 'clear':
            self.board.clearHighlights()
        else:
            try:
                self.board.highlightCity(text)
            except RuntimeError:
                pass

def main():
    app = QtGui.QApplication([])
    main_widget = MainWidget()
    main_widget.showMaximized()
    app.exec_()

if __name__ == '__main__':
    main()
