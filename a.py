import mysql.connector

#haslo = !Haslo123123
#user = input('Podaj uzytkownika')
#haslo = input("Podaj haslo")

user = 'root'
haslo = '123123123'
mydb = mysql.connector.connect(
  host="localhost",
  user=user,
  passwd=haslo,
  database="test"
)
kursor = mydb.cursor()


def addCategory():
  kursor.execute('select categoryid from category')
  indeksy = []
  for i in kursor:
    indeksy.append(i[0])
  
  nazwa = input("Podaj nazwe kategorii (Wymagane)\n")
  opis = input("Podaj opis kategorii\n")
  zdjecie = input("Podaj sciezke do zdjecia\n")
  i=1
  while i in indeksy:
    i+=1
  kursor.execute('insert into category (categoryid, categoryname, descriptions) values (%s,%s,%s)', (str(i), nazwa, opis))
  mydb.commit()

def addSupplier():
  kursor.execute('select supplierid from supplier')
  indeksy = []
  for i in kursor:
    indeksy.append(i[0])
  
  companyName = input("Podaj nazwe firmy (Wymagane)\n")
  contactName = input("Podaj imie i nazwisko osoby kontaktowej\n")
  phone = input("Podaj numer telefonu\n")
  email = input("Podaj email\n")
  homePage = input("Podaj strone domowa\n")
  i=1
  while i in indeksy:
    i+=1
  kursor.execute('insert into supplier (supplierId, companyName, contactName, phone, email, homePage) values (%s,%s,%s,%s,%s,%s)', (str(i), companyName, contactName, phone, email, homePage))
  mydb.commit()
  
def addProduct():
  kursor.execute('select productid from product')
  indeksy = []
  for i in kursor:
    indeksy.append(i[0])
  
  productname = input("Podaj nazwe produktu (Wymagane)\n")
  price = input("Podaj cene produktu (Wymagane)\n")
  instock = input("Podaj ilosc produktu\n")
  supplierID = input('Podaj ID dostawcy\n')
  categoryID = input("Podaj ID kategorii\n")
  i=1
  while i in indeksy:
    i+=1
  kursor.execute('insert into product (productid, productname, price, instock, supplierID, categoryID) values (%s,%s,%s,%s,%s,%s)', (str(i), productname, price, instock, supplierID, categoryID))
  mydb.commit()

def addServiceSupplier():
  kursor.execute('select supplierid from servicesupplier')
  indeksy = []
  for i in kursor:
    indeksy.append(i[0])
  
  companyName = input("Podaj nazwe firmy (Wymagane)\n")
  contactName = input("Podaj imie i nazwisko osoby kontaktowej\n")
  phone = input("Podaj numer telefonu\n")
  email = input("Podaj email\n")
  homePage = input("Podaj strone domowa\n")
  i=1
  while i in indeksy:
    i+=1
  kursor.execute('insert into servicesupplier (supplierId, companyName, contactName, phone, email, homePage) values (%s,%s,%s,%s,%s,%s)', (str(i), companyName, contactName, phone, email, homePage))
  mydb.commit()

def addService():
  kursor.execute('select serviceid from service')
  indeksy = []
  for i in kursor:
    indeksy.append(i[0])
  
  typeOfService = input("Podaj typ usługi (Wymagane)\n")
  price = input("Podaj cene produktu (Wymagane)\n")
  instock = input("Podaj ilosc produktu\n")
  supplierID = input('Podaj ID dostawcy\n')

  i=1
  while i in indeksy:
    i+=1
  kursor.execute('insert into service (serviceid, typeofservice, price, instock, supplierID) values (%s,%s,%s,%s,%s)', (str(i), typeOfService, price, instock, supplierID))
  mydb.commit()

def addShipper():
  kursor.execute('select shipperid from shipper')
  indeksy = []
  for i in kursor:
    indeksy.append(i[0])

  companyName = input("Podaj nazwe firmy (Wymagane)\n")
  phone = input("Podaj numer telefonu (Wymagane)\n")

  i=1
  while i in indeksy:
    i+=1
  kursor.execute('insert into shipper (shipperid, companyName, phone) values (%s,%s,%s)', (str(i), companyName, phone))
  mydb.commit()

def addCustomer():
  kursor.execute('select customerid from customer')
  indeksy = []
  for i in kursor:
    indeksy.append(i[0])

  companyName = input("Podaj nazwe firmy\n")
  contactName = input("Podaj imie i nazwisko (wymagane)\n")
  phone = input("Podaj numer telefonu (wymagane)\n")
  address = input("Podaj adres\n")
  city = input("Podaj miasto\n")
  postalCode = input("Podaj kod pocztowy (same liczby)\n")
  country = input("Podaj kraj\n")

  i=1
  while i in indeksy:
    i+=1
  kursor.execute('insert into customer (customerid, companyname, contactName, phone, address, city, postalCode, country) values (%s,%s,%s,%s,%s,%s,%s,%s)', (str(i), companyName, contactName, phone, address, city, postalCode, country))
  mydb.commit()  

def addRegion():
  kursor.execute('select regionid from region')
  indeksy = []
  for i in kursor:
    indeksy.append(i[0])

  regionDescription = input("Podaj opis regionu (wymagane)\n")

  i=1
  while i in indeksy:
    i+=1
  kursor.execute('insert into region (regionid, regionDescription) values (%s,%s)', (str(i), regionDescription))
  mydb.commit() 

def addEmployees():
  kursor.execute('select employeeid from employees')
  indeksy = []
  for i in kursor:
    indeksy.append(i[0])

  lastName = input("Podaj nazwisko (wymagane)\n")
  firstName = input("Podaj imie (wymagane)")
  hireTime = input("Podaj date zatrudnienia (Format:)")
  title = input("Podaj stanowisko")
  phone = input("Podaj numer telefonu (wymagane)")
  email = input("Podaj email (wymagane)")
  regionID = input("Podaj region w jakim pracujesz")

  i=1
  while i in indeksy:
    i+=1
  kursor.execute('insert into employees (employeeid, lastName, firstName, hireTime, title, phone, email, regionID) values (%s,%s,%s,%s,%s,%s,%s,%s)', (str(i), lastName, firstName, hireTime, title, phone, email, regionID))
  mydb.commit() 

def addOrders():
  pass








def main():
  while(1):
    decyzja1 = int(input('Co chesz zrobic\n1.Dodac do tabeli\n2.Zobaczyc tabele\n'))
    if decyzja1 == 1:
      print('Do jakiej tabeli chcesz dodac rekord?\n')
      kursor.execute('show tables')
      k = 1
      for i in kursor:
        print(str(k)+'. '+i[0])
        k+=1
      #print('1.Category\n2.Supplier\n3.Product')
      decyzja2 = int(input())
      if decyzja2 == 1:
        addCategory()
      elif decyzja2 == 2:
        addSupplier()
      elif decyzja2 == 3:
        addProduct()
      elif decyzja2 == 4:
        addServiceSupplier()
      elif decyzja2 == 5:
        addService()
      elif decyzja2 == 6:
        addCustomer()
      elif decyzja2 == 7:
        addRegion()
      elif decyzja2 == 8:
        addEmployees()
    if decyzja1 == 2:
      decyzja3 = input("Z jakiej tabeli chcesz wyswietlic dane?\n")
      decyzja4 = input("Jakie kolumny chcesz wyswietlic\n")
      kursor.execute('select '+decyzja4.strip() + ' from ' + decyzja3.strip())
      for i in kursor:
        print(i)
      print('\n')
    #kursor.execute('select * from product')
    #for h in kursor:
    #  print(h)





if __name__ == "__main__":
    main()




