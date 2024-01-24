import tkinter as tk
from tkinter import *
from td_backend import insert_task, remove_task, view_tasks
import customtkinter as ctk
from CTkListbox import *

ctk.set_appearance_mode("dark")  # Set a modern dark theme (optional)

class toDo():
    def __init__(self):
        self.window = ctk.CTk()  # Use CustomTkinter's main window

        self.window.geometry("400x300")  # Adjust window size
        self.window.title("To-do list")

        # Labels
        self.l1 = ctk.CTkLabel(self.window, text="Task", font=("Roboto Medium", 14))  # Modern font
        self.l1.grid(row=0, column=0, padx=10, pady=10)  # Add padding for spacing

        self.l2 = ctk.CTkLabel(self.window, text="Date", font=("Roboto Medium", 14))
        self.l2.grid(row=0, column=3, padx=10, pady=10)

        # Entries
        self.task_text = StringVar()
        self.e1 = ctk.CTkEntry(self.window, textvariable=self.task_text, width=25)  # Wider entry
        self.e1.grid(row=0, column=2, padx=10, pady=10)

        self.date_text = StringVar()
        self.e2 = ctk.CTkEntry(self.window, textvariable=self.date_text, width=15)
        self.e2.grid(row=0, column=4, padx=10, pady=10)

        # Listbox & Scrollbar
        self.list1 = CTkListbox(self.window, height=6, width=35, font=("Roboto Normal", 12))
        self.list1.grid(row=1, column=0, rowspan=7, columnspan=7, padx=10, pady=10)

        self.sb1 = ctk.CTkScrollbar(self.window)
        self.sb1.grid(row=2, column=7, rowspan=7, sticky="ns")  # Configure scrollbar position

       # self.list1.configure(yscrollcommand=self.sb1.set)
       # self.sb1.configure(command=self.list1.yview)

        # Buttons
        self.b1 = ctk.CTkButton(self.window, text="Add", width=100,
                                command=lambda:[self.add_task(), self.delete_entries()])
        self.b1.grid(row=0, column=5, padx=10, pady=10)

        self.b2 = ctk.CTkButton(self.window, text="Delete", width=100, command=self.delete_task)
        self.b2.grid(row=0, column=6, padx=10, pady=10)

        self.view_tasks()

    def add_task(self):
        addT = self.e1.get()
        addD = self.e2.get()
        tasks = view_tasks()
        insert_task(addT, addD)
        self.list1.delete(0,END)
        for task in tasks:
            self.list1.insert(END, f"Task: {task['task']} - Date: {task['date']}")
        

    def delete_entries(self):
        self.e1.delete(0,END)
        self.e2.delete(0,END)

    def delete_task(self):
        remove_task()
        self.list1.delete(END)
    
    def view_tasks(self):
        tasks = view_tasks()
        self.list1.delete(0, END)
        for task in tasks:
            self.list1.insert(END, f"Task: {task['task']} - Date: {task['date']}")
    

    

    def pushtostart(self):
        self.window.mainloop()

if __name__ == "__main__":
    todo = toDo()
    todo.pushtostart()
