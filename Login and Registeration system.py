import tkinter as tk
from tkinter import messagebox

users = {}


def register():
    username = reg_user.get()
    password = reg_pass.get()

    if username == "" or password == "":
        messagebox.showwarning("Error", "All fields are required")
    elif username in users:
        messagebox.showwarning("Error", "User already exists")
    else:
        users[username] = password
        messagebox.showinfo("Success", "Registered Successfully")
        reg_user.delete(0, tk.END)
        reg_pass.delete(0, tk.END)

def login():
    username = log_user.get()
    password = log_pass.get()

    if username in users and users[username] == password:
        messagebox.showinfo("Success", "Login Successful")
    else:
        messagebox.showerror("Error", "Invalid Credentials")


root = tk.Tk()
root.title("Modern Login System")
root.geometry("700x400")
root.config(bg="#f5f6fa")


tk.Label(root, text="🔐 Login System",
         font=("Arial", 20, "bold"),
         bg="#6c5ce7", fg="white", pady=10).pack(fill="x")


main = tk.Frame(root, bg="#f5f6fa")
main.pack(expand=True)


login_frame = tk.Frame(main, bg="white", bd=0, relief="solid")
login_frame.grid(row=0, column=0, padx=30, pady=30)

tk.Label(login_frame, text="Login",
         font=("Arial", 16, "bold"),
         bg="white").pack(pady=10)

tk.Label(login_frame, text="Username", bg="white").pack()
log_user = tk.Entry(login_frame, width=25, font=("Arial", 11))
log_user.pack(pady=5)

tk.Label(login_frame, text="Password", bg="white").pack()
log_pass = tk.Entry(login_frame, show="*", width=25, font=("Arial", 11))
log_pass.pack(pady=5)

tk.Button(login_frame, text="Login",
          bg="#0984e3", fg="white",
          width=20, command=login).pack(pady=15)


reg_frame = tk.Frame(main, bg="white", bd=0)
reg_frame.grid(row=0, column=1, padx=30, pady=30)

tk.Label(reg_frame, text="Register",
         font=("Arial", 16, "bold"),
         bg="white").pack(pady=10)

tk.Label(reg_frame, text="Username", bg="white").pack()
reg_user = tk.Entry(reg_frame, width=25, font=("Arial", 11))
reg_user.pack(pady=5)

tk.Label(reg_frame, text="Password", bg="white").pack()
reg_pass = tk.Entry(reg_frame, show="*", width=25, font=("Arial", 11))
reg_pass.pack(pady=5)

tk.Button(reg_frame, text="Register",
          bg="#00b894", fg="white",
          width=20, command=register).pack(pady=15)

root.mainloop()