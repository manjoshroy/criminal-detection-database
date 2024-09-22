import tkinter
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect
import cv2
from tkinter.filedialog import askopenfilename


class Main:
    def __init__(self):
        self.root = tkinter.Tk()
        self.root.title("Criminal Database || Add Criminal")
        self.root.geometry("700x600")
        self.mainColor = '#2c3e50'
        self.secondColor = '#999999'
        self.textColor = 'black'
        self.font = ('', 14, 'bold')
        self.font1 = ('', 12)
        self.root.configure(bg=self.mainColor)

        self.mainLabel = tkinter.Label(self.root, text="ADD CRIMINAL", font=("Bahnschrift", 40, 'bold'), bg=self.mainColor,
                                       fg="white")

        self.mainLabel.pack(pady=20)
        self.form = tkinter.Frame(self.root, bg=self.secondColor, highlightbackground="black", highlightthickness=2)
        self.form.pack(pady=20)

        self.lb2 = tkinter.Label(self.form, text="Name", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = tkinter.Label(self.form, text="Email", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = tkinter.Label(self.form, text="Mobile", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.lb5 = tkinter.Label(self.form, text="Father Name", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)

        self.lb6 = tkinter.Label(self.form, text="Address", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3)
        self.txt6.grid(row=5, column=1, padx=10, pady=10)

        self.lb7 = tkinter.Label(self.form, text="Image", font=self.font, bg=self.secondColor,
                                 foreground=self.textColor)
        self.lb7.grid(row=6, column=0, padx=10, pady=10)
        self.txt7 = tkinter.Entry(self.form, font=self.font1, width=32, relief=tkinter.RIDGE, borderwidth=3)
        self.txt7.grid(row=6, column=1, padx=10, pady=10)
        self.btn1 = tkinter.Button(self.form, text="select", font=self.font, command=self.selectImage,
                                   background="white", foreground="black")
        self.btn1.grid(row=6, column=2, pady=10)

        self.btn = tkinter.Button(self.root, text="Submit", font=self.font, width=20, command=self.add_criminal,
                                  background="white", foreground="black")
        self.btn.pack(pady=10)
        self.root.mainloop()

    def selectImage(self):
        name = self.txt2.get()
        print(name)
        if len(name) != 0:
            path = askopenfilename()
            # print(path)
            img = cv2.imread(path)
            cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

            faces = cascade.detectMultiScale(img, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                cv2.rectangle(img=img, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=5)

            if len(faces) == 0:
                msg.showwarning("Warning", 'Image is not Valid', parent=self.root)
            else:
                msg.showinfo("Success", 'Image is uploaded')
                # img_name = f"{name}_{random.randint(10000, 99999)}.jpeg"
                img_name = f"{name}.jpeg"
                cv2.imwrite(f"../criminal_image/{img_name}", img)
                self.txt7.insert(0, img_name)
        else:
            msg.showwarning("warning", "Please enter the name first..", parent=self.root)

    def add_criminal(self):
        conn = Connect()
        cr = conn.cursor()
        # id = self.txt1.get()
        name = self.txt2.get()
        email = self.txt3.get()
        mobile = self.txt4.get()
        father_name = self.txt5.get()
        address = self.txt6.get()
        image = self.txt7.get()
        print(id, name, email, mobile, father_name, address, image)
        if len(name) == 0 or len(email) == 0 or len(mobile) == 0 or len(father_name) == 0 or len(
                address) == 0 or len(image) == 0:
            msg.showwarning("Warning", "Please enter all the filed", parent=self.root)
        else:
            q = f"insert into criminals values(null,'{name}','{email}','{mobile}', '{father_name}', '{address}', '{image}')"
            print(q)
            cr.execute(q)
            conn.commit()
            msg.showinfo("success", "criminal added successfully", parent=self.root)
            # self.txt1.delete(0, 'end')
            self.txt2.delete(0, 'end')
            self.txt3.delete(0, 'end')
            self.txt4.delete(0, 'end')
            self.txt5.delete(0, 'end')
            self.txt6.delete(0, 'end')
            self.txt7.delete(0, 'end')


#obj = Main()
