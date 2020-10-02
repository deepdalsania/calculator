import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QApplication


def arrowIcon(self):

    self.arrow = QLabel(self)
    self.arrow.setPixmap(QPixmap("ARR.png"))
    self.arrow.setGeometry(QRect(650, 240, 50, 40))
    self.arrow.setScaledContents(True)
    self.arrow.setToolTip('Tech-Totes Club.')

    self.arrow = QLabel(self)
    self.arrow.setPixmap(QPixmap("ARR.png"))
    self.arrow.setGeometry(QRect(280, 345, 30, 30))
    self.arrow.setScaledContents(True)
    self.arrow.setToolTip('Tech-Totes Club.')

    self.arrow = QLabel(self)
    self.arrow.setPixmap(QPixmap("ARR.png"))
    self.arrow.setGeometry(QRect(280, 395, 30, 30))
    self.arrow.setScaledContents(True)
    self.arrow.setToolTip('Tech-Totes Club.')