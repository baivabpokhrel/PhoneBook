

import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox

class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
#         img = controller.image()

        # Widget Creation
        # panel = tk.Label(self, image = img) 
        # Labels
        self.controller = controller
        label_type = tk.Label(self, text="® CopyRight Phonebook 2018", fg = "gray",font=controller.footer_font)

        label1 = tk.Label(self, text="PhoneBook'ed")
        label1.config(font=("Courier", 45, 'bold'))
        label2 = tk.Label(self, text="Welcome to the App Let's Go!!\n\nSign up if a new user \n\n else Log in")
        label2.config(font=("Courier", 20))
        # Buttons
        button1 = tk.Button(self, text="Sign Up",command=lambda: controller.show_frame("SignupPage"))
        button2 = tk.Button(self, text="Log In",command=lambda: controller.show_frame("LoginPage"))
        
        n = 150
        m = 50
        
        
        label_type.pack(side=BOTTOM)
        label1.pack(side=TOP,ipady=100)
        label2.place(x=n-30,y=m*5)
        button1.place(x=n+110,y=m*8)
        button2.place(x=n+117,y=m*8.5)