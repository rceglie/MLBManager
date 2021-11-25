#cd IdeaProjects\MLBManager\design\ui
#pyuic6 -o main_window.py main_window.ui

import sys
from PyQt6 import QtWidgets
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMessageBox, QDialog, QStackedWidget
from PyQt6.uic import loadUi
from design.ui.main_window import Ui_MainWindow
from src import saveoperations as so
from design.ui import LoadingWindow as lw

class LoadingWindow(QDialog):

    def __init__(self):
        super(LoadingWindow, self).__init__()
        loadUi("LoadingWindow.ui", self)
        self.league = so.startup()
        self.gotoMainWindow()

    def gotoMainWindow(self):
        screen = MainWindow()
        widget.addWidget(screen)
        widget.setCurrentIndex(widget.currentIndex()+1)

class MainWindow(QDialog):

    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("MainWindow.ui", self)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()
    loadingwindow = LoadingWindow()
    screen = MainWindow()
    widget.addWidget(loadingwindow)
    widget.addWidget(screen)
    widget.show()
    sys.exit(app.exec())