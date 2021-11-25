import sys
from PyQt6.QtWidgets import QApplication, QWidget, QToolTip, QPushButton, QMessageBox, QMainWindow
from PyQt6.uic import loadUi
from design.ui.main_window import Ui_MainWindow
from src import saveoperations as so
from src import League
from src.main import run
import time

class MainWindow(QMainWindow, Ui_MainWindow, League):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.tempFunction)
        self.league = so.startup()
        self.gotoMainWindow()

    def tempFunction(self):
        #league = run()
        self.label.setText(self.league.allTeams[0].name)