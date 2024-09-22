from tkinter import *
import tkinter.messagebox as msg
from PIL import Image, ImageTk
from connection import Connect  # Ensure these imports are correct
from admin import add_criminal, view_criminal, add_report, view_report, center_changepassword, view_identifycriminal
from admin import identify_criminal
from admin import center_profile


class CenterDashboard:
    def __init__(self, centerDetails):
        self.centerDetails = centerDetails
        print(centerDetails)
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title("Center Dashboard")

        self.mainMenu = Menu(self.root, bg='#2c3e50', fg='white', font=('Arial', 12), activebackground='black')
        self.root.configure(menu=self.mainMenu)

        # Updated image path
        img_path = 'C:/Users/manjo/Downloads/gbgb.jpg'
        img = Image.open(img_path)

        # Get screen width and height
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()

        img = img.resize((width, height))

        # Create PhotoImage object
        bg = ImageTk.PhotoImage(img)

        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill='both', expand=True)

        self.canvas.create_image(0, 0, image=bg, anchor='nw')

        text_overlay = "Welcome to Center Dashboard"
        self.canvas.create_text(width // 2, 50, text=text_overlay, font=('', 28, 'bold'), fill='white')

        self.create_menu()

        # Keep a reference to the image to prevent it from being garbage collected
        self.bg_image = bg

        self.root.mainloop()

    def create_menu(self):
        menu_options = {'bg': '#2c3e50', 'fg': 'white', 'font': ('Arial', 12), 'activebackground': 'black'}

        self.adminSubMenu = Menu(self.mainMenu, tearoff=0, **menu_options)
        self.mainMenu.add_cascade(label="Manage Criminal", menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label="Add Criminal", command=add_criminal.Main)
        self.adminSubMenu.add_command(label="View Criminal", command=self.view_criminal)

        self.reportSubMenu = Menu(self.mainMenu, tearoff=0, **menu_options)
        self.mainMenu.add_cascade(label="Manage Report", menu=self.reportSubMenu)
        self.reportSubMenu.add_command(label="Add Report", command=add_report.AddReport)
        self.reportSubMenu.add_command(label="View Report", command=self.view_report)

        self.identifySubMenu = Menu(self.mainMenu, tearoff=0, **menu_options)
        self.mainMenu.add_cascade(label="Identify Criminal", menu=self.identifySubMenu)
        self.identifySubMenu.add_command(label="Identify Criminal",
                                         command=lambda: identify_criminal.identifycriminal(self.centerDetails))
        self.identifySubMenu.add_command(label="View Identified Criminals", command=self.view_identifiedcriminal)

        self.profileSubMenu = Menu(self.mainMenu, tearoff=0, **menu_options)
        self.mainMenu.add_cascade(label="Manage Profile", menu=self.profileSubMenu)
        self.profileSubMenu.add_command(label="Center Profile", command=self.center_profile)
        self.profileSubMenu.add_command(label="Center Change Password", command=self.center_changepassword)
        self.profileSubMenu.add_command(label="Logout", command=self.logout)

    def logout(self):
        self.root.destroy()

    def view_criminal(self):
        obj = view_criminal.criminal()

    def center_changepassword(self):
        obj = center_changepassword.centerchangepassword()

    def view_report(self):
        obj = view_report.report()

    def view_identifiedcriminal(self):
        obj = view_identifycriminal.viewidentifycriminal()

    def center_profile(self):
        obj = center_profile.CenterProfile(2)


if __name__ == '__main__':
    admin = CenterDashboard(centerDetails=(1, 'manjoshroy18@gmail.com'))
