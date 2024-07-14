from aifc import Error
from sqlite3 import OperationalError
import psycopg2
import tkinter as tk
from tkinter import ttk, messagebox



class InteractionWithTheDatabase():

    def __init__(self, host, database, port, user, password):
        self.host = host
        self.database = database
        self.port = port
        self.user = user
        self.password = password
        self.cursor = None
        self.conn = None
    
    def connectionToDatabase(self):
        try:
            self.conn = psycopg2.connect(
                host = self.host,
                database = self.database,
                port = self.port,
                user = self.user,
                password = self.password
            )
            self.cursor = self.conn.cursor()
            
        except OperationalError as e:
            print(f"erroe:{e}")

    def weAskForEmployees(self):
        try:
            self.cursor.execute('SELECT personID, firstName, secondName, surname, gender, dateOfBirth FROM person')
            return self.cursor.fetchall()
        except Error as e:
            print(f"erroe:{e}")
            return[]

    def displayingDataOfSpecificEmployee(self, person_id):
        try:
            self.cursor.execute('SELECT * FROM person WHERE personID = %s', (person_id,))
            result = self.cursor.fetchall()
            return result

        except Error as e:
            print(f"error:{e}")
            return[]

    def documentOutput(self, person_id):
        try:
            self.cursor.execute('SELECT * FROM passportData WHERE personID = %s', (person_id,))
            passport_data = self.cursor.fetchall()
            result = []
            for passport in passport_data:
                self.cursor.execute('SELECT typeOfDocument FROM documentationReference WHERE documentationReferenceID = %s', (passport[2],))
                passport = list(passport)
                passport[2] = self.cursor.fetchone()[0]
                result.append(passport)
            return result

        except Error as e:
            print(f"error:{e}")
            return[]
        
    def addressOutput(self, person_id):
        try:
            self.cursor.execute('SELECT * FROM address WHERE typeOfAdressID = %s', (person_id,))
            typeOfAdress_data = self.cursor.fetchall()
            result = []
            for adress in typeOfAdress_data:
                self.cursor.execute('SELECT typeOfAdress FROM typeOfAdress WHERE typeOfAdressID = %s', (adress[5],))
                adress = list(adress)
                adress[5] = self.cursor.fetchone()[0] 
                result.append(adress)
            return result
        
        except Error as e:
            print(f"error {e}")
            return[]
    
    def addPerson(self, selected_itemFirstName, selected_itemSecondName, selected_itemSurname, selected_itemGender, selected_itemDateOfBirth):
        try:
            self.cursor.execute(''' INSERT INTO person (firstName, secondName, gender, surname, dateOfBirth) VALUES(%s,%s,%s,%s,%s) ''',
                            (selected_itemFirstName, selected_itemSecondName, selected_itemSurname, selected_itemGender, selected_itemDateOfBirth))
            self.conn.commit()

        except Error as e:
            print(f"error {e}")
            return[]
        
    def addDocument(self, selected_itemDocumentationReferenceID, selected_itemSerialNumber, selected_itemNumberPD, selected_itemDateOfIssue, selected_itemIssuedByWhom, person_id):
        try:
            self.cursor.execute(''' INSERT INTO passportData ( documentationReferenceID, serialNumber, numberPD, dateOfIssue, issuedByWhom, personID) VALUES(%s,%s,%s,%s,%s,%s)''',
                (selected_itemDocumentationReferenceID, selected_itemSerialNumber, selected_itemNumberPD, selected_itemDateOfIssue, selected_itemIssuedByWhom, person_id))
            self.conn.commit()

        except Error as e:
            print(f"error {e}")
            return[]
    
    def receivingAllTypesOfDocuments(self):
        try:
            self.cursor.execute('SELECT typeOfDocument FROM documentationReference')
            passport_data = self.cursor.fetchall()
            return passport_data
        
        except Error as e:
            print(f"error {e}")
            return[]
        
    def changePerson(self, selected_itemFirstName, selected_itemSecondName, selected_itemSurname, selected_itemGender, selected_itemDateOfBirth, person_id):
        try:
            self.cursor.execute(''' UPDATE person SET firstName = %s,  secondName = %s, gender = %s, surname = %s, dateOfBirth = %s WHERE personID = %s''',
                (selected_itemFirstName, selected_itemSecondName,  selected_itemGender, selected_itemSurname, selected_itemDateOfBirth, person_id))
            self.conn.commit()

        except Error as e:
            print(f"error {e}")
            return[]

    def deletionPerson(self, person_id):
        self.cursor.execute('DELETE FROM person WHERE personID = %s', (person_id,))
        self.conn.commit()
        
    def closeConnection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

