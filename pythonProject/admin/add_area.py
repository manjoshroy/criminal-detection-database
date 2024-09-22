import tkinter
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect


class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Criminal Database || Add Area")
        self.root.geometry("700x600")

        # New color scheme
        self.mainColor = '#2c3e50'
        self.secondColor = '#999999'
        self.textColor = 'black'

        self.font = ('', 14, 'bold')
        self.font1 = ('', 12)
        self.root.configure(bg=self.mainColor)

        self.mainLabel = tkinter.Label(self.root, text="ADD AREA", font=("Bahnschrift", 40, 'bold'), bg=self.mainColor,
                                       fg="white")
        self.mainLabel.pack(pady=20)

        self.form = tkinter.Frame(self.root, bg=self.secondColor, highlightbackground="black", highlightthickness=2)
        self.form.pack(pady=20)

        self.lb1 = tkinter.Label(self.form, text="Area Name", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = tkinter.Label(self.form, text="City Name", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = tkinter.Label(self.form, text="State Name", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = tkinter.Label(self.form, text="Land Mark", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.btn = tkinter.Button(self.root, text="Submit", font=self.font, width=20, command=self.add_area,
                                  background="#999999", foreground="black")
        self.btn.pack(pady=10)
        self.root.mainloop()

    def add_area(self):
        conn = Connect()
        cr = conn.cursor()
        area_name = self.txt1.get()
        city_name = self.txt2.get()
        state_name = self.txt3.get()
        land_mark = self.txt4.get()
        print(area_name, city_name, state_name, land_mark)
        if len(area_name) == 0 or len(city_name) == 0 or len(state_name) == 0 or len(land_mark) == 0:
            msg.showwarning("Warning", "Please enter all the fields", parent=self.root)
        else:
            q = f"insert into add_area values('{area_name}','{city_name}','{state_name}','{land_mark}')"
            print(q)
            cr.execute(q)
            conn.commit()
            msg.showinfo("Success", "Area added successfully", parent=self.root)
            self.txt1.delete(0, 'end')
            self.txt2.delete(0, 'end')
            self.txt3.delete(0, 'end')
            self.txt4.delete(0, 'end')

#obj = Main()