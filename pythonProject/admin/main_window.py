from tkinter import Tk, Canvas, Button
from PIL import Image, ImageTk
import os


class TitlePage:
    def __init__(self):
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title('Criminal Detection Database || Main Window')
        self.root.config(background='#da4469')

        # Updated image path
        img = Image.open('C:/Users/manjo/Downloads/fghgh.jpg')
        width = int(self.root.winfo_screenwidth())
        height = int(self.root.winfo_screenheight())
        img = img.resize((width, height))
        bg = ImageTk.PhotoImage(img)

        self.canvas = Canvas(self.root, width=self.root.winfo_width(), height=self.root.winfo_height())
        self.canvas.pack(fill='both', expand=True)

        self.canvas.create_image(0, 0, image=bg, anchor='nw')

        self.canvas.create_text(150, 30, text='CRIMINAL DETECTION DATABASE ', font=("Bahnschrift", 50, 'bold'), fill="#ccccff",
                                anchor='nw')

        self.canvas.create_text(255, 350, text='Welcome', font=("Bahnschrift", 60, 'bold'), fill="#ccccff")

        button_style = {
            'width': 10,
            'height': 1,
            'font': ("", 20, 'bold'),
            'bg': "#ccccff",  # Light gray background color
            'fg': "black",    # Black text color
            'activebackground': "#b3b3b3",  # Slightly darker gray background color when clicked
            'activeforeground': "black",     # Black text color when clicked
            'borderwidth': 2,
            'relief': "raised"
        }

        self.adminButton = Button(self.root, text="Admin Panel", command=self.open_admin_login, **button_style)
        self.adminWindow = self.canvas.create_window(50, 400, anchor="nw", window=self.adminButton)
        self.adminButton.bind("<Enter>", self.on_enter)
        self.adminButton.bind("<Leave>", self.on_leave)

        self.centerButton = Button(self.root, text="Center Panel", command=self.open_center_login, **button_style)
        self.centerWindow = self.canvas.create_window(260, 400, anchor="nw", window=self.centerButton)
        self.centerButton.bind("<Enter>", self.on_enter)
        self.centerButton.bind("<Leave>", self.on_leave)

        self.canvas.create_text(960, 300, text='Leave?', font=("Bahnschrift", 60, 'bold'), fill="#ccccff",
                                anchor='nw')
        self.leave = Button(self.root, text="Exit", command=lambda: self.root.destroy(), **button_style)
        self.leaveWindow = self.canvas.create_window(990, 400, anchor="nw", window=self.leave)  # Adjusted x-coordinate
        self.leave.bind("<Enter>", self.on_enter)
        self.leave.bind("<Leave>", self.on_leave)

        self.root.mainloop()

    def validate_admin_login(self, username, password):
        return True

    def open_admin_dashboard(self):
        os.system('python admin_dashboard.py')

    def open_admin_login(self):
        os.system('python admin_login.py')

    def open_center_login(self):
        os.system('python center_login.py')

    def on_enter(self, event):
        event.widget.config(bg="#b3b3b3")  # Change background color when cursor enters
        self.root.config(cursor="hand2")  # Change cursor to hand

    def on_leave(self, event):
        event.widget.config(bg="#ccccff")  # Change background color when cursor leaves
        self.root.config(cursor="")  # Reset cursor to default


TitlePage()