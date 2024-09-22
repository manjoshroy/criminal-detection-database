import tkinter
import tkinter.messagebox as msg
from connection import Connect
import tkinter.ttk as ttk


class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Criminal Database || Add center")
        self.root.geometry("700x600")

        # New color scheme
        self.mainColor = '#2c3e50'
        self.secondColor = '#999999'
        self.textColor = 'black'

        self.font = ('', 14, 'bold')
        self.font1 = ('', 12)
        self.root.configure(bg=self.mainColor)

        self.mainLabel = tkinter.Label(self.root, text="ADD CENTER", font=("Bahnschrift", 40, 'bold'), bg=self.mainColor,
                                       fg="white")

        self.mainLabel.pack(pady=20)
        self.form = tkinter.Frame(self.root, bg=self.secondColor, highlightbackground="black", highlightthickness=2)
        self.form.pack(pady=20)

        self.lb1 = tkinter.Label(self.form, text="Name", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = tkinter.Label(self.form, text="Email", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = tkinter.Label(self.form, text="Mobile", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = tkinter.Label(self.form, text="Password", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = tkinter.Entry(self.form, font=self.font1, width=32, show="*", relief=tkinter.RIDGE, borderwidth=3)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.lb5 = tkinter.Label(self.form, text="Area", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5 = ttk.Combobox(self.form, font=self.font1, width=30, values=self.getArea(),
                                 state='readonly')
        self.txt5.grid(row=4, column=1, padx=10, pady=10)

        self.lb6 = tkinter.Label(self.form, text="Location", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6 = ttk.Combobox(self.form, font=self.font1, width=30, values=self.getlocation(),
                                 state='readonly')
        self.txt6.grid(row=5, column=1, padx=10, pady=10)

        self.btn = tkinter.Button(self.root, text="Submit", font=self.font, width=20, command=self.add_center,
                                  background="white", foreground="black")
        self.btn.pack(pady=10)
        self.root.mainloop()

    def getArea(self):
        conn = Connect()
        cr = conn.cursor()
        q = f"select * from add_area"
        cr.execute(q)
        result = cr.fetchall()
        list = []
        for i in result:
            list.append(i[0])
        return list

    def getlocation(self):
        conn = Connect()
        cr = conn.cursor()
        q = f"select * from location1"
        cr.execute(q)
        result = cr.fetchall()
        list = []
        for i in result:
            list.append(i[0])
        return list

    def add_center(self):
        conn = Connect()
        cr = conn.cursor()
        name = self.txt1.get()
        email = self.txt2.get()
        mobile = self.txt3.get()
        password = self.txt4.get()
        area = self.txt5.get()
        location = self.txt6.get()
        if len(name) == 0 or len(email) == 0 or len(mobile) == 0 or len(password) == 0 or len(
                area) == 0 or len(location) == 0:
            msg.showwarning("Warning", "Please enter all the fields", parent=self.root)
        else:
            try:
                q = f"INSERT INTO add_center (name, email, mobile, password, area, location) VALUES (%s, %s, %s, %s, %s, %s)"
                cr.execute(q, (name, email, mobile, password, area, location))
                conn.commit()
                msg.showinfo("Success", "Center added successfully", parent=self.root)
                self.txt1.delete(0, 'end')
                self.txt2.delete(0, 'end')
                self.txt3.delete(0, 'end')
                self.txt4.delete(0, 'end')
                self.txt5.delete(0, 'end')
                self.txt6.delete(0, 'end')
            except Exception as e:
                msg.showerror("Error", f"Failed to add center: {str(e)}", parent=self.root)


#obj = Main()
