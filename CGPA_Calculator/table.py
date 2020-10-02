import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QApplication, QTableWidget, QTableView


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Design Window
        self.setMinimumSize(QSize(1000, 825))
        self.setWindowTitle("SPI/CGPA")
        self.setStyleSheet('background-color:white;')

        self.t = QTableWidget(self)
        self.t.setRowCount(2)
        self.t.setColumnCount(3)
        self.t.resize(300, 200)
        self.t.move(500, 300)
        self.t.setDropIndicatorShown(False)
        self.t.setShowGrid(False)

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    sys.exit(app.exec_())
