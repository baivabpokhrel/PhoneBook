
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
        self._phone= "0000000000"
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
        data = [MainPage,SignupPage,LoginPage, ProfilePage]
        
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
    def signup(self,phone,password,confirm_password):
        if((password.get()==confirm_password.get()) and (DatabaseManager.user_exists(phone))):
            # TODO: need to check if name already exists
            frame = self.page_array["LoginPage"]
            frame.tkraise()
        else:
            messagebox.showwarning("Warning","Please check!!\nPasswords do not Match")
    def login(self,phone,password):
        # TODO: need to check username and passoword match in DB
        # TODO : need to check if no such name exists in DB
        
        
        frame = self.page_array["ProfilePage"]
        frame.tkraise()
        self._phone=phone
        print("phone is:",self.get_phone())
    
    def get_phone(self):
        return self._phone













def main():
    #print("Phonebook App\n")
    app = Application()
    app.mainloop()


if __name__ == "__main__":
    main()



