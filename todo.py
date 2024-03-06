import tkinter as tk
from tkinter import *
from td_backend import insert_task, remove_task, view_tasks



class toDo():
    def __init__(self):
        self.window = Tk()  # Use CustomTkinter's main window

        self.window.title("To-do list")

        # Labels
        self.l1 = Label(self.window, text="Task")  
        self.l1.grid(row=0, column=0)  

        self.l2 = Label(self.window, text="Date")
        self.l2.grid(row=0, column=3)

        # Entries
        self.task_text = StringVar()
        self.e1 = Entry(self.window, textvariable=self.task_text)
        self.e1.grid(row=0, column=2)

        self.date_text = StringVar()
        self.e2 = Entry(self.window, textvariable=self.date_text)
        self.e2.grid(row=0, column=4)

        # Listbox & Scrollbar
        self.list1 = Listbox(self.window, height=6, width=35)
        self.list1.grid(row=1, column=0, rowspan=7, columnspan=7)
        self.list1.insert(END, self.task_text, self.date_text)

        self.sb1 = Scrollbar(self.window)
        self.sb1.grid(row=2, column=7, rowspan=7)  # Configure scrollbar position

        self.list1.configure(yscrollcommand=self.sb1.set)
        self.sb1.configure(command=self.list1.yview)

        # Buttons
        self.b1 = Button(self.window, text="Add",
                                      command=lambda:[self.add_task(), self.delete_entries()],
                                      fg="black")
        
        self.b1.grid(row=0, column=5)

        self.b2 = Button(self.window, text="Delete", command=self.delete_task, fg="black")
        self.b2.grid(row=0, column=6)

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
        tasks = view_tasks
        if tasks:
            remove_task()
            self.list1.delete(END)
        else:
            print("No tasks to delete")
    
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
