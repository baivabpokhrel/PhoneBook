import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
import DatabaseManager


class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        self.phone=controller.get_phone()

        self.controller = controller
        tk.Frame.__init__(self, parent)

        # Labels
        label_type = tk.Label(self, text="® CopyRight Phonebook 2018", fg = "gray",font=controller.footer_font)

        label1 = tk.Label(self, text="PhoneBook'ed")
        label1.config(font=("Courier", 35, 'bold'))
        display= 'Welcome Back ' + DatabaseManager.get_name(self.phone)

        label_name= tk.Label(self, text=display)

        button_home = tk.Button(self, text="Home",command=lambda: controller.show_frame("MainPage"))




        n = 150
        m = 50
        label_type.pack(side=BOTTOM)
        label1.pack(side=TOP,ipady=20)
        label_name.place(x=n,y=n+50)
        button_home.place(x=n+50,y=m+150)
