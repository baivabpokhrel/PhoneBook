import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox


class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        self.phone=controller.get_phone()
        
        self.controller = controller
        tk.Frame.__init__(self, parent)
        
        # Labels
        label_type = tk.Label(self, text="® CopyRight Phonebook 2018", fg = "gray",font=controller.footer_font)
        
        label1 = tk.Label(self, text="PhoneBook'ed")
        label1.config(font=("Courier", 35, 'bold'))
        
        print("phone again is", self.phone)
        label_name= tk.Label(self, text="Hey")



        n = 150
        m = 50
        label_type.pack(side=BOTTOM)
        label1.pack(side=TOP,ipady=20)
        label_name.place(x=150,y=150)