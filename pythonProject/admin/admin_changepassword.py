import tkinter as tk
from tkinter import messagebox as msg
from connection import Connect


class AdminChangePassword:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Criminal Database || Admin Change Password")
        self.root.geometry("700x600")
        self.root.configure(bg="#263238")  # Dark blue-grey background

        # Define styles
        self.heading_style = {"font": ("Bahnschrift", 40, 'bold'), "bg": "#263238", "fg": "white"}
        self.label_style_email = {"font": ("Arial", 14, 'bold'), "fg": "black"}
        self.label_style_password = {"font": ("Arial", 14, 'bold'), "fg": "black"}
        self.entry_style = {"font": ("Arial", 12), "width": 32, "relief": tk.RIDGE, "borderwidth": 3, "highlightthickness": 2}
        self.button_style = {"font": ("Arial", 14), "bg": "white", "fg": "black", "relief": tk.RAISED, "borderwidth": 2}

        # User interface components
        self.mainLabel = tk.Label(self.root, text="ADMIN CHANGE PASSWORD", **self.heading_style)
        self.mainLabel.pack(pady=20)

        self.form = tk.Frame(self.root, bg="#455A64", highlightbackground="black", highlightthickness=2, borderwidth=2)
        self.form.pack(pady=20, padx=20)

        self.lb1 = tk.Label(self.form, text="Enter Email", **self.label_style_email)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tk.Entry(self.form, **self.entry_style)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = tk.Label(self.form, text="Enter Old Password", **self.label_style_password)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tk.Entry(self.form, **self.entry_style, show="*")
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = tk.Label(self.form, text="Enter New Password", **self.label_style_password)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tk.Entry(self.form, **self.entry_style, show="*")
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.btn = tk.Button(self.root, text="Submit", **self.button_style, width=20, command=self.change_password)
        self.btn.pack(pady=20)

        self.root.mainloop()

    def change_password(self):
        conn = Connect()
        cr = conn.cursor()
        email = self.txt1.get()
        old_password = self.txt2.get()
        new_password = self.txt3.get()

        if len(email) == 0 or len(old_password) == 0 or len(new_password) == 0:
            msg.showwarning("Warning", "Please fill all fields", parent=self.root)
        else:
            query = f"SELECT * FROM add_admin WHERE email = '{email}' and password='{old_password}'"
            cr.execute(query)
            result = cr.fetchone()
            if result is None:
                msg.showwarning("Warning", "Invalid Email or Password", parent=self.root)
            else:
                query = f"UPDATE add_admin SET password='{new_password}' WHERE email='{email}'"
                cr.execute(query)
                conn.commit()
                msg.showinfo("Success", "Admin password has been updated", parent=self.root)

#obj = AdminChangePassword()
