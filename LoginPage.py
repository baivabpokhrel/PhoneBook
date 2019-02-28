
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox

class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        
        
        self.controller = controller
        tk.Frame.__init__(self, parent)

        # Labels
        label_type = tk.Label(self, text="® CopyRight Phonebook 2018", fg = "gray",font=controller.footer_font)
        label1 = tk.Label(self, text="PhoneBook'ed")
        label1.config(font=("Courier", 35, 'bold'))
        label_phone = Label(self, text="Phone")
        label_password = Label(self, text="Password")
        
        
        
        # Entries
        entry_phone = Entry(self)
        entry_password = Entry(self,show='*')
    
    
        # Button
        button_home = tk.Button(self, text="Home",command=lambda: controller.show_frame("MainPage"))
        button_login = tk.Button(self, text="Log In",command=lambda: self.login(entry_phone,entry_password))
    
        
        n = 150
        m = 50
        label_type.pack(side=BOTTOM)
        label1.pack(side=TOP,ipady=20)
        label_phone.place(x=n,y=m*3)
        label_password.place(x=n,y=m*4)
        entry_phone.place(x=n+75,y=m*3)
        entry_password.place(x=n+75,y=m*4)
        button_home.place(x=225,y=300)
        button_login.place(x=325,y=300)
    def login(self,phone_entry, password_entry):
        # to check if correct details given
        self.controller.login(phone_entry.get(),password_entry.get())

