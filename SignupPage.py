
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox


class SignupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        
        # Labels
        label_type = tk.Label(self, text="® CopyRight Phonebook 2018", fg = "gray",font=controller.footer_font)
        label1 = tk.Label(self, text="PhoneBook'ed")
        label1.config(font=("Courier", 35, 'bold'))
        label_username = tk.Label(self, text="Name")
        label_email = tk.Label(self, text="Email")
        label_phone = tk.Label(self, text="Phone Number")
        
        
        label_password = tk.Label(self, text="Password")
        label_confirm_password = tk.Label(self, text="Confirm Password")
        
        
        # Entries
        entry_username = Entry(self)
        entry_email = Entry(self)
        entry_phone = Entry(self)
        
        
        entry_password = Entry(self ,show='*')
        entry_confirm_password = Entry(self,show='*')
        
        
        
        # Button
        #controller.show_frame("MainPage")
        button_home = tk.Button(self, text="Home",command=lambda:controller.show_frame("MainPage"))
            #if(not(entry6.get()==entry7.get())):
        
    
        button_sign_up = tk.Button(self, text="Sign Up",command=lambda: slef.signup(entry_phone,entry_password,entry_confirm_password))
        button_login = tk.Button(self, text="Log In",command=lambda: controller.show_frame("LoginPage"))
        button_exit= tk.Button(self, text="Exit",command=lambda: controller.destroy())
        
        n = 150
        m = 25
        label_type.pack(side = BOTTOM)
        label1.pack(side=TOP,ipady=20)
        label_username.place(x=n, y=m*5)
        label_email.place(x=n, y=m*7)
        label_phone.place(x=n, y=m*9)
        
        
        label_password.place(x=n, y=m*11)
        label_confirm_password.place(x=n, y=m*13)
        entry_username.place(x=n+125, y=m*5)
        entry_email.place(x=n+125, y=m*7)
        entry_phone.place(x=n+125, y=m*9)
        
        
        entry_password.place(x=n+125, y=m*11)
        entry_confirm_password.place(x=n+125, y=m*13)
        button_home.place(x=150,y=400)
        button_sign_up.place(x=250,y=400)
        button_login.place(x=350,y=400)
        button_exit.place(x=450,y=400)
    def singup(self,phone_entry, password_entry,confirm_password_entry):
        # to check if correct account exists and two password match
        self.controller.signup(phone_entry.get(),password_entry.get(),confirm_password_entry.get())

