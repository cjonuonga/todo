import tkinter as tk
from tkinter import *
from td_backend import *

class toDo():
    def __init__(self):
        self.window = Tk()

        self.window.wm_title("To-do list")
        


        # Labels
        self.l1 = Label(self.window, text = "Task")
        self.l1.grid(row=0, column=0)

        self.l2 = Label(self.window, text = "Date")
        self.l2.grid(row=0, column=3)


        # Entries
        self.entry_text = StringVar()
        self.e1 = Entry(self.window, textvariable=self.entry_text)
        self.e1.grid(row=0, column=2)

        self.date_text = StringVar()
        self.e2 = Entry(self.window, textvariable=self.date_text)
        self.e2.grid(row=0, column=4)
        
        # Listbox & Scrollbar
        self.list1 = Listbox(self.window, height=6, width=35)
        self.list1.grid(row=1, column=0, rowspan=7, columnspan=7)

        self.sb1 = Scrollbar(self.window)
        self.sb1.grid(row=2, column=7, rowspan=7)

        self.list1.configure(yscrollcommand=self.sb1.set) # sets scrollbar to take control of the listbox
        self.sb1.configure(command=self.list1.yview) # moves screen up and down within the listbox
        
        # Buttons
        self.b1 = Button(self.window, text="Add", width=5, command=self.add_task)
        self.b1.grid(row=0, column=5)

        self.b2 = Button(self.window, text="Delete", width=5, command=self.delete_task)
        self.b2.grid(row=0, column=6)

        self.b3 = Button(self.window, text="view",width=5)
        self.b3.grid(row=0, column=7)


    def add_task(self):
        addT = self.e1.get()
        addD = self.e2.get()
        insert_task(addT, addD)

    def delete_task(self):
        remove_task()


    def pushtostart(self):
        self.window.mainloop()

if __name__ == "__main__":
    todo = toDo()
    todo.pushtostart()
