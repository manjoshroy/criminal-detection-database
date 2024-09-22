import tkinter
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import re
from connection import Connect

class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Criminal Database || Add Admin")
        self.root.geometry("700x600")
        self.mainColor = '#2c3e50'
        self.secondColor = '#999999'
        self.textColor = 'black'
        self.font = ('', 14, 'bold')
        self.font1 = ('', 12)
        self.root.configure(bg=self.mainColor)
        self.mainLabel = tkinter.Label(self.root, text="ADD ADMIN", font=("Bahnschrift", 40, 'bold'), bg=self.mainColor,
                                       fg="white")
        self.mainLabel.pack(pady=20)
        self.form = tkinter.Frame(self.root, bg=self.secondColor, highlightbackground="black", highlightthickness=2)
        self.form.pack(pady=20)

        self.lb1 = tkinter.Label(self.form, text="Admin Name", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = tkinter.Label(self.form, text="Enter Email", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = tkinter.Label(self.form, text="Enter Password", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tkinter.Entry(self.form, font=self.font1, width=32, show="*", relief=tkinter.RIDGE, borderwidth=3)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = tkinter.Label(self.form, text="Select Role", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = ttk.Combobox(self.form, font=self.font1, width=30, values=['Super Admin', 'Admin'], state='readonly')
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.lb5 = tkinter.Label(self.form, text="Mobile", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)

        self.btn = tkinter.Button(self.root, text="Submit", font=self.font, width=20, command=self.add_admin,
                                  background="white", foreground="black")
        self.btn.pack(pady=10)
        self.root.mainloop()

    def is_valid_password(self, password):
        # Password should be at least 8 characters long, contain at least one symbol and one capital letter
        if len(password) < 8:
            return False
        if not re.search(r"[A-Z]", password):
            return False
        if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
            return False
        return True

    def add_admin(self):
        conn = Connect()
        cr = conn.cursor()
        name = self.txt1.get()
        email = self.txt2.get()
        password = self.txt3.get()
        role = self.txt4.get()
        mobile = self.txt5.get()
        print(name, email, password, role, mobile)
        if len(name) == 0 or len(email) == 0 or len(password) == 0 or len(role) == 0 or len(mobile) == 0:
            msg.showwarning("Warning", "Please enter all the fields", parent=self.root)
        else:
            if '@' in email and '.' in email:
                if self.is_valid_password(password):
                    if len(mobile) == 10 and mobile.isdigit():
                        q = f"insert into add_admin values(null,'{name}','{email}','{password}','{role}','{mobile}')"
                        print(q)
                        cr.execute(q)
                        conn.commit()
                        msg.showinfo("Success", "Admin added successfully", parent=self.root)
                        self.txt1.delete(0, 'end')
                        self.txt2.delete(0, 'end')
                        self.txt3.delete(0, 'end')
                        self.txt4.set('')  # Reset the ComboBox
                        self.txt5.delete(0, 'end')
                    else:
                        msg.showwarning("Warning", "Please enter a valid 10-digit mobile number", parent=self.root)
                else:
                    msg.showwarning("Warning", "Password must be at least 8 characters and contain at least one symbol and one capital letter", parent=self.root)
            else:
                msg.showwarning("Warning", "Please enter email in correct format", parent=self.root)


#obj = Main()
