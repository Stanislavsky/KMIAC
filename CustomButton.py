import tkinter as tk
from tkinter import NW, StringVar, ttk, messagebox
from InteractionWithTheDatabase import InteractionWithTheDatabase

class CustomButton():
    def __init__(self, relx, rely, text, root, userTable, documentsTable, addressTable):
        self.relx = relx
        self.rely = rely
        self.text = text
        self.root = root
        self.userTable = userTable
        self.documentsTable = documentsTable
        self.addressTable = addressTable
        
    def deleteUser(self):
        person_id = self.userTable.giveId()

        if person_id == None:
            messagebox.showinfo("Предупреждение", message="Перед удалением нужно выбрать пользователя")
            return
        
        result = messagebox.askyesno(title="Удаление", message="Вы уверены, что хотите удалить пользователя?")
        if result:
            
            person_id = self.userTable.giveId()

            interactionWithTheDatabase = InteractionWithTheDatabase('localhost', 'main', 5432, "postgres", '123')
            interactionWithTheDatabase.connectionToDatabase()
            interactionWithTheDatabase.deletionPerson(person_id)
            interactionWithTheDatabase.closeConnection()
            messagebox.showinfo("Успех", message="Пользователь успешно удален")

            self.userTable.tableOutput()
            self.documentsTable.tableOutput()  
            self.addressTable.tableOutput()
            
        else:
            messagebox.showinfo("Удаление отменено", "Удаление пользователя отменено.") 

    def changeUser(self):

        person_id = self.userTable.giveId()
        if person_id == None:
            messagebox.showinfo("Предупреждение", message="Перед изменением нужно выбрать пользователя")
            return

        new_window = tk.Toplevel()
        new_window.geometry('350x200')
        new_window.title("Отдельное окно")

        titleEFirstName = tk.Label(new_window, text="Имя:", font='Times 10')
        titleEFirstName.place(relx=0, rely=0.07, anchor="w")

        titleESecondName = tk.Label(new_window, text="Фамилия:", font='Times 10')
        titleESecondName.place(relx=0, rely=0.23, anchor="w")

        titleEGender = tk.Label(new_window, text="Отчество:", font='Times 10')
        titleEGender.place(relx=0, rely=0.39, anchor="w")

        titleESurname = tk.Label(new_window, text="Пол:", font='Times 10')
        titleESurname.place(relx=0, rely=0.55, anchor="w")

        titleEDateOfBirth = tk.Label(new_window, text="Дата рождения:", font='Times 10')
        titleEDateOfBirth.place(relx=0, rely=0.71, anchor="w")

        eFirstName = tk.Entry(new_window)
        eFirstName.place(x=100, y=8, width=200)
        eSecondName = tk.Entry(new_window)
        eSecondName.place(x=100, y=40, width=200)
        eGender = tk.Entry(new_window)
        eGender.place(x=100, y=70, width=200)
        eSurname = tk.Entry(new_window)
        eSurname.place(x=100, y=102, width=200)
        eDateOfBirth = tk.Entry(new_window)
        eDateOfBirth.place(x=100, y=132, width=200)

        interactionWithTheDatabase = InteractionWithTheDatabase('localhost', 'main', 5432, "postgres", '123')
        interactionWithTheDatabase.connectionToDatabase()
        person = interactionWithTheDatabase.displayingDataOfSpecificEmployee(person_id)
        interactionWithTheDatabase.closeConnection()

        eFirstName.insert(0, person[0][1])
        eSecondName.insert(0, person[0][2])
        eSurname.insert(0, person[0][3])
        eGender.insert(0, person[0][4])
        eDateOfBirth.insert(0, person[0][5])

        def change():
            selected_itemFirstName = eFirstName.get().strip()
            selected_itemSecondName = eSecondName.get().strip()
            selected_itemSurname = eSurname.get().strip()
            selected_itemGender = eGender.get().strip()
            selected_itemDateOfBirth = eDateOfBirth.get().strip()

            if not selected_itemFirstName or not selected_itemSecondName or not selected_itemSurname or not selected_itemGender or not selected_itemDateOfBirth:
                messagebox.showinfo("Ошибка", message="Одно из полей не введено")
            else:
                interactionWithTheDatabase = InteractionWithTheDatabase('localhost', 'main', 5432, "postgres", '123')
                interactionWithTheDatabase.connectionToDatabase()
                interactionWithTheDatabase.changePerson(selected_itemFirstName, selected_itemSecondName, selected_itemGender, selected_itemSurname, selected_itemDateOfBirth, person_id)
                interactionWithTheDatabase.closeConnection()
                
                messagebox.showinfo("Успех", message="Пользователь успешно изменен")
                self.userTable.tableOutput()

        button = tk.Button(new_window, text="Сохранить изменение", command=change)
        button.place(relx=0.5, rely=0.9, anchor="center")

    def addUser(self):
        new_window = tk.Toplevel()
        new_window.geometry('350x200')
        new_window.title("Отдельное окно")

        titleEFirstName = tk.Label(new_window, text="Имя:", font='Times 10')
        titleEFirstName.place(relx=0, rely=0.07, anchor="w")

        titleESecondName = tk.Label(new_window, text="Фамилия:", font='Times 10')
        titleESecondName.place(relx=0, rely=0.23, anchor="w")

        titleEGender = tk.Label(new_window, text="Отчество:", font='Times 10')
        titleEGender.place(relx=0, rely=0.39, anchor="w")

        titleESurname = tk.Label(new_window, text="Пол:", font='Times 10')
        titleESurname.place(relx=0, rely=0.55, anchor="w")

        titleEDateOfBirth = tk.Label(new_window, text="Дата рождения:", font='Times 10')
        titleEDateOfBirth.place(relx=0, rely=0.71, anchor="w")

        eFirstName = tk.Entry(new_window)
        eFirstName.place(x=100, y=8, width=200)
        eSecondName = tk.Entry(new_window)
        eSecondName.place(x=100, y=40, width=200)
        eGender = tk.Entry(new_window)
        eGender.place(x=100, y=70, width=200)
        eSurname = tk.Entry(new_window)
        eSurname.place(x=100, y=102, width=200)
        eDateOfBirth = tk.Entry(new_window)
        eDateOfBirth.place(x=100, y=132, width=200)

        eFirstName.insert(0, "")
        eSecondName.insert(0, "")
        eSurname.insert(0, "")
        eGender.insert(0, "")
        eDateOfBirth.insert(0, "")

        def add():
            selected_itemFirstName = eFirstName.get().strip()
            selected_itemSecondName = eSecondName.get().strip()
            selected_itemSurname = eSurname.get().strip()
            selected_itemGender = eGender.get().strip()
            selected_itemDateOfBirth = eDateOfBirth.get().strip()

            if not selected_itemFirstName or not selected_itemSecondName or not selected_itemSurname or not selected_itemGender or not selected_itemDateOfBirth:
                messagebox.showinfo("Ошибка", message="Одно из полей не введено")
            else:
                interactionWithTheDatabase = InteractionWithTheDatabase('localhost', 'main', 5432, "postgres", '123')
                interactionWithTheDatabase.connectionToDatabase()
                interactionWithTheDatabase.addPerson(selected_itemFirstName, selected_itemSecondName, selected_itemSurname, selected_itemGender, selected_itemDateOfBirth)
                interactionWithTheDatabase.closeConnection()
                
                eFirstName.delete(0, tk.END)
                eSecondName.delete(0, tk.END)
                eSurname.delete(0, tk.END)
                eGender.delete(0, tk.END)
                eDateOfBirth.delete(0, tk.END)
                messagebox.showinfo("Успех", message="Пользователь успешно добавлен")
                self.userTable.tableOutput()

        button = tk.Button(new_window, text="Добавить", command=add)
        button.place(relx=0.5, rely=0.9, anchor="center")

    def addDocument(self):

        person_id = self.userTable.giveId()
        if person_id == None:
            messagebox.showinfo("Предупреждение", message="Перед изменением нужно выбрать пользователя")
            return

        new_window = tk.Toplevel()
        new_window.geometry('350x200')
        new_window.title("Отдельное окно")

        titleEDocumentationReferenceID = tk.Label(new_window, text="Тип документа:", font='Times 10')
        titleEDocumentationReferenceID.place(relx=0, rely=0.07, anchor="w")

        titleESerialNumber = tk.Label(new_window, text="Серия:", font='Times 10')
        titleESerialNumber.place(relx=0, rely=0.23, anchor="w")

        titleENumberPD = tk.Label(new_window, text="Номер:", font='Times 10')
        titleENumberPD.place(relx=0, rely=0.39, anchor="w")

        titleEDateOfIssue = tk.Label(new_window, text="Дата получения:", font='Times 10')
        titleEDateOfIssue.place(relx=0, rely=0.55, anchor="w")

        titleEIssuedByWhom = tk.Label(new_window, text="Кем выдан:", font='Times 10')
        titleEIssuedByWhom.place(relx=0, rely=0.71, anchor="w")

        eDocumentationReferenceID = tk.Entry(new_window)
        eDocumentationReferenceID.place(x=100, y=8, width=200)
        eSerialNumber = tk.Entry(new_window)
        eSerialNumber.place(x=100, y=40, width=200)
        eNumberPD = tk.Entry(new_window)
        eNumberPD.place(x=100, y=70, width=200)
        eDateOfIssue = tk.Entry(new_window)
        eDateOfIssue.place(x=100, y=102, width=200)
        eIssuedByWhom = tk.Entry(new_window)
        eIssuedByWhom.place(x=100, y=132, width=200)

        eDocumentationReferenceID.insert(0, "")
        eSerialNumber.insert(0, "")
        eNumberPD.insert(0, "")
        eDateOfIssue.insert(0, "")
        eIssuedByWhom.insert(0, "")

        interactionWithTheDatabase = InteractionWithTheDatabase('localhost', 'main', 5432, "postgres", '123')
        interactionWithTheDatabase.connectionToDatabase()
        typeOfDocuments = interactionWithTheDatabase.receivingAllTypesOfDocuments()
        
        languages = [item[1] for item in typeOfDocuments]
        languages_var = StringVar(new_window, value=typeOfDocuments[0][0])   
        languages_var.set(languages[0])
        label = ttk.Label(textvariable=languages_var)
        label.pack(anchor=NW, padx=6, pady=6)
        
        combobox = ttk.Combobox(textvariable=languages_var, values=languages)
        combobox.pack(anchor=NW, padx=6, pady=6)
                
        

        def add():

            selected_itemDocumentationReferenceID = combobox.get()


            # selected_itemDocumentationReferenceID = eDocumentationReferenceID.get().strip()
            selected_itemSerialNumber = eSerialNumber.get().strip()
            selected_itemNumberPD = eNumberPD.get().strip()
            selected_itemDateOfIssue = eDateOfIssue.get().strip()
            selected_itemIssuedByWhom = eIssuedByWhom.get().strip()

            if not selected_itemDocumentationReferenceID or not selected_itemSerialNumber or not selected_itemNumberPD or not selected_itemDateOfIssue or not selected_itemIssuedByWhom:
                messagebox.showinfo("Ошибка", message="Одно из полей не введено")
                interactionWithTheDatabase.closeConnection()
            else:
                
                
                interactionWithTheDatabase.addDocument(selected_itemDocumentationReferenceID, selected_itemSerialNumber, selected_itemNumberPD, selected_itemDateOfIssue, selected_itemIssuedByWhom, person_id)
                interactionWithTheDatabase.closeConnection()
                
                eDocumentationReferenceID.delete(0, tk.END)
                eSerialNumber.delete(0, tk.END)
                eNumberPD.delete(0, tk.END)
                eDateOfIssue.delete(0, tk.END)
                eIssuedByWhom.delete(0, tk.END)
                messagebox.showinfo("Успех", message="Документ успешно добавлен")
                self.userTable.tableOutput()

        button = tk.Button(new_window, text="Добавить", command=add)
        button.place(relx=0.5, rely=0.9, anchor="center")

    def deletionDocument():
        pass
    
    def changeDocument():
        pass

    def addPassport():
        pass

    def deletionPassport():
        pass

    def changePassport():
        pass

    def pressingAdd(self):
        button = tk.Button(self.root, text=self.text, command=self.addUser)
        button.place(relx=self.relx, rely=self.rely, anchor="center")

    def pressingDelete(self):
        button = tk.Button(self.root, text=self.text, command=self.deleteUser)
        button.place(relx=self.relx, rely=self.rely, anchor="center")
    
    def pressingСhange(self):   
        button = tk.Button(self.root, text=self.text, command=self.changeUser)
        button.place(relx=self.relx, rely=self.rely, anchor="center")
    
    def documentAdd(self):
        button = tk.Button(self.root, text=self.text, command=self.addDocument)
        button.place(relx=self.relx, rely=self.rely, anchor="center")
    
    def documentDeletion(self):
        button = tk.Button(self.root, text=self.text, command=self.deletionDocument)
        button.place(relx=self.relx, rely=self.rely, anchor="center")

    def documentChange(self):
        button = tk.Button(self.root, text=self.text, command=self.changeDocument)
        button.place(relx=self.relx, rely=self.rely, anchor="center")
    
    def passportAdd(self):
        button = tk.Button(self.root, text=self.text, command=self.addPassport)
        button.place(relx=self.relx, rely=self.rely, anchor="center")
    
    def passportDeletion(self):
        button = tk.Button(self.root, text=self.text, command=self.deletionPassport)
        button.place(relx=self.relx, rely=self.rely, anchor="center")

    def passportChange(self):
        button = tk.Button(self.root, text=self.text, command=self.changePassport)
        button.place(relx=self.relx, rely=self.rely, anchor="center")

