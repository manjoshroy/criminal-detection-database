from connection import Connect
import tkinter
import tkinter.messagebox as msg
import tkinter.ttk as ttk


class centerchangepassword:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Criminal Database || Center Change Password")
        self.root.geometry("700x600")

        self.mainColor = '#2C3E50'
        self.secondColor = '#34495E'
        self.textColor = 'white'
        self.inputBgColor = '#F0F0F0'
        self.inputFgColor = 'black'

        self.font = ('', 14, 'bold')
        self.font1 = ('', 12)
        self.root.configure(bg=self.mainColor)

        self.mainLabel = tkinter.Label(self.root, text="Center Change Password", font=("", 20, 'bold'),
                                       bg=self.mainColor, fg=self.textColor)
        self.mainLabel.pack(pady=20)

        self.form = tkinter.Frame(self.root, bg=self.secondColor, highlightbackground="white", highlightthickness=2)
        self.form.pack(pady=20)

        self.lb1 = tkinter.Label(self.form, text="Enter Email", font=self.font, bg=self.secondColor,
                                 fg=self.textColor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3,
                                  bg=self.inputBgColor, fg=self.inputFgColor)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = tkinter.Label(self.form, text="Enter Old Password", font=self.font, bg=self.secondColor,
                                 fg=self.textColor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3,
                                  bg=self.inputBgColor, fg=self.inputFgColor, show='*')
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = tkinter.Label(self.form, text="Enter New Password", font=self.font, bg=self.secondColor,
                                 fg=self.textColor)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3,
                                  bg=self.inputBgColor, fg=self.inputFgColor, show='*')
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.btn = tkinter.Button(self.root, text="Submit", font=self.font, width=20, command=self.change_password,
                                  bg="white", fg=self.mainColor)
        self.btn.pack(pady=10)

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
            q = f"SELECT * FROM add_center WHERE email = '{email}' AND password = '{old_password}'"
            cr.execute(q)
            result = cr.fetchone()
            if result is None:
                msg.showwarning("Warning", "Invalid email or password", parent=self.root)
            else:
                q = f"UPDATE add_center SET password = '{new_password}' WHERE email = '{email}'"
                cr.execute(q)
                conn.commit()
                msg.showinfo("Success", "Password has been updated", parent=self.root)

if __name__ == "__main__":
    centerchangepassword()
