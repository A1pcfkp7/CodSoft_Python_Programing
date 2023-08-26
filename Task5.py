import tkinter as tk
from tkinter import messagebox

class ContactBookApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Contact Book")
        
        self.contacts = []
        
        self.name_var = tk.StringVar()
        self.phone_var = tk.StringVar()
        self.email_var = tk.StringVar()
        self.address_var = tk.StringVar()
        
        self.create_ui()

    def create_ui(self):
        tk.Label(self.root, text="Contact Book", font=("Helvetica", 16)).pack(pady=10)

        tk.Label(self.root, text="Name:").pack()
        tk.Entry(self.root, textvariable=self.name_var).pack()

        tk.Label(self.root, text="Phone:").pack()
        tk.Entry(self.root, textvariable=self.phone_var).pack()

        tk.Label(self.root, text="Email:").pack()
        tk.Entry(self.root, textvariable=self.email_var).pack()

        tk.Label(self.root, text="Address:").pack()
        tk.Entry(self.root, textvariable=self.address_var).pack()

        tk.Button(self.root, text="Add Contact", command=self.add_contact).pack(pady=10)
        tk.Button(self.root, text="View Contacts", command=self.view_contacts).pack(pady=5)
        tk.Button(self.root, text="Search Contact", command=self.search_contact).pack(pady=5)
        tk.Button(self.root, text="Update Contact", command=self.update_contact).pack(pady=5)
        tk.Button(self.root, text="Delete Contact", command=self.delete_contact).pack(pady=5)

    def add_contact(self):
        name = self.name_var.get()
        phone = self.phone_var.get()
        email = self.email_var.get()
        address = self.address_var.get()

        self.contacts.append({"Name": name, "Phone": phone, "Email": email, "Address": address})
        self.clear_entries()
        messagebox.showinfo("Success", "Contact added successfully.")

    def view_contacts(self):
        if self.contacts:
            contacts_text = "\n".join([f"Name: {contact['Name']}, Phone: {contact['Phone']}" for contact in self.contacts])
            messagebox.showinfo("Contacts", contacts_text)
        else:
            messagebox.showinfo("Contacts", "No contacts available.")

    def search_contact(self):
        keyword = self.name_var.get()
        found_contacts = [contact for contact in self.contacts if keyword in contact["Name"] or keyword in contact["Phone"]]
        if found_contacts:
            contacts_text = "\n".join([f"Name: {contact['Name']}, Phone: {contact['Phone']}" for contact in found_contacts])
            messagebox.showinfo("Search Results", contacts_text)
        else:
            messagebox.showinfo("Search Results", "No matching contacts found.")

    def update_contact(self):
        # To be implemented
        pass

    def delete_contact(self):
        # To be implemented
        pass

    def clear_entries(self):
        self.name_var.set("")
        self.phone_var.set("")
        self.email_var.set("")
        self.address_var.set()

if __name__ == "__main__":
    root = tk.Tk()
    app = ContactBookApp(root)
    root.mainloop()
