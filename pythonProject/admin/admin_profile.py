import tkinter
from tkinter import ttk
import tkinter.messagebox as msg
from PIL import Image, ImageTk
from connection import Connect


class adminprofile:
    def __init__(self, data):
        self.id = data[0]
        self.root = tkinter.Toplevel()
        self.root.title("Manage Profile")
        self.root.state('zoomed')

        self.mainColor = '#444b6e'
        self.secondColor = '#8d95b9'
        self.thirdColor = '#272c3f'

        self.font = ('', 15, 'bold')
        self.font1 = ('', 15)
        self.root.configure(bg=self.mainColor)
        self.mainLabel = tkinter.Label(self.root, text="Admin Profile", relief="solid", borderwidth=4,
                                       font=("Arial", 35, 'bold'))
        self.mainLabel.pack(pady=10, padx=10)

        width = int(self.root.winfo_screenwidth())
        height = int(self.root.winfo_screenheight())

        self.frame = tkinter.Frame(self.root, highlightthickness=2, bg="white", padx=10, pady=10)
        self.frame.pack(fill=tkinter.BOTH, expand=True)

        self.frame1 = tkinter.Frame(self.frame, highlightthickness=2, highlightbackground="black", padx=30, pady=30)
        self.frame1.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        self.frame2 = tkinter.Frame(self.frame, bg="grey", highlightthickness=2, highlightbackground="black", padx=40, pady=40)
        self.frame2.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

        img = Image.open('D:\\Personal\\aadhar\\WhatsApp Image 2024-01-07 at 09.50.38_15237457.jpg')

        # Resize the image to fit the frame
        img = img.resize((width // 3, height // 2))
        self.bg = ImageTk.PhotoImage(img)

        self.canvas = tkinter.Canvas(self.frame1, width=width // 3, height=height // 2, highlightthickness=2, highlightbackground="black")
        self.canvas.pack(fill='both', expand=True)
        self.canvas.create_image(0, 0, image=self.bg, anchor='nw')

        self.lb1 = tkinter.Label(self.frame2, text="Admin Name", relief="solid", font=self.font, borderwidth=4, padx=5,
                                 pady=5)
        self.lb1.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.txt1 = tkinter.Entry(self.frame2, font=self.font1, width=25, relief="solid", borderwidth=4)
        self.txt1.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.lb2 = tkinter.Label(self.frame2, text="Enter Email", relief="solid", borderwidth=4, font=self.font, padx=5,
                                 pady=5)
        self.lb2.grid(row=1, column=0, padx=20, pady=10, sticky="e")
        self.txt2 = tkinter.Entry(self.frame2, font=self.font1, width=25, relief="solid", borderwidth=4)
        self.txt2.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.lb3 = tkinter.Label(self.frame2, text="Mobile ", relief="solid", borderwidth=4, font=self.font, padx=5,
                                 pady=5)
        self.lb3.grid(row=2, column=0, padx=60, pady=10, sticky="e")
        self.txt3 = tkinter.Entry(self.frame2, font=self.font1, width=25, relief="solid", borderwidth=4)
        self.txt3.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.btn = tkinter.Button(self.frame2, text="Submit", font=self.font, width=15, relief="solid", borderwidth=5,
                                  command=self.add_admin)
        self.btn.grid(row=3, column=1, pady=20)

        self.txt1.insert(0, data[1])
        self.txt2.insert(0, data[2])
        self.txt3.insert(0, data[3])

        self.root.mainloop()

    def add_admin(self):
        conn = Connect()
        cr = conn.cursor()
        Admin_Name = self.txt1.get()
        Enter_Email = self.txt2.get()
        mobile = self.txt3.get()
        if len(Admin_Name) == 0 or len(Enter_Email) == 0 or len(mobile) == 0:
            msg.showwarning("Warning", "Please enter all the fields", parent=self.root)
        else:
            if '@' in Enter_Email and '.' in Enter_Email and mobile.isdigit() and len(mobile) == 10:
                q = f"update add_admin set name='{Admin_Name}', email='{Enter_Email}', mobile='{mobile}' where id='{self.id}'"
                cr.execute(q)
                conn.commit()
                msg.showinfo("success", "Admin added successfully", parent=self.root)
                self.txt1.delete(0, 'end')
                self.txt2.delete(0, 'end')
                self.txt3.delete(0, 'end')
            else:
                msg.showwarning("Warning", "Please enter email and mobile in correct format", parent=self.root)


data = [1, 'manjosh', 'm@gmail.com', '1234123412']
#obj = adminprofile(data)
