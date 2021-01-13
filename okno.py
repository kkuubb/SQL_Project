import mysql.connector
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys


class oknoZaloguj(QMainWindow):
    szerokosc = 600
    wysokosc = 300
    posx = 200
    posy = 200
    def __init__(self):
        super(oknoZaloguj, self).__init__()
        self.setGeometry(self.posx, self.posy, self.szerokosc, self.wysokosc)
        self.initUI()

#inicjacja poczatkowych obiektow
    def initUI(self):
        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText("Podaj login i haslo")
        self.l1.move(self.szerokosc/2.5, self.wysokosc/5)
        self.l1.adjustSize()
        self.l1.hide()

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Zaloguj')
        self.b1.move(self.szerokosc/2.4, self.wysokosc/1.7)
        self.b1.clicked.connect(self.zaloguj)
        self.b1.hide() 

        self.it1 = QtWidgets.QLineEdit(self)
        self.it1.move(self.szerokosc/2.4, self.wysokosc/3.5)
        self.it2 = QtWidgets.QLineEdit(self)
        self.it2.move(self.szerokosc/2.4, self.wysokosc/2.5)
        self.it1.hide()
        self.it2.hide()

        self.setWindowTitle('Alligro <3 - logowanie')
        self.l1.show()
        self.b1.show()
        self.it1.show()
        self.it2.show()

#okno logowania
    def zaloguj(self):
        login = self.it1.text()
        haslo = self.it2.text()
        global mydb
        mydb = mysql.connector.connect(
        host="localhost",
        user=login,
        passwd=haslo,
        database="test"
        )
        global kursor
        kursor = mydb.cursor()
        self.l1.hide()
        self.b1.hide()
        self.it1.hide()
        self.it2.hide()
        self.pokazOpcje()
#okno wyboru opcji
    def pokazOpcje(self):
        self.setWindowTitle('Alligro <3 - Jakie dzialanie chcesz wykonac?')
        l1 = QtWidgets.QLabel(self)
        l1.setText("Co chcesz zrobic?")
        l1.adjustSize()
        l1size = l1.size()
        l1s = l1size.width()
        l1w = l1size.height()
        l1.move(self.szerokosc/2-l1s/2, self.wysokosc/7)
        l1.show()
 


        






def main():
    app = QApplication(sys.argv)
    win = oknoZaloguj()
    win.show()
    app.exec_()


if __name__ == "__main__":
    main()