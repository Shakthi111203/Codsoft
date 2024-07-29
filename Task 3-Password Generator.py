import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password(event=None):
    try:
        length = int(length_entry.get("1.0", tk.END).strip())
        if length <= 0:
            raise ValueError("Length must be greater than 0")
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for i in range(length))
        password_entry.delete("1.0", tk.END)
        password_entry.insert("1.0", password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Password Generator")
root.geometry("400x300") 
root.configure(bg='#F2C2C2')

title_label = tk.Label(root, text="Password Generator", font=('helvetica', 16, 'bold', 'underline'), bg='#F2C2C2')
title_label.pack(pady=10) 

length_frame = tk.Frame(root, bg='#F2C2C2')
length_frame.pack(pady=10)

length_label = tk.Label(length_frame, text="Length:", font=('helvetica', 13, 'bold'), bg='#F2C2C2')  
length_label.pack(side=tk.LEFT, padx=5)  

length_entry = tk.Text(length_frame, width=20, height=1, font=('helvetica', 13, 'bold')) 
length_entry.pack(side=tk.LEFT, padx=5) 

length_entry.bind('<Return>', generate_password)

generate_button = tk.Button(root, text="Generate Password", command=generate_password, bg='lightblue')  
generate_button.pack(pady=5) 

password_label = tk.Label(root, text="Generated Password:",pady=5, font=('helvetica', 13, 'bold'), bg='#F2C2C2') 
password_label.pack(pady=10)  

password_entry = tk.Text(root, width=30, height=2.5, pady=5, font=('helvetica', 13, 'bold')) 
password_entry.pack(pady=3)

root.mainloop()
