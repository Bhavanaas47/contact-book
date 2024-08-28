import tkinter as tk
from tkinter import messagebox


class ContactBook:
    def __init__(self, master):
        self.master = master
        master.title("Contact Book")

        self.contacts = {}

        # Set background color for the main window
        master.configure(bg="#e0f7fa")

        # Create GUI elements with color design
        self.name_label = tk.Label(master, text="Name", bg="#e0f7fa", fg="#00796b")
        self.name_label.grid(row=0, column=0, padx=5, pady=5)

        self.phone_label = tk.Label(master, text="Phone", bg="#e0f7fa", fg="#00796b")
        self.phone_label.grid(row=1, column=0, padx=5, pady=5)

        self.email_label = tk.Label(master, text="Email", bg="#e0f7fa", fg="#00796b")
        self.email_label.grid(row=2, column=0, padx=5, pady=5)

        self.name_entry = tk.Entry(master, bg="#ffffff", fg="#00796b")
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)

        self.phone_entry = tk.Entry(master, bg="#ffffff", fg="#00796b")
        self.phone_entry.grid(row=1, column=1, padx=5, pady=5)

        self.email_entry = tk.Entry(master, bg="#ffffff", fg="#00796b")
        self.email_entry.grid(row=2, column=1, padx=5, pady=5)

        self.add_button = tk.Button(master, text="Add Contact", command=self.add_contact, bg="#4caf50", fg="#ffffff")
        self.add_button.grid(row=3, column=0, padx=5, pady=5)

        self.search_button = tk.Button(master, text="Search Contact", command=self.search_contact, bg="#2196f3",
                                       fg="#ffffff")
        self.search_button.grid(row=3, column=1, padx=5, pady=5)

        self.update_button = tk.Button(master, text="Update Contact", command=self.update_contact, bg="#ff9800",
                                       fg="#ffffff")
        self.update_button.grid(row=4, column=0, padx=5, pady=5)

        self.delete_button = tk.Button(master, text="Delete Contact", command=self.delete_contact, bg="#f44336",
                                       fg="#ffffff")
        self.delete_button.grid(row=4, column=1, padx=5, pady=5)

        self.list_button = tk.Button(master, text="List Contacts", command=self.list_contacts, bg="#9c27b0",
                                     fg="#ffffff")
        self.list_button.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

        self.contacts_list = tk.Text(master, height=10, width=50, bg="#ffffff", fg="#00796b")
        self.contacts_list.grid(row=6, column=0, columnspan=2, padx=5, pady=5)

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        # Check if the email is a Gmail address
        if not email.endswith("@gmail.com"):
            messagebox.showinfo("Error", "Only Gmail addresses are allowed.")
            return

        if name in self.contacts:
            messagebox.showinfo("Error", "Contact with this name already exists.")
        else:
            self.contacts[name] = {"phone": phone, "email": email}
            messagebox.showinfo("Success", f"Contact {name} added.")
            self.clear_entries()

    def search_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            info = self.contacts[name]
            self.phone_entry.delete(0, tk.END)
            self.phone_entry.insert(0, info['phone'])
            self.email_entry.delete(0, tk.END)
            self.email_entry.insert(0, info['email'])
        else:
            messagebox.showinfo("Error", "Contact not found.")

    def update_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()

        # Check if the email is a Gmail address
        if not email.endswith("@gmail.com"):
            messagebox.showinfo("Error", "Only Gmail addresses are allowed.")
            return

        if name in self.contacts:
            self.contacts[name] = {"phone": phone, "email": email}
            messagebox.showinfo("Success", f"Contact {name} updated.")
            self.clear_entries()
        else:
            messagebox.showinfo("Error", "Contact not found.")

    def delete_contact(self):
        name = self.name_entry.get()
        if name in self.contacts:
            del self.contacts[name]
            messagebox.showinfo("Success", f"Contact {name} deleted.")
            self.clear_entries()
        else:
            messagebox.showinfo("Error", "Contact not found.")

    def list_contacts(self):
        self.contacts_list.delete(1.0, tk.END)
        if self.contacts:
            for name, info in self.contacts.items():
                self.contacts_list.insert(tk.END, f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}\n")
        else:
            self.contacts_list.insert(tk.END, "No contacts found.")

    def clear_entries(self):
        self.name_entry.delete(0, tk.END)
        self.phone_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)


if __name__ == "__main__":
    root = tk.Tk()
    contact_book = ContactBook(root)
    root.mainloop()
