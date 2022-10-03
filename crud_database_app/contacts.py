from cProfile import label
from email.mime import application, image
from sqlite3 import Row
from tkinter import Tk, W, E, S, N, StringVar, END, Entry, Button, PhotoImage, Label, LabelFrame, Scrollbar, Toplevel
from tkinter import ttk # provide access to use the TK widgets


class contact:
    

    def __init__(self, root ):
        self.root=root # Stores the container of my application and can be accessible from anywhere
        self.create_left_logo() # calling the function for creating the logo
        self.create_label_frame() #calling the function for creating the frame
        self.create_message_area()
        self.create_tree_view()
        ttk.style = ttk.Style()
        ttk.style.configure("Treeview", font=('helvetica',10))
        ttk.style.configure("Treeview.Heading", font=('helvetica',12, 'bold'))
    
    # For displaying the logo
    def create_left_logo(self):
        photo = PhotoImage(file= 'icons/contacts_logo.gif') 
        label = Label(image= photo) #stores the image inside a container
        label.image = photo #display the photo
        label.grid(row=0, column=0) #For positioning of the label (container where image is stored)
    
    # For displaying the labelframe, label, entry fields and button
    
    def create_label_frame(self):
        labelFrame= LabelFrame(self.root, text="Create New Contact", bg="sky blue", font="helvetica 10")
        labelFrame.grid(row=0, column=1, padx=8, pady=8, sticky='ew')
        Label(labelFrame, text='Name:', bg="green", fg="white").grid(row=1, column=1, sticky=W, pady=2, padx=15)
        self.namefield= Entry(labelFrame)
        self.namefield.grid(row=1, column=2, sticky=W, padx=5, pady=2)
        Label(labelFrame, text='Email:', bg="brown", fg="white").grid(row=2, column=1, sticky=W, pady=2, padx=15)
        self.emailfield= Entry(labelFrame)
        self.emailfield.grid(row=2,column=2,sticky=W,padx=5,pady=2)
        Label(labelFrame, text='Number:', bg="black", fg="white").grid(row=3, column=1, sticky=W, pady=2, padx=15)
        self.numfield= Entry(labelFrame)
        self.numfield.grid(row=3,column=2,sticky=W,padx=5,pady=2)
        Button(labelFrame, text="Add Contact", command="", bg="blue",fg="white").grid(row=4, column=2,sticky=E, padx=5, pady=5)
        
    # For displaying the message after performing any operations on the data
    
    def create_message_area(self):
        self.message= Label(text="", fg="red")
        self.message.grid(row=3,column=1, sticky=W)
    
    
    # For creating the tree view for displaying the data
    
    def create_tree_view(self):
        self.tree= ttk.Treeview(height=10, columns=("email", "number")) # ttk also having widgets like button
        self.tree.grid(row=6, column=0, columnspan=3) #position
        self.tree.heading('#0', text='Name', anchor=W) 
        self.tree.heading('email', text='Email Address', anchor=W)
        self.tree.heading('number', text='Contact Number', anchor=W)
        
    
    # For creating the scroll bar
    def create_scrollbar(self):
        self.scrollbar= Scrollbar(orient='vertical', command=self.tree.yview)
        self.scrollbar.grid(row=6, column=3, rowspan=10, sticky="sn")
            
                
 # First parameter defines the position it gonna be placed!       
if __name__ == '__main__': # starts the execution from here and executes the code underneth
    root = Tk() # creates an application window
    root.title('My contact List') # gives the title to the window
    app = contact(root) # For creating the instant
    root.mainloop() # run the application until we exit the application
    
    
            