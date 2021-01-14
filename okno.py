from PyQt5.QtGui import QFont
import mysql.connector
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow
import sys



class oknoZaloguj(QMainWindow):
    szerokosc = 1200
    wysokosc = 600
    posx = 200
    posy = 200
    jakieokno = 0
    uzytkownik = 0
    def __init__(self):
        super(oknoZaloguj, self).__init__()
        self.setGeometry(self.posx, self.posy, self.szerokosc, self.wysokosc)
        self.initUI()

#inicjacja poczatkowych obiektow
    def initUI(self):
        #Ekran logowania
        self.lOL1 = QtWidgets.QLabel(self)
        self.lOL1.setText("Podaj login i haslo")
        self.lOL1.adjustSize()
        self.lOL1.move(self.szerokosc/2-self.lOL1.size().width()/2, self.wysokosc/5)
        self.lOL1.adjustSize()
        self.lOL1.hide()

        self.bOL1 = QtWidgets.QPushButton(self)
        self.bOL1.setText('Zaloguj')
        self.bOL1.move(self.szerokosc/2-self.bOL1.size().width()/2, self.wysokosc/2)
        self.bOL1.clicked.connect(self.zaloguj)
        self.bOL1.hide() 

        self.itOL1 = QtWidgets.QLineEdit(self)
        self.itOL1.move(self.szerokosc/2-self.itOL1.size().width()/2, self.wysokosc/3.5)
        self.itOL2 = QtWidgets.QLineEdit(self)
        self.itOL2.move(self.szerokosc/2-self.itOL2.size().width()/2, self.wysokosc/2.7)
        self.itOL1.hide()
        self.itOL2.hide()

        self.bOL2 = QtWidgets.QPushButton(self)
        self.bOL2.setText('Stwórz konto')
        self.bOL2.move(self.szerokosc/2-self.bOL1.size().width()/2, self.wysokosc/1.7)
        self.bOL2.clicked.connect(self.stworzKonto)
        self.bOL2.hide()         

        #ekran panelu administratora
        self.lPOA1 = QtWidgets.QLabel(self)
        self.lPOA1.setText("Co chcesz zrobic?")
        self.lPOA1.adjustSize()
        l1size = self.lPOA1.size()
        l1s = l1size.width()
        self.lPOA1.move(self.szerokosc/2-l1s/2, self.wysokosc*0.4)
        self.lPOA1.hide()

        self.lPOA2 = QtWidgets.QLabel(self)
        self.lPOA2.setText("Jesteś w panelu administratora")
        self.lPOA2.setFont(QFont('Arial', 20))
        self.lPOA2.adjustSize()
        l2s = self.lPOA2.size().width()
        self.lPOA2.move(self.szerokosc/2-l2s/2, self.wysokosc*0.2)
        self.lPOA2.hide()

        self.bPOA1 = QtWidgets.QPushButton(self)
        self.bPOA1.setText("Zobacz rekordy")
        bs = self.bPOA1.size().width()
        self.bPOA1.move(self.szerokosc/2-bs/2-100, self.wysokosc*0.6)
        self.bPOA1.hide()

        self.bPOA2 = QtWidgets.QPushButton(self)
        self.bPOA2.setText("Dodaj rekordy")
        self.bPOA2.move(self.szerokosc/2-bs/2, self.wysokosc*0.6)
        self.bPOA2.hide()

        self.bPOA3 = QtWidgets.QPushButton(self)
        self.bPOA3.setText("Usun rekordy")
        self.bPOA3.move(self.szerokosc/2+bs/2, self.wysokosc*0.6)
        self.bPOA3.hide()

        #Zobacz rekordy
        self.lZR1 = QtWidgets.QLabel(self)
        self.lZR1.setText("Jaka tabele chcesz zobaczyc?")
        self.lZR1.adjustSize()
        l1size = self.lZR1.size()
        l1s = l1size.width()
        self.lZR1.move(self.szerokosc/2-l1s/2, self.wysokosc*0.05)
        self.lZR1.hide()

        self.lZR2 = QtWidgets.QLabel(self)
        self.lZR2.setText("Jaka kolumne/kolumny chcesz zobaczyc?")
        self.lZR2.adjustSize()
        l2size = self.lZR2.size()
        l2s = l2size.width()
        self.lZR2.move(self.szerokosc/2-l2s/2, self.wysokosc*0.12)
        self.lZR2.hide()

        self.cbZR1 = QtWidgets.QComboBox(self)
        self.cbZR1.hide()
        self.columna = self.cbZR1.currentText()

        self.cbZR2 = QtWidgets.QComboBox(self)
        self.cbZR2.hide()

        self.bZR1 = QtWidgets.QPushButton(self)
        self.bZR1.setText("Pokaz")
        bs = self.bZR1.size().width()
        self.bZR1.move(self.szerokosc/2-bs/2, self.wysokosc*0.2)
        self.bZR1.hide()

        self.tZR1 = QtWidgets.QTableWidget(self)
        self.tZR1.hide()

        #stworz konto
        self.itSK1 = QtWidgets.QLineEdit(self)
        self.itSK1.move(self.szerokosc/2-self.itSK1.size().width()/2, self.wysokosc/3.5)
        self.itSK2 = QtWidgets.QLineEdit(self)
        self.itSK2.move(self.szerokosc/2-self.itOL2.size().width()/2, self.wysokosc/2.7)
        self.itSK1.hide()
        self.itSK2.hide()

        self.lSK1 = QtWidgets.QLabel(self)
        self.lSK1.setText("Podaj login i haslo ktore chcesz zarejestrowac oraz wybierz jako kto chcesz sie zarejestrowac")
        self.lSK1.adjustSize()
        self.lSK1.move(self.szerokosc/2-self.lSK1.size().width()/2, self.wysokosc/5)
        self.lSK1.adjustSize()
        self.lSK1.hide()

        self.cbSK1 = QtWidgets.QComboBox(self)
        self.cbSK1.addItem('customer')
        self.cbSK1.addItem('servicesupplier')
        self.cbSK1.adjustSize()
        self.cbSK1.move(self.szerokosc/2-self.cbSK1.size().width()/2, self.wysokosc/2.3)
        self.cbSK1.hide()

        #zainicjuj pierwszy ekran
        self.setWindowTitle('Alligro <3 - logowanie')
        self.lOL1.show()
        self.bOL1.show()
        self.bOL2.show()
        self.itOL1.show()
        self.itOL2.show()


#okno logowania - dodac stworz konto i oblusge bledow
    def zaloguj(self):
        login = self.itOL1.text()
        haslo = self.itOL2.text()
        login = 'root'
        haslo = '123123123'
        global mydb
        mydb = mysql.connector.connect(
        host="localhost",
        user=login,
        passwd=haslo,
        database="test"
        )
        global kursor
        kursor = mydb.cursor()
        self.lOL1.hide()
        self.bOL1.hide()
        self.bOL2.hide()
        self.itOL1.hide()
        self.itOL2.hide()
        self.pokazOpcjeAdmin()

#okno tworzenia konta
    def stworzKonto(self):
        self.lOL1.hide()
        self.bOL1.hide()
        self.bOL2.hide()
        self.itOL1.hide()
        self.itOL2.hide()
        self.itSK1.show()
        self.itSK2.show()
        self.lSK1.show()
        self.cbSK1.show()


#okno wyboru opcji - dodac wyloguj i konto
    def pokazOpcjeAdmin(self):
        self.setWindowTitle('Alligro <3 - Panel Administratora')
        self.lPOA1.show()
        self.lPOA2.show()
        self.bPOA1.show()
        self.bPOA1.clicked.connect(self.zobaczRekordy)
        self.bPOA2.show() 
        self.bPOA3.show()

#okno do ogladania rekordów - gotowe
    def zobaczRekordy(self):
        self.setWindowTitle('Alligro <3 - Zobacz rekordy')
        self.lPOA1.hide()
        self.lPOA2.hide()
        self.bPOA1.hide()
        self.bPOA2.hide() 
        self.bPOA3.hide()
        self.lZR1.show()
        self.lZR2.show()
        kursor.execute('Show tables')
        for i in kursor:
            self.cbZR1.addItem(i[0])
        self.cbZR1.adjustSize()
        self.cbZR1.move(self.szerokosc/2-self.cbZR1.size().width()/2,self.wysokosc*0.08)
        self.cbZR1.show()
        self.cbZR1.currentIndexChanged.connect(self.updateState)
        kursor.execute('show columns from category')
        self.cbZR2.addItem('*')
        self.columnsZR1 = 1
        for i in kursor:
            self.cbZR2.addItem(i[0])
            self.columnsZR1+=1
        self.cbZR2.adjustSize()
        self.cbZR2.move(self.szerokosc/2-self.cbZR2.size().width()/2,self.wysokosc*0.15)
        self.cbZR2.show()
        self.bZR1.show()
        self.bZR1.clicked.connect(self.showData)
        self.tZR1.setGeometry(self.szerokosc*0.1,self.wysokosc*0.3,self.szerokosc*0.8, self.wysokosc*0.6)
        self.tZR1.show()
        self.tZR1.setColumnCount(1)
        self.tZR1.setRowCount(1)
        

    def updateState(self):
        self.columnsZR2 = self.cbZR1.currentText()
        self.cbZR2.clear()
        self.cbZR2.addItem('*')
        kursor.execute('show columns from '+ self.columnsZR2)
        for i in kursor:
            self.cbZR2.addItem(i[0])
        self.cbZR2.adjustSize()
        self.cbZR2.move(self.szerokosc/2-self.cbZR2.size().width()/2,self.wysokosc*0.15)

    def showData(self):
        if self.cbZR2.currentText() == "*":
            kursor.execute('show columns from '+self.cbZR1.currentText())
            kolumny = 0
            for i in kursor:
                kolumny +=1
            self.tZR1.clear()
            self.tZR1.setColumnCount(kolumny)
            kursor.execute('Select '+ self.cbZR2.currentText()+ ' from '+ self.cbZR1.currentText())
            wiersze = 0
            for i in kursor:
                wiersze+=1
            self.tZR1.setRowCount(wiersze)
            m, n =0, 0
            kursor.execute('Select '+ self.cbZR2.currentText()+ ' from '+ self.cbZR1.currentText())
            for i in kursor:
                for l in i:
                    newitem = QtWidgets.QTableWidgetItem(str(l))
                    self.tZR1.setItem(m, n, newitem)
                    n+=1
                m+=1
                n = 0
            self.tZR1.resizeColumnsToContents()
            self.tZR1.resizeRowsToContents()
        else:
            self.tZR1.clear()
            self.tZR1.setColumnCount(1)
            kursor.execute('Select '+ self.cbZR2.currentText()+ ' from '+ self.cbZR1.currentText())
            wiersze = 0
            for i in kursor:
                wiersze+=1
            self.tZR1.setRowCount(wiersze)
            m, n =0, 0
            kursor.execute('Select '+ self.cbZR2.currentText()+ ' from '+ self.cbZR1.currentText())
            for i in kursor:
                for l in i:
                    newitem = QtWidgets.QTableWidgetItem(str(l))
                    self.tZR1.setItem(m, n, newitem)
                    n+=1
                m+=1
                n = 0
            self.tZR1.resizeColumnsToContents()
            self.tZR1.resizeRowsToContents()




        






def main():
    app = QApplication(sys.argv)
    win = oknoZaloguj()
    win.show()
    app.exec_()


if __name__ == "__main__":
    main()