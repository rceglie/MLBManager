#cd IdeaProjects\MLBManager\display\ui
#pyuic6 -o MainWindow.py MainWindow.ui

import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog, QStackedWidget
from PyQt6.uic import loadUi
from src import saveoperations as so
import time

class MainWindow(QDialog):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(r'C:\Users\Robert\IdeaProjects\MLBManager\display\ui\MainWindow.ui', self)
        self.league = so.startup()

    def gotoMainWindow(self):
        screen = MainWindow()
        widget.addWidget(screen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class LoadingWindow(QDialog):

    def __init__(self):
        super(LoadingWindow, self).__init__()
        loadUi(r'C:\Users\Robert\IdeaProjects\MLBManager\display\ui\LoadingWindow.ui', self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    loadingwindow = MainWindow()
    widget.addWidget(loadingwindow)
    widget.setFixedSize(1050, 650)
    widget.show()
    sys.exit(app.exec())