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


    def initUI(self):
        self.l1 = QtWidgets.QLabel(self)
        self.l1.setText("Co chcesz zrobic?")
        self.l1.adjustSize()
        
        self.l1.move(self.szerokosc/2, self.wysokosc/8)
        print(self.l1.size())
        self.l1.show()

def main():
    app = QApplication(sys.argv)
    win = oknoZaloguj()
    win.show()
    app.exec_()


if __name__ == "__main__":
    main()