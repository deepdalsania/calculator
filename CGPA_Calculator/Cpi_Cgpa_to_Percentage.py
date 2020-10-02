import sys
import urllib
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtWidgets import QMainWindow, QLabel, QLineEdit, QPushButton, QApplication


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Design Window
        self.setWindowIcon(QIcon("CAL2.png"))
        self.setMinimumSize(QSize(1366, 825))
        self.setWindowTitle("SPI/CGPA")
        self.setStyleSheet('background-color:white;')

        # Input Take from the User
        self.line = QLineEdit(self)
        self.line.setPlaceholderText('Enter CPI/CGPA')
        self.line.setStyleSheet('border: 1px solid black;background-color : LightGrey;')
        self.line.move(450, 240)
        self.line.resize(100, 32)
        self.line.setToolTip('Enter CPI/CGPA')
        self.line.returnPressed.connect(self.checkValidation)

        # Output Give to the User
        self.resultBox = QLineEdit(self)
        self.resultBox.move(800, 240)
        self.resultBox.setStyleSheet('border: 1px solid black;background-color : LightGrey;')
        self.resultBox.setPlaceholderText("0.00%")
        self.resultBox.setToolTip('Result in Percentage.')
        self.resultBox.setReadOnly(True)
        self.resultBox.resize(100, 32)

        # Set Logos
        self.setLogos()

        # Set All Labels
        self.setLabel()

        # Set Arrow ICON
        self.setAllIcon()

        # Set All Profile
        self.setAllProfile()

        self.show()

    def setAllProfile(self):

        self.firstProfile = QLabel(self)
        self.firstProfile.setText("Mr. Darshan Bhatt<br>Software Developer")
        self.firstProfile.move(10, 550)
        self.firstProfile.setFont(QFont("Times new Roman", 15))
        self.firstProfile.adjustSize()

        self.firstProfile = QLabel(self)
        self.firstProfile.setText("Deep Dalsania<br>Software Engineer")
        self.firstProfile.move(200, 550)
        self.firstProfile.setFont(QFont("Times new Roman", 15))
        self.firstProfile.adjustSize()

        self.firstProfile = QLabel(self)
        self.firstProfile.setText("Bharat Kadchha<br>Software Developer")
        self.firstProfile.move(380, 550)
        self.firstProfile.setFont(QFont("Times new Roman", 15))
        self.firstProfile.adjustSize()

    def setLogos(self):

        self.nLogo = QLabel(self)
        self.nLogo.setPixmap(QPixmap('NGILOGO.png'))
        self.nLogo.setGeometry(QRect(20, 10, 150, 75))
        self.nLogo.setScaledContents(True)
        self.nLogo.setToolTip('Noble Group of Institution.')

        self.tLogo = QLabel(self)
        self.tLogo.setPixmap(QPixmap("TT2LOGO.png"))
        self.tLogo.setGeometry(QRect(1175, 10, 160, 150))
        self.tLogo.setScaledContents(True)
        self.tLogo.setToolTip('Tech-Totes Club.')

    def setLabel(self):

        self.fMsg = QLabel(self)
        self.fMsg.setText(
            "<b>Here You can calculate percentage (%) from CPI/CGPA/SPI. SPI/CPI/CGPA is mentioned in marksheet.</b>")
        self.fMsg.setFont(QFont("Times new Roman", 12))
        self.fMsg.move(340, 350)
        self.fMsg.adjustSize()

        self.fMsg = QLabel(self)
        self.fMsg.setText("<b>Percentage (%) = (( SPI \ CPI \ CGPA) - 0.5) x 10</b>")
        self.fMsg.setFont(QFont("Times new Roman", 12))
        self.fMsg.move(420, 400)
        self.fMsg.adjustSize()

        # Hording
        self.Hording = QLabel(self)
        self.Hording.setText("<h1><font color='blue'><b>GTU Calculator for CPI/CGPA to Percentage</b></font></h1>")
        self.Hording.setStyleSheet('background-color : white;font-family: "Times new Roman')
        self.Hording.setFont(QFont("Times new Roman", 10))
        self.Hording.move(400, 10)
        self.Hording.adjustSize()

        # Error label
        self.errorLabel = QLabel(self)
        self.errorLabel.move(450, 290)
        self.errorLabel.setFont(QFont('10'))

    def setAllIcon(self):

        self.twitter = QLabel(self)
        self.twitter.setOpenExternalLinks(True)
        self.twitter.setText("<a href='www.linkedin.com/in/bharat-kadchha'>Linkedin</a>&nbsp;&nbsp;")
        self.twitter.setGeometry(QRect(10, 600, 30, 30))
        self.twitter.setScaledContents(True)
        self.twitter.adjustSize()

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

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Backspace or e.key() == Qt.Key_Delete:
            self.line.clear()
            self.resultBox.clear()
            self.errorLabel.clear()
        if e.key() == Qt.Key_Escape:
            self.close()

    # Check Validation of the Number
    def checkValidation(self):
        print(len(self.line.text()))
        if len(self.line.text()) == 0:
            self.errorLabel.setText("<font color='red'><b>* Required.</b></font>")
            self.resultBox.clear()
        elif self.line.text().__contains__('.') and len(self.line.text().split('.')[1]) > 2:
            self.errorLabel.setText("<font color='red'><b>* Please enter CPI/CGPA in proper format.</b></font>")
        elif (self.line.text().isnumeric() and 1 <= int(self.line.text()) <= 10) or 1.00 <= float(
                self.line.text()) <= 10.00:
            self.resultBox.setText(str(round(((float(self.line.text()) - 0.5) * 10), 2)) + ' %')
            self.resultBox.setAlignment(Qt.AlignCenter)
            self.errorLabel.clear()
        else:
            self.errorLabel.setText("<font color='red'><b>* Please enter CPI/CGPA between 1.00 to 10.00.</b></font")
            self.resultBox.clear()
        self.errorLabel.adjustSize()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    sys.exit(app.exec_())
