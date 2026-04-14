import tkinter as tk
from tkinter import messagebox

contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Error", "All fields are required")
    else:
        contacts[name] = phone
        messagebox.showinfo("Success", "Contact Added")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)

def view_contacts():
    text_area.delete("1.0", tk.END)
    for name, phone in contacts.items():
        text_area.insert(tk.END, f"{name} : {phone}\n")

def search_contact():
    name = name_entry.get()
    if name in contacts:
        messagebox.showinfo("Found", f"{name}: {contacts[name]}")
    else:
        messagebox.showwarning("Not Found", "Contact not found")

def delete_contact():
    name = name_entry.get()
    if name in contacts:
        del contacts[name]
        messagebox.showinfo("Deleted", "Contact deleted")
    else:
        messagebox.showwarning("Error", "Contact not found")


root = tk.Tk()
root.title("Contact Manager")
root.geometry("450x500")
root.config(bg="#f0f8ff")  


title = tk.Label(root, text="📞 Contact Manager", font=("Arial", 18, "bold"), bg="#4682b4", fg="white", pady=10)
title.pack(fill="x")


frame = tk.Frame(root, bg="#f0f8ff")
frame.pack(pady=20)

tk.Label(frame, text="Name", font=("Arial", 12), bg="#f0f8ff").grid(row=0, column=0, padx=10, pady=5)
name_entry = tk.Entry(frame, font=("Arial", 12), width=25)
name_entry.grid(row=0, column=1, pady=5)

tk.Label(frame, text="Phone", font=("Arial", 12), bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=5)
phone_entry = tk.Entry(frame, font=("Arial", 12), width=25)
phone_entry.grid(row=1, column=1, pady=5)


btn_frame = tk.Frame(root, bg="#f0f8ff")
btn_frame.pack(pady=10)

tk.Button(btn_frame, text="Add", width=12, bg="#4CAF50", fg="white", command=add_contact).grid(row=0, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="View", width=12, bg="#2196F3", fg="white", command=view_contacts).grid(row=0, column=1, padx=5, pady=5)
tk.Button(btn_frame, text="Search", width=12, bg="#E5FF00", fg="white", command=search_contact).grid(row=1, column=0, padx=5, pady=5)
tk.Button(btn_frame, text="Delete", width=12, bg="#f44336", fg="white", command=delete_contact).grid(row=1, column=1, padx=5, pady=5)


text_area = tk.Text(root, height=10, width=40, font=("Arial", 11))
text_area.pack(pady=15)


root.mainloop()