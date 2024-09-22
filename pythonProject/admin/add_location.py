import tkinter as tk
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect


class Main:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Criminal Database || Add Location")
        self.root.geometry("700x600")

        self.mainColor = '#2c3e50'
        self.secondColor = '#999999'
        self.textColor = 'black'
        self.font = ('Arial', 14, 'bold')
        self.font1 = ('Arial', 12)
        self.root.configure(bg=self.mainColor)

        self.mainLabel = tk.Label(self.root, text="ADD LOCATION", font=("Bahnschrift", 40, 'bold'), bg=self.mainColor,
                                  fg="white")
        self.mainLabel.pack(pady=20)

        self.form = tk.Frame(self.root, bg=self.secondColor, highlightbackground="black", highlightthickness=2)
        self.form.pack(pady=20)

        self.lb1 = tk.Label(self.form, text="Location Name", font=self.font, bg=self.secondColor,
                            foreground=self.textColor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tk.Entry(self.form, font=self.font1, width=32, relief=tk.RIDGE, borderwidth=3)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = tk.Label(self.form, text="Description", font=self.font, bg=self.secondColor,
                            foreground=self.textColor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tk.Entry(self.form, font=self.font1, width=32, relief=tk.RIDGE, borderwidth=3)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = tk.Label(self.form, text="Location Area", font=self.font, bg=self.secondColor,
                            foreground=self.textColor)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = ttk.Combobox(self.form, font=self.font1, width=30, values=self.getArea(),
                                 state='readonly')
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = tk.Label(self.form, text="Timings", font=self.font, bg=self.secondColor,
                            foreground=self.textColor)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = tk.Entry(self.form, font=self.font1, width=32, relief=tk.RIDGE, borderwidth=3)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.btn = tk.Button(self.root, text="Submit", font=self.font, width=20, command=self.add_location,
                             background="#FFFFFF", foreground="black")  # White button
        self.btn.pack(pady=10)

        self.root.mainloop()

    def getArea(self):
        conn = Connect()
        cr = conn.cursor()
        q = f"select * from add_area"
        cr.execute(q)
        result = cr.fetchall()
        lst = []
        for i in result:
            lst.append(i[0])
        return lst

    def add_location(self):
        conn = Connect()
        cr = conn.cursor()
        location_name = self.txt1.get()
        description = self.txt2.get()
        location_area = self.txt3.get()
        timings = self.txt4.get()
        if len(location_name) == 0 or len(description) == 0 or len(location_area) == 0 or len(timings) == 0:
            msg.showwarning("Warning", "Please enter all the fields", parent=self.root)
        else:
            q = f"insert into location1 values('{location_name}','{description}','{location_area}','{timings}')"
            cr.execute(q)
            conn.commit()
            msg.showinfo("Success", "Location added successfully", parent=self.root)
            self.txt1.delete(0, 'end')
            self.txt2.delete(0, 'end')
            self.txt3.delete(0, 'end')
            self.txt4.delete(0, 'end')


#obj = Main()
