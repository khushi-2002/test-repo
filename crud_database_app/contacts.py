from cProfile import label
from email.mime import application, image
from sqlite3 import Row
from tkinter import Tk, W, E, S, N, StringVar, END, Entry, Button, PhotoImage, Label, LabelFrame, Scrollbar, Toplevel
from tkinter import ttk # provide access to use the TK widgets


class contact:
    def __init__(self, root ):
        self.root=root # Stores the container of my application and can be accessible from anywhere
        self.create_left_logo() # calling the function for creating the logo
    
    # For displaying the logo
    def create_left_logo(self):
        photo = PhotoImage(file= 'icons/contacts_logo.gif') 
        label = Label(image= photo)
        label.image = photo
        label.grid(row=0, column=0)
           

if __name__ == '__main__': # starts the execution from here
    root = Tk() # creates an application window
    root.title('My contacts List') # gives the title to the window
    app = contact(root) # For creating the instant
    root.mainloop() # run the application
    
    
            