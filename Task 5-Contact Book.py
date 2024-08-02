import tkinter as tk
from tkinter import messagebox, ttk

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        self.contacts = []

        self.create_ui()

    def create_ui(self):
        self.title_label = tk.Label(self.root, text="Contact Book", font=("Arial", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.input_frame = tk.Frame(self.root)
        self.input_frame.grid(row=1, column=0, padx=10, pady=50, sticky="n")

        tk.Label(self.input_frame, text="Name").grid(row=0, column=0, pady=5)
        self.name_entry = tk.Entry(self.input_frame)
        self.name_entry.grid(row=0, column=1, pady=5)

        tk.Label(self.input_frame, text="Phone").grid(row=1, column=0, pady=5)
        self.phone_entry = tk.Entry(self.input_frame)
        self.phone_entry.grid(row=1, column=1, pady=5)

        tk.Label(self.input_frame, text="Email").grid(row=2, column=0, pady=5)
        self.email_entry = tk.Entry(self.input_frame)
        self.email_entry.grid(row=2, column=1, pady=5)

        tk.Label(self.input_frame, text="Address").grid(row=3, column=0, pady=5)
        self.address_entry = tk.Entry(self.input_frame)
        self.address_entry.grid(row=3, column=1, pady=5)

        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=2, column=0, pady=10, columnspan=2)

        self.add_button = tk.Button(self.button_frame, text="Add Contact", command=self.add_contact, bg="grey", fg="white")
        self.add_button.grid(row=0, column=0, padx=5, pady=10)

        self.search_button = tk.Button(self.button_frame, text="Search Contact", command=self.search_contact, bg="grey", fg="white")
        self.search_button.grid(row=0, column=1, padx=5, pady=10)

        self.update_button = tk.Button(self.button_frame, text="Update Contact", command=self.update_contact, bg="grey", fg="white")
        self.update_button.grid(row=0, column=2, padx=5, pady=10)

        self.delete_button = tk.Button(self.button_frame, text="Delete Contact", command=self.delete_contact, bg="grey", fg="white")
        self.delete_button.grid(row=0, column=3, padx=5, pady=10)

        self.table_frame = tk.Frame(self.root)
        self.table_frame.grid(row=1, column=1, padx=10, pady=10, sticky="n")

        self.tree = ttk.Treeview(self.table_frame, columns=("Name", "Phone", "Email", "Address"), show="headings")
        self.tree.heading("Name", text="Name")
        self.tree.heading("Phone", text="Phone")
        self.tree.heading("Email", text="Email")
        self.tree.heading("Address", text="Address")
        self.tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(self.table_frame, orient=tk.VERTICAL, command=self.tree.yview)
        self.tree.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        address = self.address_entry.get()

        if name and phone:
            self.contacts.append({"name": name, "phone": phone, "email": email, "address": address})
            self.refresh_contacts()
            self.clear_entries()

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
        self.address_entry.delete(0, tk.END)

    def search_contact(self):
        query = self.name_entry.get() or self.phone_entry.get()
        if query:
            results = [c for c in self.contacts if query.lower() in c["name"].lower() or query in c["phone"]]
            if results:
                self.tree.delete(*self.tree.get_children())
                for c in results:
                    self.tree.insert("", tk.END, values=(c["name"], c["phone"], c["email"], c["address"]))
            else:
                messagebox.showinfo("Search Results", "No contacts found.")
        else:
            messagebox.showwarning("Warning", "Please enter a name or phone number to search.")

    def update_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            contact_values = item['values']
            name, phone, email, address = contact_values[0], contact_values[1], contact_values[2], contact_values[3]

            for c in self.contacts:
                if c["name"] == name and c["phone"] == phone and c["email"] == email and c["address"] == address:
                    new_name = self.name_entry.get() or c["name"]
                    new_phone = self.phone_entry.get() or c["phone"]
                    new_email = self.email_entry.get() or c["email"]
                    new_address = self.address_entry.get() or c["address"]

                    if new_name and new_phone:
                        c["name"] = new_name
                        c["phone"] = new_phone
                        c["email"] = new_email
                        c["address"] = new_address
                        self.refresh_contacts()
                        self.clear_entries()
                    break
        else:
            messagebox.showwarning("Warning", "Please select a contact to update.")

    def delete_contact(self):
        selected_item = self.tree.selection()
        if selected_item:
            item = self.tree.item(selected_item)
            contact_values = item['values']
            name, phone, email, address = contact_values[0], contact_values[1], contact_values[2], contact_values[3]

            self.contacts = [c for c in self.contacts if not (c["name"] == name and c["phone"] == phone and c["email"] == email and c["address"] == address)]
            self.refresh_contacts()
        else:
            messagebox.showwarning("Warning", "Please select a contact to delete.")

    def refresh_contacts(self):
        self.tree.delete(*self.tree.get_children())
        for c in self.contacts:
            self.tree.insert("", tk.END, values=(c["name"], c["phone"], c["email"], c["address"]))

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
