from tkinter import *
from PIL import Image, ImageTk
import tkinter.messagebox as msg
from connection import Connect
from admin import admin_dashboard


class AdminLogin:
    def __init__(self):
        self.root = Tk()
        self.root.title("Admin Login")
        self.root.state('zoomed')  # Maximize the window
        self.font = ('Arial', 14)
        self.conn = Connect()
        self.cr = self.conn.cursor()

        # Updated image path
        self.bg_image_path = "C:/Users/manjo/Downloads/bhbdhbd.jpg"
        self.bg_image = Image.open(self.bg_image_path)

        # Create a canvas and set the initial background image
        self.canvas = Canvas(self.root)
        self.canvas.pack(fill=BOTH, expand=True)

        # Load the background image
        self.update_background()

        # Color Scheme
        self.mainColor = '#1B3A57'
        self.secondColor = '#5DADE2'
        self.entryColor = '#D6EAF8'
        self.buttonColor = '#FFFFFF'
        self.textColor = '#000000'

        # Bind the resize event
        self.root.bind("<Configure>", self.resize_background)

        # Login Form Frame
        self.loginForm = Frame(self.canvas, bg=self.secondColor)

        # Email Label and Entry
        self.lb1 = Label(self.loginForm, text="Enter Email", font=self.font, bg=self.secondColor, fg="black")
        self.lb1.grid(row=0, column=0, padx=10, pady=5, sticky=W)
        self.txt1 = Entry(self.loginForm, width=30, font=self.font, bg=self.entryColor)
        self.txt1.grid(row=0, column=1, padx=10, pady=5)

        # Password Label and Entry
        self.lb2 = Label(self.loginForm, text="Enter Password", font=self.font, bg=self.secondColor, fg="black")
        self.lb2.grid(row=1, column=0, padx=10, pady=5, sticky=W)
        self.txt2 = Entry(self.loginForm, width=30, font=self.font, bg=self.entryColor, show='*')
        self.txt2.grid(row=1, column=1, padx=10, pady=5)

        # Login Button
        self.loginButton = Button(self.canvas, text="Login", width=15, font=self.font, bg=self.buttonColor, fg=self.mainColor, command=self.check_admin)
        self.loginButton_window = self.canvas.create_window(650, 450, window=self.loginButton, anchor=CENTER)

        # Pack the login form frame on the canvas
        self.loginForm_window = self.canvas.create_window(650, 300, window=self.loginForm, anchor=CENTER)

        self.root.mainloop()

    def resize_background(self, event):
        self.update_background()

    def update_background(self):
        # Get current window size
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        # Resize the image to fit the window
        self.bg_resized_image = self.bg_image.resize((width, height))
        self.bg_photo = ImageTk.PhotoImage(self.bg_resized_image)
        # Update the canvas background
        self.canvas.create_image(0, 0, image=self.bg_photo, anchor=NW)

        # Overlay text on the image
        text_overlay = "ADMIN LOGIN"
        self.canvas.create_text(640, 160, text=text_overlay, font=('Bahnschrift', 50, 'bold'), fill="white", anchor=CENTER)

    def check_admin(self):
        email = self.txt1.get()
        password = self.txt2.get()
        q = f"SELECT id, email, name, mobile, role FROM add_admin WHERE email = '{email}' and password='{password}'"
        self.cr.execute(q)
        result = self.cr.fetchone()

        if result is None:
            msg.showwarning("Warning", "Invalid Email or Password", parent=self.root)
        else:
            print(result)
            msg.showinfo("Success", "Login Successful", parent=self.root)
            self.root.destroy()
            admin_dashboard.AdminDashboard(adminDetails=result)


if __name__ == "__main__":
    AdminLogin()
