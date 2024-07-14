import tkinter as tk
from tkinter import ttk, messagebox
from InteractionWithTheDatabase import InteractionWithTheDatabase
from UserTable import UserTable
from DocumentsTable import DocumentsTable
from AddressTable import AdressTable
from CustomButton import CustomButton
# from SearchUsers import SearchUsers

class MainWindow():
    def __init__(self, root):
        self.root = root
        self.interactionWithTheDatabase = InteractionWithTheDatabase('localhost', 'main', 5432, "postgres", '123')
        self.userTable = UserTable(self.root)
        self.documentsTable = DocumentsTable(self.root, self.userTable)
        self.addressTable = AdressTable(self.root, self.userTable)
        self.addButton = CustomButton(0.2,0.36,"Добавление пользоавателя",self.root, self.userTable, self.documentsTable, self.addressTable)
        self.deletionButton = CustomButton(0.5,0.36,"Удаление пользователя",self.root, self.userTable,self.documentsTable,self.addressTable)
        self.changeButton = CustomButton(0.8,0.36,"Изменить пользователя",self.root, self.userTable,self.documentsTable,self.addressTable)
        self.addButtonDcument = CustomButton(0.2,0.63,"Добавить документ",self.root, self.userTable, self.documentsTable, self.addressTable)
        self.deletionButtonDcument = CustomButton(0.5,0.63,"Удалить документ",self.root, self.userTable, self.documentsTable, self.addressTable)
        self.changeButtonDcument = CustomButton(0.8,0.63,"Изменить документ",self.root, self.userTable, self.documentsTable, self.addressTable)

        self.addButtonPassport = CustomButton(0.2,0.9,"Добавить адрес",self.root, self.userTable, self.documentsTable, self.addressTable)
        self.deletionButtonPassport = CustomButton(0.5,0.9,"Удалить адрес",self.root, self.userTable, self.documentsTable, self.addressTable)
        self.changeButtonPassport = CustomButton(0.8,0.9,"Изменить адрес",self.root, self.userTable, self.documentsTable, self.addressTable)

    def displayTheMainWindow(self):
        self.root.geometry('800x800')
        self.root.resizable(width=False, height=False)
        self.interactionWithTheDatabase.connectionToDatabase()
        self.userTable.tableOutput()
        self.userTable.tree.bind("<ButtonRelease-1>", self.updateTables)
        self.addButton.pressingAdd()
        self.deletionButton.pressingDelete()
        self.changeButton.pressingСhange()
        
    def updateTables(self, event):
        self.documentsTable.tableOutput(event)
        self.addressTable.tableOutput(event)
        self.addButtonDcument.documentAdd()
        self.deletionButtonDcument.documentDeletion()
        self.changeButtonDcument.documentChange()
        self.addButtonPassport.passportAdd()
        self.deletionButtonPassport.passportDeletion()
        self.changeButtonPassport.passportChange()

def main():
    root = tk.Tk()
    app = MainWindow(root)
    app.displayTheMainWindow()
    root.mainloop()

if __name__ == "__main__":
    main()