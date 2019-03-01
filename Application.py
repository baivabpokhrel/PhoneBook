
import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
from MainPage import *
from SignupPage import *
from LoginPage import *
from ProfilePage import *
import DatabaseManager


# Global Variables
window_dimensions = "600x600"
app_name = "Phone Book App"



class Application(tk.Tk):
    # Constructor
    def __init__(self):
        tk.Tk.__init__(self)      #super().__init__()
        # object variables
        self._phone= '0000000000'
        self.title(app_name)
        self.geometry(window_dimensions)
        self.resizable(0,0)
        self.title_font = font.Font(family='Courier', size=32, weight="bold", underline=True)
        self.footer_font = font.Font(family='Comic Sans MS', size=12, weight='bold',slant="italic")
        self.subheader_font = font.Font(family='Times', size=12, weight='bold',underline=True)
        # the container is where we'll stack a bunch of frames on top of each other, then the one we want visible
        # will be raised above the others
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand= True)
        self.container.grid_rowconfigure(0, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        self.page_array = {}

        # Classes array
        data = [MainPage,SignupPage,LoginPage]

        for page in data:
            page_name = page.__name__
            current_page = page(parent=self.container, controller=self)
            self.page_array[page_name] = current_page

            # put all of the pages in the same location; the one on the TOP of the stacking order --> visible.
            current_page.grid(row=0, column=0, sticky="nsew")

        self.show_frame("MainPage")

    def show_frame(self,page_name):
        frame = self.page_array[page_name]
        frame.tkraise()
    def signup(self,name,email,phone,password,confirm_password):
        if(name==''):
            messagebox.showwarning("Warning","Name Field is Empty")
        elif(email==''):
            messagebox.showwarning("Warning","Email Field is Empty")
        elif(phone==''):
            messagebox.showwarning("Warning","Phone Field is Empty")
        elif (not DatabaseManager.check_valid_phone(phone)):
            messagebox.showwarning("Warning","Incorrect format for phone number")
        elif(password==''):
            messagebox.showwarning("Warning","Password Field is Empty")
        elif(confirm_password==''):
                messagebox.showwarning("Warning","Confirm Password Field is Empty")
        elif password!=confirm_password:
            messagebox.showwarning("Warning","Please check!!\nPasswords do not Match")

        elif DatabaseManager.user_exists_check(phone):
            messagebox.showwarning("Warning","User with this phone number already Exists!!")
        else:
            DatabaseManager.insert_into(name,email,phone,password)
            frame = self.page_array["LoginPage"]
            frame.tkraise()

    def login(self,phone,password):
        if (DatabaseManager.login_check(phone,password)):
            self._phone=phone
            self.create_profile_page()
        else:
            messagebox.showwarning("Warning","Username or Password doesnt match")




    def get_phone(self):
        return self._phone

    def create_profile_page(self):
        page_name = ProfilePage.__name__
        profile = ProfilePage(parent=self.container, controller=self)
        self.page_array[page_name] = profile
        profile.grid(row=0, column=0, sticky="nsew")

def main():

    app = Application()
    app.mainloop()
    DatabaseManager.close_connection()


if __name__ == "__main__":
    main()
