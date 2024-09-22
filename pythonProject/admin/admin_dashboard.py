from tkinter import *
import tkinter.messagebox as msg
from PIL import Image, ImageTk
from connection import Connect
from view_admin import ViewAdmin
from admin import add_center, add_admin
from admin import view_center
from admin import add_category
from admin import view_category
from admin import add_area
from admin import view_area
from admin import add_location
from admin import view_location
from admin import add_criminal
from admin import view_criminal
from admin import add_report
from admin import view_report, view_admin
from admin import admin_changepassword
from admin import admin_profile

class AdminDashboard:
    def __init__(self, adminDetails):
        self.adminDetails = adminDetails
        print(adminDetails)
        self.root = Tk()
        self.root.state('zoomed')
        self.root.title("Welcome to Admin Dashboard")

        self.mainMenu = Menu(self.root, bg='#4CAF50', fg='white', font=('Arial', 12))
        self.root.configure(menu=self.mainMenu)

        # Updated image path
        img = Image.open('C:/Users/manjo/Downloads/fvvfhv.jpg')
        width = self.root.winfo_screenwidth()
        height = self.root.winfo_screenheight()
        img = img.resize((width, height))
        self.bg = ImageTk.PhotoImage(img)

        self.canvas = Canvas(self.root, width=width, height=height)
        self.canvas.pack(fill='both', expand=True)

        self.canvas.create_image(0, 0, image=self.bg, anchor='nw')

        text_overlay = f"Welcome {self.adminDetails[2]} to your Dashboard"
        self.canvas.create_text(width // 2, 50, text=text_overlay, font=('Bahnschrift', 40, 'bold'), fill='black')

        self.create_menu()

        # Keep a reference to the image to prevent it from being garbage collected
        self.bg_image = self.bg

        self.root.mainloop()

    def create_menu(self):
        menu_options = {'bg': '#2c3e50', 'fg': 'white', 'font': ('Arial', 12), 'activebackground': 'black'}

        if self.adminDetails[-1] in ["Super Admin", "Admin"]:
            self.adminSubMenu = Menu(self.mainMenu, tearoff=0, **menu_options)
            self.mainMenu.add_cascade(label="Manage Admin", menu=self.adminSubMenu)
            self.adminSubMenu.add_command(label="Add Admin", command=self.run_add_admin)
            self.adminSubMenu.add_command(label="View Admin", command=self.view_admin)

        self.adminSubMenu = Menu(self.mainMenu, tearoff=0, **menu_options)
        self.mainMenu.add_cascade(label="Manage category", menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label="Add Category", command=self.run_add_category)
        self.adminSubMenu.add_command(label="View Category", command=self.view_category)

        self.adminSubMenu = Menu(self.mainMenu, tearoff=0, **menu_options)
        self.mainMenu.add_cascade(label="Manage Area", menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label="Add Area", command=self.run_add_area)
        self.adminSubMenu.add_command(label="View Area", command=self.view_area)

        self.adminSubMenu = Menu(self.mainMenu, tearoff=0, **menu_options)
        self.mainMenu.add_cascade(label="Manage Location", menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label="Add Location", command=self.run_add_location)
        self.adminSubMenu.add_command(label="View Location", command=self.view_location)

        self.adminSubMenu = Menu(self.mainMenu, tearoff=0, **menu_options)
        self.mainMenu.add_cascade(label="Manage Center", menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label="Add Center", command=self.run_add_center)
        self.adminSubMenu.add_command(label="View Center", command=self.view_center)

        self.adminSubMenu = Menu(self.mainMenu, tearoff=0, **menu_options)
        self.mainMenu.add_cascade(label="Manage criminal", menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label="Add criminal", command=self.run_add_criminal)
        self.adminSubMenu.add_command(label="View criminal", command=self.view_criminal)

        self.adminSubMenu = Menu(self.mainMenu, tearoff=0, **menu_options)
        self.mainMenu.add_cascade(label="Manage Report", menu=self.adminSubMenu)
        self.adminSubMenu.add_command(label="Add Report", command=self.run_add_report)
        self.adminSubMenu.add_command(label="View Report", command=self.view_report)

        self.profileSubMenu = Menu(self.mainMenu, tearoff=0, **menu_options)
        self.mainMenu.add_cascade(label="Profile", menu=self.profileSubMenu)
        self.profileSubMenu.add_command(label="Change Password", command=self.admin_changepassword)
        self.profileSubMenu.add_command(label="Admin Profile", command=self.admin_profile)
        self.profileSubMenu.add_command(label="Logout", command=self.logout)

    def logout(self):
        self.root.destroy()

    def view_admin(self):
        obj = view_admin.ViewAdmin()

    def run_add_admin(self):
        obj = add_admin.Main()

    def run_add_category(self):
        obj = add_category.Main()

    def run_add_area(self):
        obj = add_area.Main()

    def run_add_location(self):
        obj = add_location.Main()

    def run_add_center(self):
        obj = add_center.Main()

    def run_add_criminal(self):
        obj = add_criminal.Main()

    def run_add_report(self):
        obj = add_report.AddReport()

    def admin_changepassword(self):
        obj = admin_changepassword.AdminChangePassword()

    def view_category(self):
        obj = view_category.Category()

    def view_center(self):
        obj = view_center.Viewcenter()

    def admin_profile(self):
        obj = admin_profile.adminprofile(data=self.adminDetails)

    def view_area(self):
        obj = view_area.area()

    def view_location(self):
        obj = view_location.location()

    def view_criminal(self):
        obj = view_criminal.criminal()

    def view_report(self):
        obj = view_report.report()


if __name__ == '__main__':
    admin = AdminDashboard(adminDetails=(1, 'manjoshroy18@gmail.com', 'manjoshroy', '9391038744', 'Super Admin'))