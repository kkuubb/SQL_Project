from PyQt5.QtGui import QFont
import mysql.connector
from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QComboBox, QMainWindow, QMessageBox
import sys
import random



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
        self.lista = []
        self.listapolaczen = []
        self.idcustomera = -1
        #przycisk home admin
        self.bPHA1 = QtWidgets.QPushButton(self)
        self.bPHA1.setText('Menu główne')
        self.bPHA1.move(self.szerokosc*0.8, self.wysokosc*0.1)
        self.bPHA1.clicked.connect(self.przejdzDoOpcjiAdmina)
        self.bPHA1.hide() 

        #przycisk home klient
        self.bPHK1 = QtWidgets.QPushButton(self)
        self.bPHK1.setText('Menu główne')
        self.bPHK1.move(self.szerokosc*0.8, self.wysokosc*0.1)
        self.bPHK1.clicked.connect(self.przejdzDoOpcjiCustomer)
        self.bPHK1.hide()

        #Przycisk anuluj
        self.bPA1 = QtWidgets.QPushButton(self)
        self.bPA1.setText('Anuluj')
        self.bPA1.move(self.szerokosc*0.8, self.wysokosc*0.1)
        self.bPA1.clicked.connect(self.przejdzDoLogowania)
        self.bPA1.hide()

        #Przycisk wyloguj
        self.bPW1 = QtWidgets.QPushButton(self)
        self.bPW1.setText('Wyloguj')
        self.bPW1.move(self.szerokosc*0.9, self.wysokosc*0.1)
        self.bPW1.clicked.connect(self.wyloguj)
        self.bPW1.hide()

        #Popup window
        self.popUp = QtWidgets.QMessageBox(self)
        self.popUpKUP = QtWidgets.QMessageBox(self)
        self.popUpKUP.buttonClicked.connect(self.naPewnoChceKupic)
        self.popUpKoniec = QtWidgets.QMessageBox(self)

        #Ekran logowania
        self.lOL1 = QtWidgets.QLabel(self)
        self.lOL1.setText("Podaj login i haslo")
        self.lOL1.adjustSize()
        self.lOL1.move(self.szerokosc/2-self.lOL1.size().width()/2, self.wysokosc/5)
        self.lOL1.adjustSize()
        self.lOL1.hide()

        self.bOL1 = QtWidgets.QPushButton(self)
        self.bOL1.setText('Zaloguj')
        self.bOL1.move(self.szerokosc/2-self.bOL1.size().width(), self.wysokosc/2)
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
        self.bOL2.move(self.szerokosc/2, self.wysokosc/2)
        self.bOL2.clicked.connect(self.stworzKonto)
        self.bOL2.hide()  

        self.cbOL1 = QtWidgets.QComboBox(self)
        self.cbOL1.addItem('admin')
        self.cbOL1.addItem('customer')
        self.cbOL1.addItem('servicesupplier')
        self.cbOL1.adjustSize()
        self.cbOL1.move(self.szerokosc/2-self.cbOL1.size().width()/2, self.wysokosc/2.3)
        self.cbOL1.hide()       

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

        self.bPOA1.clicked.connect(self.zobaczRekordy)
        self.bPOA2.clicked.connect(self.przejdzDoDodawaniaRekordow)
        self.bPOA3.clicked.connect(self.przejdzDoUsuwaniaRekordow)

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
        self.cbZR1.currentTextChanged.connect(self.updateState)

        self.cbZR2 = QtWidgets.QComboBox(self)
        self.cbZR2.hide()

        self.bZR1 = QtWidgets.QPushButton(self)
        self.bZR1.setText("Pokaz")
        bs = self.bZR1.size().width()
        self.bZR1.move(self.szerokosc/2-bs/2, self.wysokosc*0.2)
        self.bZR1.hide()
        self.bZR1.clicked.connect(self.showData)

        self.tZR1 = QtWidgets.QTableWidget(self)
        self.tZR1.hide()

        #stworz konto
        self.itSK1 = QtWidgets.QLineEdit(self)
        self.itSK1.move(self.szerokosc/2-self.itSK1.size().width()/2, self.wysokosc/3.5)
        self.itSK2 = QtWidgets.QLineEdit(self)
        self.itSK2.move(self.szerokosc/2-self.itSK2.size().width()/2, self.wysokosc/2.7)
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

        self.bSK1 = QtWidgets.QPushButton(self)
        self.bSK1.setText('Dalej')
        self.bSK1.move(self.szerokosc/2-self.bSK1.size().width()/2, self.wysokosc/2)
        self.bSK1.hide() 
        self.bSK1.clicked.connect(self.przejdzDoPodawaniaDodatkowychInfo)

        self.bSK2 = QtWidgets.QPushButton(self)
        self.bSK2.setText('Dodaj konto')
        self.bSK2.move(self.szerokosc/2-self.bSK2.size().width()/2, self.wysokosc*0.7)
        self.bSK2.hide()
        self.bSK2.clicked.connect(self.dodajKontoDoTabeli) 

        #Dodaj rekordy
        self.cbDR1 = QtWidgets.QComboBox(self)
        self.cbDR1.hide()
        self.cbDR1.currentIndexChanged.connect(self.pokazPolaDoWypelnienia)

        self.lDR1 = QtWidgets.QLabel(self)
        self.lDR1.setText("Do jakiej tabeli chcesz dodac rekord?")
        self.lDR1.adjustSize()
        l1size = self.lDR1.size()
        l1s = l1size.width()
        self.lDR1.move(self.szerokosc/2-l1s/2, self.wysokosc*0.1)
        self.lDR1.hide()

        self.bDR1 = QtWidgets.QPushButton(self)
        self.bDR1.setText("Dodaj rekordy")
        self.bDR1.move(self.szerokosc/2-self.bDR1.size().width()/2, self.wysokosc*0.9)
        self.bDR1.hide()
        self.bDR1.clicked.connect(self.dodajRekordyDoTabel)

        #Usun rekordy
        self.cbUR1 = QtWidgets.QComboBox(self)
        self.cbUR1.hide()
        self.cbUR1.currentIndexChanged.connect(self.pokazPolaZKotrychUsuwamy)

        self.lUR1 = QtWidgets.QLabel(self)
        self.lUR1.setText("Z jakiej tabeli chcesz usunac rekord?")
        self.lUR1.adjustSize()
        l1size = self.lUR1.size()
        l1s = l1size.width()
        self.lUR1.move(self.szerokosc/2-l1s/2, self.wysokosc*0.1)
        self.lUR1.hide()

        self.lUR2 = QtWidgets.QLabel(self)
        self.lUR2.setText("Podaj wartosc dzieki ktorej mamy znalezc rekord ktory chcesz usunac")
        self.lUR2.adjustSize()
        l1size = self.lUR2.size()
        l1s = l1size.width()
        self.lUR2.move(self.szerokosc/2-l1s/2, self.wysokosc*0.23)
        self.lUR2.hide()

        self.bUR1 = QtWidgets.QPushButton(self)
        self.bUR1.setText('Usun rekord')
        self.bUR1.move(self.szerokosc/2-self.bUR1.size().width()/2, self.wysokosc*0.9)
        self.bUR1.hide() 
        self.bUR1.clicked.connect(self.usunRekord)



        #ekran panelu klienta

        self.lPOK1 = QtWidgets.QLabel(self)
        self.lPOK1.setText("Co chcesz zrobic?")
        self.lPOK1.adjustSize()
        l1size = self.lPOK1.size()
        l1s = l1size.width()
        self.lPOK1.move(self.szerokosc/2-l1s/2, self.wysokosc*0.4)
        self.lPOK1.hide()

        self.lPOK2 = QtWidgets.QLabel(self)
        self.lPOK2.setText("Jesteś w panelu Klienta")
        self.lPOK2.setFont(QFont('Arial', 20))
        self.lPOK2.adjustSize()
        l2s = self.lPOK2.size().width()
        self.lPOK2.move(self.szerokosc/2-l2s/2, self.wysokosc*0.2)
        self.lPOK2.hide()

        self.bPOK1 = QtWidgets.QPushButton(self)
        self.bPOK1.setText("Złóż zamówienie")
        self.bPOK1.adjustSize()
        self.bPOK1.hide()

        self.bPOK2 = QtWidgets.QPushButton(self)
        self.bPOK2.setText("Zobacz zamówienia")
        self.bPOK2.adjustSize()
        self.bPOK2.hide()

        self.bPOK3 = QtWidgets.QPushButton(self)
        self.bPOK3.setText("Twoje konto")
        self.bPOK3.adjustSize()
        self.bPOK3.hide()

        self.bPOK1.move(self.szerokosc/2-self.bPOK1.size().width()-self.bPOK2.size().width()/2, self.wysokosc*0.6)
        self.bPOK2.move(self.szerokosc/2-self.bPOK2.size().width()/2, self.wysokosc*0.6)
        self.bPOK3.move(self.szerokosc/2+self.bPOK2.size().width()/2, self.wysokosc*0.6)
        self.bPOK1.clicked.connect(self.przejdzDoPrzegladaniaproduktow)
        #self.bPOA2.clicked.connect(self.przejdzDoDodawaniaRekordow)
        #self.bPOA3.clicked.connect(self.przejdzDoUsuwaniaRekordow)

        #Ekran ogladania produktów i usług
        self.tPU1 = QtWidgets.QTableWidget(self)
        self.tPU1.hide()

        self.cbPU1 = QtWidgets.QComboBox(self)
        self.cbPU1.hide()
        self.cbPU1.addItem('product')
        self.cbPU1.addItem('service')
        self.cbPU1.move(self.szerokosc/2-self.cbPU1.size().width()/2, self.wysokosc*0.1)
        self.cbPU1.currentTextChanged.connect(self.przegladanieProduktow)

        self.tPU1 = QtWidgets.QTableWidget(self)
        self.tPU1.hide()
        self.tPU1.doubleClicked.connect(self.wybraneDane)

        self.bPU1 = QtWidgets.QPushButton(self)
        self.bPU1.setText("Szukaj")
        self.bPU1.adjustSize()
        self.bPU1.hide()
        self.bPU1.clicked.connect(self.przejdzDoSzukaniaProduktow)
        self.bPU1.move(self.szerokosc/2-self.bPU1.size().width()/2, self.wysokosc*0.93)

        self.logowanie()


    def wyloguj(self):
        for i in self.lista:
            i.hide()
        self.lista = []
        for i in self.listapolaczen:
            i.close()
        self.listapolaczen = []
        self.bPW1.hide()
        self.itOL1.clear()
        self.itOL2.clear()
        self.bPHK1.hide()
        self.bPHA1.hide()
        self.idcustomera = -1
        self.logowanie()

    def przejdzDoLogowania(self):
        for i in self.lista:
            i.hide()
        self.lista = []
        for i in self.polaSK1:
            i.hide()
        for i in self.nazwySK2:
            i.hide()
        for i in self.listapolaczen:
            i.close()
        self.itSK1.clear()
        self.itSK2.clear()
        self.logowanie()
        #zainicjuj pierwszy ekran
    def logowanie(self):
        self.setWindowTitle('Alligro <3 - logowanie')
        self.lOL1.show()
        self.bOL1.show()
        self.bOL2.show()
        self.itOL1.show()
        self.itOL2.show()
        self.cbOL1.show()
        self.bPA1.hide() 


#okno logowania
    def zaloguj(self):
        if self.cbOL1.currentText() == 'admin':
            login = self.itOL1.text()
            haslo = self.itOL2.text()
            if login == 'root' and haslo == '123123123':
                global mydb
                mydb = mysql.connector.connect(
                host="localhost",
                user=login,
                passwd=haslo,
                database="test"
                )
                self.listapolaczen.append(mydb)
                self.kursor = mydb.cursor()
                self.kursor.execute('show tables')
                self.tablice = self.kursor.fetchall()
                self.kursor1 = mydb.cursor()
                self.kursor2 = mydb.cursor()
                self.lOL1.hide()
                self.bOL1.hide()
                self.bOL2.hide()
                self.itOL1.hide()
                self.itOL2.hide()
                self.cbOL1.hide() 
                self.bPHA1.show()
                self.pokazOpcjeAdmin()
                self.bPW1.show()
            else:
                self.showPopup()
        else:
            login = self.itOL1.text()
            haslo = self.itOL2.text()
            kto = self.cbOL1.currentText()
            global mydbNA
            mydbNA = mysql.connector.connect(
            host="localhost",
            user='root',
            passwd='123123123',
            database="test"
            )
            self.listapolaczen.append(mydbNA)
            self.kursorNA = mydbNA.cursor()
            if kto == "customer":
                self.kursorNA.execute("select pswd, customerid from customer where nick = '"+login+"'")
                znaleziony = 0
                for i in self.kursorNA:
                    print(i[1])
                    if i[0]==haslo:
                        self.pokazOpcjeCustomer()
                        znaleziony = 1
                        self.lOL1.hide()
                        self.bOL1.hide()
                        self.bOL2.hide()
                        self.itOL1.hide()
                        self.itOL2.hide()
                        self.cbOL1.hide()
                        self.bPW1.show()
                        self.idcustomera = i[1]
                        break
                if znaleziony == 0:
                    self.showPopup()


    def showPopup(self):
        tytuł = "Sprwadź dane!"
        wiadomosc = "Podałeś błędny login lub hasło"
        self.popUp.setWindowTitle(tytuł)
        self.popUp.setText(wiadomosc)
        self.popUp.setIcon(QMessageBox.Critical)
        x = self.popUp.exec_()
            

#okno tworzenia konta
    def stworzKonto(self):
        self.lOL1.hide()
        self.bOL1.hide()
        self.bOL2.hide()
        self.itOL1.hide()
        self.itOL2.hide()
        self.cbOL1.hide() 
        self.polaSK1 = []
        self.nazwySK1 = []
        self.nazwySK2 = []
        self.itSK1.show()
        self.itSK2.show()
        self.lSK1.show()
        self.cbSK1.show()
        self.bSK1.show()
        self.bPA1.show()
        self.lista = [self.bSK2, self.itSK1, self.itSK2, self.lSK1, self.cbSK1, self.bSK1, self.bPA1]

    def przejdzDoPodawaniaDodatkowychInfo(self):
        if self.itSK1.text() == '' or self.itSK2.text() == '':
            self.showPopup()
        else:
            self.stworzKontoDodatkoweInformacje()

        
    def stworzKontoDodatkoweInformacje(self):
        self.bSK2.show()
        self.ktoSK1 = self.cbSK1.currentText() 
        self.nickSK1 = self.itSK1.text()
        self.pswdSK1 = self.itSK2.text()
        self.itSK1.hide()
        self.itSK2.hide()
        self.lSK1.hide()
        self.cbSK1.hide()
        self.bSK1.hide()
        self.mydbSK = mysql.connector.connect(
        host="localhost",
        user='root',
        passwd='123123123',
        database="test"
        )
        self.listapolaczen.append(self.mydbSK)
        self.kursorSK = self.mydbSK.cursor() 
        self.kursorSK.execute('show columns from '+self.ktoSK1)
        ile = 0
        for i in self.kursorSK:
            self.nazwySK1.append(i[0])
            ile+=1
        self.nazwySK1.pop(0)
        for i in range(ile-3):
            self.polaSK1.append(QtWidgets.QLineEdit(self))
            self.nazwySK2.append(QtWidgets.QLabel(self))
        przesuniecie = 0
        for i in self.polaSK1:
            i.move(self.szerokosc/2-i.size().width()/2, self.wysokosc*0.2+przesuniecie)
            i.show()
            przesuniecie+=30
        przesuniecie = 0
        for i in range(len(self.nazwySK2)):
            self.nazwySK2[i].setText(self.nazwySK1[i])
            self.nazwySK2[i].move(self.szerokosc/2-self.nazwySK2[i].size().width()-self.polaSK1[i].size().width()/2, self.wysokosc*0.2+przesuniecie)
            self.nazwySK2[i].show()
            przesuniecie+=30



        
    def dodajKontoDoTabeli(self):
        mozna = 1
        for i in self.polaSK1:
            if i.text() == '':
                mozna = 0
        if mozna == 1:
            if self.ktoSK1 == "customer":
                self.kursorSK.execute('select customerid from customer')
                indeksy = []
                for i in self.kursorSK:
                    indeksy.append(i[0])

                i=1
                while i in indeksy:
                    i+=1
                self.kursorSK.execute('insert into customer (customerid, companyname, contactName, phone, address, city, postalCode, country, nick, pswd) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)', (str(i), self.polaSK1[0].text(), self.polaSK1[1].text(), self.polaSK1[2].text(), self.polaSK1[3].text(), self.polaSK1[4].text(), self.polaSK1[5].text(), self.polaSK1[6].text(),self.nickSK1, self.pswdSK1))
                self.mydbSK.commit()  

            elif self.ktoSK1 == 'servicesupplier':
                self.kursorSK.execute('select supplierid from servicesupplier')
                indeksy = []
                for i in self.kursorSK:
                    indeksy.append(i[0])

                i=1
                while i in indeksy:
                    i+=1
                self.kursorSK.execute('insert into servicesupplier (supplierId, companyName, contactName, phone, email, homePage, nick, pswd) values (%s,%s,%s,%s,%s,%s,%s,%s)', (str(i), self.polaSK1[0].text(), self.polaSK1[1].text(), self.polaSK1[2].text(), self.polaSK1[3].text(), self.polaSK1[4].text(),self.nickSK1, self.pswdSK1))
                self.mydbSK.commit()
            self.logowanie()
            for i in self.nazwySK2:
                i.hide()
            for i in self.polaSK1:
                i.hide()
            self.bSK2.hide()
        self.itSK1.clear()
        self.itSK2.clear()
        self.mydbSK.close()
#przycisk menu główne
    def przejdzDoOpcjiAdmina(self):
        for i in self.lista:
            i.hide()
        self.lista = []
        self.pokazOpcjeAdmin()
#okno wyboru opcji - dodac wyloguj i konto
    def pokazOpcjeAdmin(self):
        self.setWindowTitle('Alligro <3 - Panel Administratora')
        self.bPHA1.show() 
        self.lPOA1.show()
        self.lPOA2.show()
        self.bPOA1.show()
        self.bPOA3.show()
        self.bPOA2.show() 
        self.lista = [self.lPOA1, self.lPOA2, self.bPOA1, self.bPOA2, self.bPOA3]

#okno do ogladania rekordów - gotowe
    def zobaczRekordy(self):
        self.tZR1.clear()
        self.setWindowTitle('Alligro <3 - Zobacz rekordy')
        self.lPOA1.hide()
        self.lPOA2.hide()
        self.bPOA1.hide()
        self.bPOA2.hide() 
        self.bPOA3.hide()
        self.lZR1.show()
        self.lZR2.show()
        self.cbZR1.clear()
        for i in self.tablice:
            self.cbZR1.addItem(i[0])
        self.cbZR1.adjustSize()
        self.cbZR1.move(self.szerokosc/2-self.cbZR1.size().width()/2,self.wysokosc*0.08)
        self.cbZR1.show()
        self.cbZR2.adjustSize()
        self.cbZR2.move(self.szerokosc/2-self.cbZR2.size().width()/2,self.wysokosc*0.15)
        self.cbZR2.show()
        self.bZR1.show()
        self.tZR1.setGeometry(self.szerokosc*0.1,self.wysokosc*0.3,self.szerokosc*0.8, self.wysokosc*0.6)
        self.tZR1.show()
        self.tZR1.setColumnCount(1)
        self.tZR1.setRowCount(1)
        self.lista = [self.lZR1, self.lZR2, self.cbZR1, self.cbZR2, self.bZR1, self.tZR1]

        

    def updateState(self):
        self.columnsZR2 = self.cbZR1.currentText()
        self.cbZR2.clear()
        self.cbZR2.addItem('*')
        self.kursor.execute("show columns from "+ self.columnsZR2.strip())
        for i in self.kursor:
            self.cbZR2.addItem(i[0])
            dodane =+1
        self.cbZR2.adjustSize()
        self.cbZR2.move(self.szerokosc/2-self.cbZR2.size().width()/2,self.wysokosc*0.15)

    def showData(self):
        if self.cbZR2.currentText() == "*":
            self.kursor.execute('show columns from '+self.cbZR1.currentText())
            kolumny = 0
            nazwykolumn = []
            for i in self.kursor:
                nazwykolumn.append(i[0])
                kolumny +=1
            self.tZR1.clear()
            self.tZR1.setColumnCount(kolumny)
            self.kursor.execute('Select '+ self.cbZR2.currentText()+ ' from '+ self.cbZR1.currentText())
            wiersze = 0
            for i in self.kursor:
                wiersze+=1
            self.tZR1.setRowCount(wiersze)
            m, n =0, 0
            self.kursor.execute('Select '+ self.cbZR2.currentText()+ ' from '+ self.cbZR1.currentText())
            for i in self.kursor:
                for l in i:
                    newitem = QtWidgets.QTableWidgetItem(str(l))
                    self.tZR1.setItem(m, n, newitem)
                    n+=1
                m+=1
                n = 0
            self.tZR1.setHorizontalHeaderLabels(nazwykolumn)
            self.tZR1.resizeColumnsToContents()
            self.tZR1.resizeRowsToContents()
        else:
            self.tZR1.clear()
            self.tZR1.setColumnCount(1)
            self.kursor.execute('Select '+ self.cbZR2.currentText()+ ' from '+ self.cbZR1.currentText())
            wiersze = 0
            for i in self.kursor:
                wiersze+=1
            self.tZR1.setRowCount(wiersze)
            m, n =0, 0
            self.kursor.execute('Select '+ self.cbZR2.currentText()+ ' from '+ self.cbZR1.currentText())
            for i in self.kursor:
                for l in i:
                    newitem = QtWidgets.QTableWidgetItem(str(l))
                    self.tZR1.setItem(m, n, newitem)
                    n+=1
                m+=1
                n = 0
            self.tZR1.resizeColumnsToContents()
            self.tZR1.resizeRowsToContents()

#okno do dodawania rekordow

    def przejdzDoDodawaniaRekordow(self):
        for i in self.lista:
            i.hide()
        self.dodajRekordy()

    def dodajRekordy(self):
        self.kursor1.execute('Show tables')
        self.cbDR1.clear()
        for i in self.kursor1:
            self.cbDR1.addItem(i[0])
        self.cbDR1.adjustSize()
        self.cbDR1.move(self.szerokosc/2-self.cbDR1.size().width()/2,self.wysokosc*0.15)
        self.cbDR1.show()
        self.lDR1.show()
        self.polaSK1 = []
        self.nazwySK1 = []
        self.nazwySK2 = []
        self.bDR1.show()
        self.lista = [self.cbDR1, self.lDR1, self.bDR1]
        self.pokazPolaDoWypelnienia()



    def pokazPolaDoWypelnienia(self):
        self.kursor1.execute('show columns from '+self.cbDR1.currentText())
        for i in self.polaSK1:
            i.hide()
        for i in self.nazwySK2:
            i.hide()
        self.nazwySK2 = []
        self.nazwySK1 = []
        self.polaSK1 = []
        ile = 0
        for i in self.kursor1:
            self.nazwySK1.append(i[0])
            ile+=1

        if self.cbDR1.currentText() == 'orderdetails':
            for i in range(ile):
                self.polaSK1.append(QtWidgets.QLineEdit(self))
                self.nazwySK2.append(QtWidgets.QLabel(self))
        else:
            self.nazwySK1.pop(0)
            for i in range(ile-1):
                self.polaSK1.append(QtWidgets.QLineEdit(self))
                self.nazwySK2.append(QtWidgets.QLabel(self))
        przesuniecie = 0
        for i in self.polaSK1:
            i.move(self.szerokosc/2-i.size().width()/2, self.wysokosc*0.2+przesuniecie)
            i.show()
            przesuniecie+=30
        przesuniecie = 0
        for i in range(len(self.nazwySK2)):
            self.nazwySK2[i].setText(self.nazwySK1[i])
            self.nazwySK2[i].adjustSize()
            self.nazwySK2[i].move(self.szerokosc/2-self.nazwySK2[i].size().width()-self.polaSK1[i].size().width()/2-5, self.wysokosc*0.2+przesuniecie)
            self.nazwySK2[i].show()
            przesuniecie+=30
        
        for i in self.polaSK1:
            self.lista.append(i)
        for i in self.nazwySK2:
            self.lista.append(i)

    def dodajRekordyDoTabel(self):
        if self.cbDR1.currentText() != 'orderdetails':
            if self.cbDR1.currentText() == 'employees':
                idd = 'employee'
            elif self.cbDR1.currentText() == 'orders':
                idd = 'order'
            elif self.cbDR1.currentText() == 'servicesupplier':
                idd = 'supplier'
            else:
                idd = self.cbDR1.currentText()
            self.kursor1.execute('select '+idd+'id from '+self.cbDR1.currentText())
            indeksy = []
            for i in self.kursor1:
                indeksy.append(i[0])

            i = 1
            while i in indeksy:
                i+=1
            kolumny = ''
            kolumnynumer = []
            self.kursor1.execute('show columns from '+self.cbDR1.currentText())
            for k in self.kursor1:
                kolumnynumer.append(k)
            for k in kolumnynumer[1:]:
                kolumny = kolumny + k[0]+ ', '
            wartosci = ' '
            for k in self.polaSK1:
                wartosci = wartosci +"'" +k.text()+"'" +', '
            kolumny = kolumny[0:-2]
            wartosci = wartosci[0:-2]
            self.kursor1.execute('insert into '+ self.cbDR1.currentText() + ' (' +idd+'id, ' +kolumny +') values ('+str(i)+', '+wartosci+')')
            #print('insert into '+ self.cbDR1.currentText() + ' (' +idd+'id, ' +kolumny +') values ('+str(i)+', '+wartosci+')')
        else:
            if self.polaSK1[6].text() == '1':
                kolumny = ''
                kolumnynumer = []
                self.kursor1.execute('show columns from '+self.cbDR1.currentText())
                for k in self.kursor1:
                    if k[0]!='serviceid':
                        kolumnynumer.append(k)
                for k in kolumnynumer:
                    kolumny = kolumny + k[0]+ ', '
                wartosci = ' '
                for k in range(len(self.polaSK1)):
                    if k != 5:
                        wartosci = wartosci +"'" +self.polaSK1[k].text()+"'" +', '
                kolumny = kolumny[0:-2]
                wartosci = wartosci[0:-2]
                self.kursor1.execute('insert into '+ self.cbDR1.currentText() + ' (' +kolumny +') values ('+wartosci+')')
                #print('insert into '+ self.cbDR1.currentText() + ' (' +kolumny +') values ('+wartosci+')')
            if self.polaSK1[6].text() == '2':
                kolumny = ''
                kolumnynumer = []
                self.kursor1.execute('show columns from '+self.cbDR1.currentText())
                for k in self.kursor1:
                    if k[0]!='productid':
                        kolumnynumer.append(k)
                for k in kolumnynumer:
                    kolumny = kolumny + k[0]+ ', '
                wartosci = ' '
                for k in range(len(self.polaSK1)):
                    if k != 3:
                        wartosci = wartosci +"'" +self.polaSK1[k].text()+"'" +', '
                kolumny = kolumny[0:-2]
                wartosci = wartosci[0:-2]
                self.kursor1.execute('insert into '+ self.cbDR1.currentText() + ' (' +kolumny +') values ('+wartosci+')')
                #print('insert into '+ self.cbDR1.currentText() + ' (' +kolumny +') values ('+wartosci+')')
        mydb.commit()

    #okno usuwania rekordow
    def przejdzDoUsuwaniaRekordow(self):
        for i in self.lista:
            i.hide()
        self.usunRekordy()

    def usunRekordy(self):
        self.cbUR1.clear()
        self.polaSK1 = []
        self.nazwySK1 = []
        self.nazwySK2 = []
        self.lista = [self.cbUR1, self.lUR1, self.lUR2, self.bUR1]
        for i in self.tablice:
            self.cbUR1.addItem(i[0])
        self.cbUR1.adjustSize()
        self.cbUR1.move(self.szerokosc/2-self.cbUR1.size().width()/2,self.wysokosc*0.15)
        self.cbUR1.show()
        self.lUR1.show()
        self.lUR2.show()
        self.bUR1.show()

    def pokazPolaZKotrychUsuwamy(self):
        self.kursor1.execute('show columns from '+self.cbUR1.currentText())
        for i in self.polaSK1:
            i.hide()
        for i in self.nazwySK2:
            i.hide()
        self.nazwySK2 = []
        self.nazwySK1 = []
        self.polaSK1 = []
        ile = 0
        for i in self.kursor1:
            self.nazwySK1.append(i[0])
            ile+=1 
        for i in range(ile):
            self.polaSK1.append(QtWidgets.QLineEdit(self))
            self.nazwySK2.append(QtWidgets.QLabel(self))
        przesuniecie = 0
        for i in self.polaSK1:
            i.move(self.szerokosc/2-i.size().width()/2, self.wysokosc*0.3+przesuniecie)
            i.show()
            przesuniecie+=30
        przesuniecie = 0
        for i in range(len(self.nazwySK2)):
            self.nazwySK2[i].setText(self.nazwySK1[i])
            self.nazwySK2[i].adjustSize()
            self.nazwySK2[i].move(self.szerokosc/2-self.nazwySK2[i].size().width()-self.polaSK1[i].size().width()/2-5, self.wysokosc*0.3+przesuniecie)
            self.nazwySK2[i].show()
            przesuniecie+=30
        
        for i in self.polaSK1:
            self.lista.append(i)
        for i in self.nazwySK2:
            self.lista.append(i)

    def usunRekord(self):
        zt = -1
        ktore = 0
        for i in self.polaSK1:
            if len(i.text())>0:
                zt = i.text()
                break
            ktore+=1
        #print("delete from "+ self.cbUR1.currentText() + " where '"+ self.nazwySK2[ktore].text() + "' = '" + zt + "'" ) 
        if zt != -1:
            self.kursor1.execute("delete from "+ self.cbUR1.currentText() + " where "+ self.nazwySK2[ktore].text() + " = '" + zt + "'" )
            mydb.commit()
            
        

    def przejdzDoOpcjiCustomer(self):
        for i in self.lista:
            i.hide()
        self.lista = []
        self.pokazOpcjeCustomer()
    def pokazOpcjeCustomer(self):
        self.setWindowTitle('Alligro <3 - Panel Klienta')
        self.bPOK1.show()
        self.bPOK2.show()
        self.bPOK3.show()
        self.bPHK1.show()
        self.lPOK1.show()
        self.lPOK2.show()
        self.napisyPP = []
        self.polaPP = []
        self.lista = [self.bPOK1, self.bPOK2, self.bPOK3, self.lPOK2, self.lPOK1]


    def przejdzDoPrzegladaniaproduktow(self):
        for i in self.lista:
            i.hide()
        self.lista = []
        self.przegladanieProduktow()
        self.cbPU1.show()
        self.tPU1.show()
        self.bPU1.show()
        self.tPU1.setGeometry(self.szerokosc*0.1,self.wysokosc*0.3,self.szerokosc*0.8, self.wysokosc*0.6)
        self.tPU1.setColumnCount(1)
        self.tPU1.setRowCount(1)
        self.przegladanieProduktow()

    def przegladanieProduktow(self):
        self.kursorNA.execute('show columns from '+ self.cbPU1.currentText())
        for i in self.polaPP:
            i.hide()
        for i in self.napisyPP:
            i.hide()
        self.napisyPP = []
        self.polaPP = []
        kolumny = []
        for i in self.kursorNA:
            kolumny.append(i[0])
        for i in kolumny:
            self.polaPP.append(QtWidgets.QLineEdit(self))
            self.napisyPP.append(QtWidgets.QLabel(self))
        for i in range(len(self.polaPP)):
            self.polaPP[i].move(self.szerokosc/2-(len(kolumny)*self.polaPP[i].size().width()/2)+(i*self.polaPP[i].size().width()), self.wysokosc*0.2)
            self.polaPP[i].show()
        for i in range(len(self.napisyPP)):
            self.napisyPP[i].move(self.szerokosc/2-(len(kolumny)*self.napisyPP[i].size().width()/2)+(i*self.napisyPP[i].size().width()), self.wysokosc*0.15)
            self.napisyPP[i].setText(kolumny[i])
            self.napisyPP[i].show()

        self.kursorNA.execute('show columns from '+self.cbPU1.currentText())
        kolumnyl = 0
        for i in self.kursorNA:
            kolumnyl +=1
        self.tPU1.clear()
        self.tPU1.setColumnCount(kolumnyl)
        self.kursorNA.execute('Select * from '+ self.cbPU1.currentText())
        wiersze = 0
        for i in self.kursorNA:
            wiersze+=1
        self.tPU1.setRowCount(wiersze)
        m, n =0, 0
        self.kursorNA.execute('Select * from '+ self.cbPU1.currentText())
        for i in self.kursorNA:
            for l in i:
                newitem = QtWidgets.QTableWidgetItem(str(l))
                self.tPU1.setItem(m, n, newitem)
                n+=1
            m+=1
            n = 0
        self.tPU1.setHorizontalHeaderLabels(kolumny)
        self.tPU1.resizeColumnsToContents()
        self.tPU1.resizeRowsToContents()

        for i in self.polaPP:
            self.lista.append(i)
        for i in self.napisyPP:
            self.lista.append(i)
        self.lista.append(self.cbPU1)
        self.lista.append(self.tPU1)
        self.lista.append(self.bPU1)

    def przejdzDoSzukaniaProduktow(self):
        self.znalezionePP = -1
        for i in range(len(self.polaPP)):
            if self.polaPP[i].text() != '':
                self.znalezionePP = i
                break
        if self.znalezionePP == -1:
            self.przejdzDoPrzegladaniaproduktow()
        else:
            self.pokazWyszukaneRekordy()
    
    def pokazWyszukaneRekordy(self):       
        self.kursorNA.execute('show columns from '+self.cbPU1.currentText())
        kolumny = 0
        for i in self.kursorNA:
            kolumny +=1
        self.tPU1.clear()
        self.tPU1.setColumnCount(kolumny)
        self.kursorNA.execute('select * from '+self.cbPU1.currentText() + ' where ' + self.napisyPP[self.znalezionePP].text() + ' = ' + self.polaPP[self.znalezionePP].text())
        wiersze = 0
        for i in self.kursorNA:
            wiersze+=1
        self.tPU1.setRowCount(wiersze)
        m, n =0, 0
        self.kursorNA.execute('select * from '+self.cbPU1.currentText() + ' where ' + self.napisyPP[self.znalezionePP].text() + ' = ' + self.polaPP[self.znalezionePP].text())
        for i in self.kursorNA:
            for l in i:
                newitem = QtWidgets.QTableWidgetItem(str(l))
                self.tPU1.setItem(m, n, newitem)
                n+=1
            m+=1
            n = 0
        self.tPU1.resizeColumnsToContents()
        self.tPU1.resizeRowsToContents()

    def wybraneDane(self):
        self.rowKUP = 0
        for idx in self.tPU1.selectionModel().selectedIndexes():
            self.rowKUP = idx.row()
        self.idtegoczegos = self.tPU1.item(self.rowKUP, 0).text()
        self.showPopupKUP()

    def showPopupKUP(self):
        tytuł = "Kupowanie <3"
        wiadomosc = "Czy na pewno chcesz kupić ten przedmiot?"
        self.popUpKUP.setWindowTitle(tytuł)
        self.popUpKUP.setText(wiadomosc)
        self.popUpKUP.setIcon(QMessageBox.Question)
        self.popUpKUP.setStandardButtons(QMessageBox.Yes|QMessageBox.No)
        x = self.popUpKUP.exec_()

    def showPopupKoniecProduktu(self):
        tytuł = "Skończyło się :/"
        wiadomosc = "Niestety produkt który próbujesz kupić się skończył"
        self.popUpKoniec.setWindowTitle(tytuł)
        self.popUpKoniec.setText(wiadomosc)
        self.popUpKoniec.setIcon(QMessageBox.Warning)
        x = self.popUpKoniec.exec_()

    def naPewnoChceKupic(self, i):

        if i.text() != '&No':
            if self.cbPU1.currentText() == 'product':
                self.kursorNA.execute("select instock from product where productid = " + self.idtegoczegos)
                ilezostalo = self.kursorNA.fetchone()
                ilezostalo = ilezostalo[0]
                if ilezostalo == 0:
                    self.showPopupKoniecProduktu()
                else:
                    self.kursorNA.execute('select employeeid from employees')
                    listapracownikow = []
                    for i in self.kursorNA:
                        listapracownikow.append(i[0])
                    self.kursorNA.execute('select shipperid from shipper')
                    listadostawcow = []
                    for i in self.kursorNA:
                        listadostawcow.append(i[0])
                    self.kursorNA.execute('select orderid from orders')
                    indeksy = []
                    for i in self.kursorNA:
                        indeksy.append(i[0])
                    i=1
                    while i in indeksy:
                        i+=1    
                    kolejka = ("call dodajDetaleZamowienia (%s, %s,%s, %s,%s, %s,'%s')")
                    self.kursorNA.execute(kolejka, (str(i), self.idcustomera, random.choice(listapracownikow), random.choice(listadostawcow), self.idtegoczegos, 3, 1))
                    mydbNA.commit()
            else:
                self.kursorNA.execute("select instock from service where serviceid = " + self.idtegoczegos)
                ilezostalo = self.kursorNA.fetchone()
                ilezostalo = ilezostalo[0]
                if ilezostalo == 0:
                    self.showPopupKoniecProduktu()
                else:
                    self.kursorNA.execute('select employeeid from employees')
                    listapracownikow = []
                    for i in self.kursorNA:
                        listapracownikow.append(i[0])
                    self.kursorNA.execute('select shipperid from shipper')
                    listadostawcow = []
                    for i in self.kursorNA:
                        listadostawcow.append(i[0])
                    self.kursorNA.execute('select orderid from orders')
                    indeksy = []
                    for i in self.kursorNA:
                        indeksy.append(i[0])
                    i=1
                    while i in indeksy:
                        i+=1    
                    kolejka = ("call dodajDetaleZamowienia (%s, %s,%s, %s,%s, %s,'%s')")
                    self.kursorNA.execute(kolejka, (str(i), self.idcustomera, random.choice(listapracownikow), random.choice(listadostawcow), 3, self.idtegoczegos, 2))
                    mydbNA.commit()


        
        
    



def main():
    app = QApplication(sys.argv)
    win = oknoZaloguj()
    win.show()
    app.exec_()


if __name__ == "__main__":
    main()