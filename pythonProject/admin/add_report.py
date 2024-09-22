import tkinter as tk
from tkinter import messagebox as msg
from tkinter import ttk
from connection import Connect  # Assuming this is your database connection class
from tkinter.filedialog import askopenfilename
import cv2
import random
import os


class AddReport:
    def insert(self):
        if (self.title.get() == "" or self.description.get() == "" or self.date.get() == "" or
                self.culprit_name.get() == "" or self.mobile.get() == "" or self.email.get() == "" or
                self.address.get() == "" or self.image.get() == ""):
            msg.showwarning("Warning", "Please enter all fields", parent=self.root)
        else:
            sql = "INSERT INTO report (title, description, date, culprit_name, mobile, email, address, image) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
            values = (
                self.title.get(), self.description.get(), self.date.get(), self.culprit_name.get(), self.mobile.get(),
                self.email.get(), self.address.get(), self.image.get())
            self.cr.execute(sql, values)
            self.conn.commit()
            msg.showinfo("Success", "Inserted successfully", parent=self.root)
            self.conn.close()
            self.root.destroy()

    def selectImage(self):
        name = self.title.get()
        if len(name) != 0:
            path = askopenfilename()
            if path:
                img = cv2.imread(path)
                cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
                faces = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

                for (x, y, w, h) in faces:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 5)

                if len(faces) == 0:
                    msg.showwarning("Warning", 'Image is not valid', parent=self.root)
                else:
                    msg.showinfo("Success", 'Image has been uploaded', parent=self.root)
                    img_name = f"{name}_{random.randint(10000, 99999)}.jpeg"
                    if not os.path.exists("Report_Image"):
                        os.makedirs("Report_Image")
                    cv2.imwrite(f"Report_Image/{img_name}", img)
                    self.image.insert(0, img_name)
        else:
            msg.showwarning("Warning", "Please enter the title first", parent=self.root)

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("ADD REPORT")
        self.conn = Connect()
        self.cr = self.conn.cursor()
        self.root.state("zoomed")

        self.mainColor = '#2C3E50'
        self.secondColor = '#999999'
        self.textColor = 'black'
        self.buttonColor = 'white'
        self.entryBgColor = '#ECF0F1'

        self.font = ("Arial", 18, "bold")
        self.root.configure(bg=self.mainColor)

        self.style = ttk.Style()
        self.style.configure('TLabel', background=self.secondColor, foreground=self.textColor, font=self.font)
        self.style.configure('TButton', background=self.buttonColor, foreground='black', font=("Arial", 16, "bold"))
        self.style.configure('TEntry', font=self.font, fieldbackground=self.entryBgColor)

        self.mainLabel1 = tk.Label(self.root, text="ADD REPORT", font=("Bahnschrift", 40, 'bold'), bg=self.mainColor, fg="white")
        self.mainLabel1.pack(pady=20)

        self.form = tk.Frame(self.root, bg=self.secondColor, padx=5, pady=20, highlightthickness=2, highlightbackground='black')
        self.form.pack(pady=20, padx=20, fill=tk.NONE, expand=False)

        self.lb1 = ttk.Label(self.form, text="Title")
        self.lb1.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.title = ttk.Entry(self.form, font=self.font, width=25)
        self.title.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.lb2 = ttk.Label(self.form, text="Description")
        self.lb2.grid(row=2, column=0, padx=10, pady=5, sticky="e")
        self.description = ttk.Entry(self.form, font=self.font, width=25)
        self.description.grid(row=2, column=1, padx=10, pady=5, sticky="w")

        self.lb3 = ttk.Label(self.form, text="Date")
        self.lb3.grid(row=3, column=0, padx=10, pady=5, sticky="e")
        self.date = ttk.Entry(self.form, font=self.font, width=25)
        self.date.grid(row=3, column=1, padx=10, pady=5, sticky="w")

        self.lb4 = ttk.Label(self.form, text="Culprit Name")
        self.lb4.grid(row=4, column=0, padx=10, pady=5, sticky="e")
        self.culprit_name = ttk.Entry(self.form, font=self.font, width=25)
        self.culprit_name.grid(row=4, column=1, padx=10, pady=5, sticky="w")

        self.lb5 = ttk.Label(self.form, text="Mobile")
        self.lb5.grid(row=5, column=0, padx=10, pady=5, sticky="e")
        self.mobile = ttk.Entry(self.form, font=self.font, width=25)
        self.mobile.grid(row=5, column=1, padx=10, pady=5, sticky="w")

        self.lb6 = ttk.Label(self.form, text="Email")
        self.lb6.grid(row=6, column=0, padx=10, pady=5, sticky="e")
        self.email = ttk.Entry(self.form, font=self.font, width=25)
        self.email.grid(row=6, column=1, padx=10, pady=5, sticky="w")

        self.lb7 = ttk.Label(self.form, text="Address")
        self.lb7.grid(row=7, column=0, padx=10, pady=5, sticky="e")
        self.address = ttk.Entry(self.form, font=self.font, width=25)
        self.address.grid(row=7, column=1, padx=10, pady=5, sticky="w")

        self.lb8 = ttk.Label(self.form, text="Choose Image")
        self.lb8.grid(row=8, column=0, padx=10, pady=5, sticky="e")
        self.image = ttk.Entry(self.form, font=self.font, width=25)
        self.image.grid(row=8, column=1, padx=10, pady=5, sticky="w")
        self.saveBtn = ttk.Button(self.form, text="Select Image", command=self.selectImage)
        self.saveBtn.grid(row=8, column=2, padx=10, pady=5)

        self.btn = ttk.Button(self.form, text="SUBMIT", width=15, command=self.insert)
        self.btn.grid(row=9, columnspan=3, pady=10)

        self.center_window()
        self.root.mainloop()

    def center_window(self):
        self.root.update_idletasks()
        width = self.form.winfo_width()
        height = self.form.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.form.place(x=x, y=y, anchor="center")


if __name__ == "__main__":
    AddReport()
