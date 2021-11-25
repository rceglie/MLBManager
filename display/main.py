#cd IdeaProjects\MLBManager\design\ui
#pyuic6 -o main_window.py main_window.ui

import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog, QStackedWidget
from PyQt6.uic import loadUi
from src import saveoperations as so
import time

class LoadingWindow(QDialog):

    def __init__(self):
        super(LoadingWindow, self).__init__()
        loadUi(r'C:\Users\Robert\IdeaProjects\MLBManager\display\ui\LoadingWindow.ui', self)
        self.league = so.startup()
        #time.sleep(5)
        self.gotoMainWindow()

    def gotoMainWindow(self):
        screen = MainWindow()
        widget.addWidget(screen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class MainWindow(QDialog):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi(r'C:\Users\Robert\IdeaProjects\MLBManager\display\ui\MainWindow.ui', self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    loadingwindow = LoadingWindow()
    screen = MainWindow()
    widget.addWidget(loadingwindow)
    widget.addWidget(screen)
    widget.show()
    sys.exit(app.exec())