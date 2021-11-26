#cd IdeaProjects\MLBManager\display\ui
#pyuic6 -o MainWindow.py MainWindow.ui

import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog, QStackedWidget
from PyQt6.uic import loadUi
from src import saveoperations as so
from src.main import simulateSeason

class MainWindow(QDialog):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(r'C:\Users\Robert\IdeaProjects\MLBManager\display\ui\MainWindow.ui', self)
        self.league = so.startup()
        self.pushButton.clicked.connect(self.simulateSeason)

    def simulateSeason(self):

        screen = StandingsWindow(self.league)
        widget.addWidget(screen)
        widget.setCurrentIndex(widget.currentIndex()+1)


class StandingsWindow(QDialog):

    def __init__(self, league):
        self.league = league
        super(StandingsWindow, self).__init__()
        loadUi(r'C:\Users\Robert\IdeaProjects\MLBManager\display\ui\StandingsWindow.ui', self)
        simulateSeason(league)
        self.div.setText("AL East")
        self.t0.setText(league.ALEast[0].name)
        self.t1.setText(league.ALEast[1].name)
        self.t2.setText(league.ALEast[2].name)
        self.t3.setText(league.ALEast[3].name)
        self.t4.setText(league.ALEast[4].name)
        self.label_6.setText(str(league.ALEast[0].wins))
        self.label_7.setText(str(league.ALEast[1].wins))
        self.label_8.setText(str(league.ALEast[2].wins))
        self.label_9.setText(str(league.ALEast[3].wins))
        self.label_10.setText(str(league.ALEast[4].wins))
        self.div.setText(str(widget.count()))

        self.btnSimAgain.clicked.connect(self.simulateAnotherSeason)

    def simulateAnotherSeason(self):
        x = 1
        screen = StandingsWindow(self.league)
        widget.addWidget(screen)
        #currentIndex = widget.currentIndex
        widget.removeWidget(widget.currentWidget())

class LoadWindow(QDialog):

    def __init__(self):
        super(LoadWindow, self).__init__()
        loadUi(r'C:\Users\Robert\IdeaProjects\MLBManager\display\ui\MainWindow.ui', self)
        self.league = so.startup()

    def simulateSeason(self):

        screen = StandingsWindow(self.league)
        widget.addWidget(screen)
        widget.setCurrentIndex(widget.currentIndex()+1)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    loadingwindow = MainWindow()
    widget.addWidget(loadingwindow)
    widget.setFixedSize(1050, 650)
    widget.setWindowTitle("MLB Manager")
    widget.show()
    sys.exit(app.exec())