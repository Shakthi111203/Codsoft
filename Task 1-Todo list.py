import tkinter as tk
from tkinter import messagebox
import json

tasks = []

def add_task():
    name = entry_name.get()
    if name:
        tasks.append({"name": name, "completed": False})
        update_task_list()
        entry_name.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task name is required.")

def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for i, task in enumerate(tasks):
        status = "Completed" if task["completed"] else "Pending"
        listbox_tasks.insert(tk.END, f"{i + 1}. {task['name']} - {status}")

def mark_completed():
    try:
        index = listbox_tasks.curselection()[0]
        tasks[index]["completed"] = not tasks[index]["completed"]
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Select a task to mark completed.")

def delete_task():
    try:
        index = listbox_tasks.curselection()[0]
        tasks.pop(index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "Select a task to delete.")

def load_tasks():
    global tasks
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
        update_task_list()
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

entry_name = tk.Entry(frame, width=30)
entry_name.grid(row=0, column=1, padx=20)

label_name = tk.Label(frame, text="Task Name:")
label_name.grid(row=0, column=0)

add_task_button = tk.Button(root, text="Add Task", command=add_task, bg='DodgerBlue', fg='White')
add_task_button.pack(pady=10)

listbox_tasks = tk.Listbox(root, width=50)
listbox_tasks.pack(pady=10,padx=10)

mark_completed_button = tk.Button(root, text="Mark Completed", command=mark_completed, bg='Green', fg='White')
mark_completed_button.pack(side=tk.LEFT, padx=20)

delete_task_button = tk.Button(root, text="Delete Task", command=delete_task, bg='Red', fg='White')
delete_task_button.pack(side=tk.RIGHT, padx=20)

load_tasks()

root.mainloop()
