import tkinter
import tkinter.messagebox as msg
from connection import Connect


class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Criminal Database || Add Category")
        self.root.geometry("900x800")
        self.mainColor = '#2c3e50'
        self.secondColor = '#999999'
        self.textColor = 'black'

        self.font = ('', 14, 'bold')
        self.font1 = ('', 12)
        self.root.configure(bg=self.mainColor)

        self.mainLabel = tkinter.Label(self.root, text="ADD CATEGORY", font=("Bahnschrift", 40, 'bold'), bg=self.mainColor,
                                       fg="white")
        self.mainLabel.pack(pady=20)

        self.Form = tkinter.Frame(self.root, bg=self.secondColor, highlightbackground="black", highlightthickness=2)
        self.Form.pack(pady=20)

        self.lb1 = tkinter.Label(self.Form, text="Category Name", font=self.font, bg=self.secondColor, fg=self.textColor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)

        self.txt1 = tkinter.Entry(self.Form, font=self.font1, width=40, relief=tkinter.RIDGE)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = tkinter.Label(self.Form, text="Description", font=self.font, bg=self.secondColor, fg=self.textColor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)

        self.txt2 = tkinter.Entry(self.Form, font=self.font1, width=40, relief=tkinter.RIDGE)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.btn = tkinter.Button(self.root, text="Submit", font=self.font, width=20, command=self.category,
                                  background="white", foreground="black")
        self.btn.pack(pady=10)

        self.root.mainloop()

    def category(self):
        conn = Connect()
        cr = conn.cursor()
        name = self.txt1.get()
        description = self.txt2.get()

        print(name, description)

        if len(name) == 0 or len(description) == 0:
            msg.showwarning("Warning", "Please enter all the fields", parent=self.root)
        else:
            q = f"INSERT INTO category VALUES ('{name}', '{description}')"
            print(q)
            cr.execute(q)
            conn.commit()
            msg.showinfo("Success", "Category added successfully", parent=self.root)
            self.txt1.delete(0, 'end')
            self.txt2.delete(0, 'end')


#obj = Main()