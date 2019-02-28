import tkinter as tk
from tkinter import *
from tkinter import font
from tkinter import messagebox
from Database.py import *


# Global Variables
window_dimensions = "600x600"
app_name = "Phone Book App"



class Application(tk.Tk):
    # Constructor
    def __init__(self):
        tk.Tk.__init__(self)      #super().__init__()
# object variables
        self._name = "admin"
        self.email = StringVar()
        self.phoneNumber = StringVar()
        self.currentAddress = StringVar()
        self.DOB = StringVar()
        self.password= StringVar()
        self.confirmPassword= StringVar()
        self.title(app_name)
        self.geometry(window_dimensions)
        self.resizable(0,0)
        self.title_font = font.Font(family='Courier', size=32, weight="bold", underline=True)
        self.footer_font = font.Font(family='Comic Sans MS', size=12, weight='bold',slant="italic")
        self.subheader_font = font.Font(family='Times', size=12, weight='bold',underline=True)
        # the container is where we'll stack a bunch of frames on top of each other, then the one we want visible
        # will be raised above the others
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand= True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.page_array = {}
    
        # Classes array
        data = [MainPage,SignupPage,LoginPage, ProfilePage]
    
        for page in data:
            page_name = page.__name__
            current_page = page(parent=container, controller=self)
            self.page_array[page_name] = current_page
            
            # put all of the pages in the same location; the one on the TOP of the stacking order --> visible.
            current_page.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame("MainPage")
    
    def show_frame(self,page_name):
        frame = self.page_array[page_name]
        frame.tkraise()
    def sign_up(self,username,password,confirm_password):
        if(password.get()==confirm_password.get()):
            # TODO: need to check if name already exists
            frame = self.page_array["LoginPage"]
            frame.tkraise()
        else:
            messagebox.showwarning("Warning","Please check!!\nPasswords do not Match")
    def login(self,username):
        # TODO: need to check username and passoword match in DB
        # TODO : need to check if no such name exists in DB
        
            #print("username is:",username.get())
        self._name=username
        frame = self.page_array["ProfilePage"]
        frame.tkraise()
    
    def get_name(self):
        return self._name





class MainPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
#         img = controller.image()

        # Widget Creation
        # panel = tk.Label(self, image = img) 
        # Labels
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
        
        
        entry_password = Entry(self, textvariable=controller.password,show='*')
        entry_confirm_password = Entry(self, textvariable=controller.confirmPassword,show='*')
        
        
        
        # Button
        #controller.show_frame("MainPage")
        button_home = tk.Button(self, text="Home",command=lambda:controller.show_frame("MainPage"))
            #if(not(entry6.get()==entry7.get())):
        
    
        button_sign_up = tk.Button(self, text="Sign Up",command=lambda: controller.sign_up(entry_username,entry_password,entry_confirm_password))
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



class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Labels
        label_type = tk.Label(self, text="® CopyRight Phonebook 2018", fg = "gray",font=controller.footer_font)
        label1 = tk.Label(self, text="PhoneBook'ed")
        label1.config(font=("Courier", 35, 'bold'))
        label_username = Label(self, text="Username")
        label_password = Label(self, text="Password")
        
        
        
        # Entries
        entry_username = Entry(self)
        entry_password = Entry(self,show='*')
    
    
        # Button
        button_home = tk.Button(self, text="Home",command=lambda: controller.show_frame("MainPage"))
        button_login = tk.Button(self, text="Log In",command=lambda: self.login(entry_username,entry_password))
    
        
        n = 150
        m = 50
        label_type.pack(side=BOTTOM)
        label1.pack(side=TOP,ipady=20)
        label_username.place(x=n,y=m*3)
        label_password.place(x=n,y=m*4)
        entry_username.place(x=n+75,y=m*3)
        entry_password.place(x=n+75,y=m*4)
        button_home.place(x=225,y=300)
        button_login.place(x=325,y=300)
    def login(self,name_entry, password_entry):
        # TODO : need to check if account already exists or any detail
        self.controller.login(name_entry.get())


class ProfilePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        # Labels
        label_type = tk.Label(self, text="® CopyRight Phonebook 2018", fg = "gray",font=controller.footer_font)
        
        label1 = tk.Label(self, text="PhoneBook'ed")
        label1.config(font=("Courier", 35, 'bold'))
        
        #print("name is", controller.get_name())
        label_name= tk.Label(self, text=controller.get_name())



        n = 150
        m = 50
        label_type.pack(side=BOTTOM)
        label1.pack(side=TOP,ipady=20)
        label_name.place(x=150,y=150)

def main():
    #print("Phonebook App\n")
    app = Application()
    app.mainloop()


if __name__ == "__main__":
    main()



