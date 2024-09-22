from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect


class Viewcenter:
    def __init__(self):
        self.root = Tk()
        self.root.state("zoomed")
        self.root.title("Criminal Database || View center ")
        self.conn = Connect()
        self.cr = self.conn.cursor()

        # Apply the styles from the Category class
        self.mainColor = '#2c3e50'
        self.secondColor = '#3498db'
        self.textColor = 'white'
        self.root.configure(bg=self.mainColor)

        # Create a ttk style
        self.style = ttk.Style()

        # Configure the style for the Treeview widget
        self.style.configure("Treeview", font=('', 14), rowheight=50, background='#FFFFFF', foreground='#000000')
        self.style.configure("Treeview.Heading", font=('', 14, 'bold'), background='#FFFFFF', foreground='#000000')  # Update font color to black

        # Configure the style for the buttons
        self.style.configure("TButton", font=('', 12), background='#4d79ff', foreground='#000000')
        self.style.map("TButton", background=[('active', '#4d79ff')])

        # Configure the style for the labels
        self.style.configure("TLabel", font=('', 14), background='#4d79ff', foreground='#000000')

        # Add more styles
        self.style.configure("TFrame", background='#FFFFFF')
        self.style.configure("Horizontal.TScale", background='#FFFFFF', foreground='#000000')
        self.style.configure("Vertical.TScrollbar", background='#FFFFFF', foreground='#000000')
        self.style.configure("Horizontal.TProgressbar", background='#2196F3', foreground='#FFFFFF')

        # Configure the style for the Entry widgets
        self.style.configure("TEntry", font=('', 14), background='#FFFFFF', foreground='#000000')

        self.mainlabel = Label(self.root, text="VIEW CENTER", font=('Helvetica', 28, 'bold'), bg=self.mainColor, fg=self.textColor)
        self.mainlabel.pack(pady=20)

        self.searchFrame = Frame(self.root, bg=self.mainColor, borderwidth=2)
        self.searchFrame.pack(pady=10)

        # Search label and entry
        self.searchLabel = Label(self.searchFrame, text="Search", font=('', 14), bg=self.mainColor, fg=self.textColor)
        self.searchLabel.pack(side=LEFT, padx=10, pady=20)
        self.searchField = Entry(self.searchFrame, font=('', 14), bg="white", fg="black")
        self.searchField.pack(side=LEFT, padx=10, pady=20)

        # Buttons using ttk.Button
        self.searchBtn = ttk.Button(self.searchFrame, text="Search", style="TButton", width=10, command=self.searchcenter)
        self.searchBtn.pack(side=LEFT, padx=10, pady=20)
        self.refreshBtn = ttk.Button(self.searchFrame, text="Refresh", style="TButton", width=10, command=self.refreshData)
        self.refreshBtn.pack(side=LEFT, padx=10, pady=20)
        self.deleteBtn = ttk.Button(self.searchFrame, text="Delete", style="TButton", width=10, command=self.deletecenter)
        self.deleteBtn.pack(side=LEFT, padx=10, pady=20)

        self.centerTable = ttk.Treeview(self.root, columns=('id', 'name', 'email', 'mobile', 'password', 'area', 'location'))
        self.centerTable.heading('id', text='id')
        self.centerTable.heading('name', text='name')
        self.centerTable.heading('email', text='email')
        self.centerTable.heading('mobile', text='mobile')
        self.centerTable.heading('password', text='password')
        self.centerTable.heading('area', text='area')
        self.centerTable.heading('location', text='location')
        self.centerTable['show'] = 'headings'

        self.centerTable.pack(expand=True, fill='both', padx=20, pady=20)
        self.getcenterInfo()

        self.style.theme_use('clam')

        self.centerTable.bind("<Double-1>", self.openUpdateWindow)

        self.root.mainloop()

    def getcenterInfo(self):
        q = "select id, name, email, mobile, password, area, location from add_center"
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.centerTable.get_children():
            self.centerTable.delete(row)

        for i in range(len(result)):
            self.centerTable.insert('', index=i, values=result[i])

    def searchcenter(self):
        data = self.searchField.get()
        q = f" select id, name, email, mobile, password, area, location from add_center where name like '%{data}%'"
        print(q)
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.centerTable.get_children():
            self.centerTable.delete(row)

        for i in range(len(result)):
            self.centerTable.insert('', index=i, values=result[i])

    def refreshData(self):
        self.searchField.delete(0, 'end')
        self.getcenterInfo()

    def deletecenter(self):
        row = self.centerTable.selection()
        if len(row) == 0:
            msg.showwarning("Warning", "Please select the Item", parent=self.root)
        else:
            row_id = row[0]
            items = self.centerTable.item(row_id)
            data = items['values']
            confirm = msg.askyesno("", "Are you sure you want to delete ?", parent=self.root)
            if confirm:
                q = f"delete from add_center where id='{data[0]}'"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo("Success", "center has been deleted", parent=self.root)
                self.refreshData()
            else:
                msg.showinfo("Success", "Deletion Aborted", parent=self.root)

    def openUpdateWindow(self, event):
        row = self.centerTable.selection()
        row_id = row[0]
        items = self.centerTable.item(row_id)
        data = items['values']

        self.root1 = Toplevel()
        self.root1.geometry("700x600")

        self.mainlabel1 = Label(self.root1, text="Update Center", font=('', 24, 'bold'), fg="black")
        self.mainlabel1.pack(pady=20)

        self.updateForm = Frame(self.root1, bg=self.mainColor)

        font = ('', 14)

        self.lb1 = Label(self.updateForm, text="Name", font=font, bg=self.mainColor, fg=self.textColor)
        self.txt1 = Entry(self.updateForm, font=font)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[1])

        self.lb2 = Label(self.updateForm, text="email", font=font, bg=self.mainColor, fg=self.textColor)
        self.txt2 = Entry(self.updateForm, font=font)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[2])

        self.lb3 = Label(self.updateForm, text="mobile", font=font, bg=self.mainColor, fg=self.textColor)
        self.txt3 = Entry(self.updateForm, font=font)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[3])

        self.lb4 = Label(self.updateForm, text="password", font=font, bg=self.mainColor, fg=self.textColor)
        self.txt4 = Entry(self.updateForm, font=font)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)
        self.txt4.insert(0, data[4])

        self.lb5 = Label(self.updateForm, text="area", font=font, bg=self.mainColor, fg=self.textColor)
        self.txt5 = Entry(self.updateForm, font=font)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.insert(0, data[5])

        self.lb6 = Label(self.updateForm, text="location", font=font, bg=self.mainColor, fg=self.textColor)
        self.txt6 = Entry(self.updateForm, font=font)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6.grid(row=5, column=1, padx=10, pady=10)
        self.txt6.insert(0, data[6])

        self.updateForm.pack(pady=10)

        self.updateBtn = Button(self.root1, text="Update", font=('', 12), width=10, command=self.updatecenter, bg=self.secondColor, fg=self.textColor)
        self.updateBtn.pack(pady=20)

        self.root1.mainloop()

    def updatecenter(self):
        id = self.centerTable.item(self.centerTable.selection())['values'][0]  # Get the id of the selected center
        name = self.txt1.get()
        email = self.txt2.get()
        mobile = self.txt3.get()
        password = self.txt4.get()
        area = self.txt5.get()
        location = self.txt6.get()

        q = f"UPDATE add_center SET name='{name}', email='{email}', mobile='{mobile}', password='{password}', area='{area}', location='{location}' WHERE id='{id}'"
        try:
            self.cr.execute(q)
            self.conn.commit()
            msg.showinfo("Success", "center has been updated", parent=self.root)
            self.root1.destroy()
            self.refreshData()  # Refresh the view after update
        except Exception as e:
            msg.showerror("Error", f"Failed to update center: {str(e)}", parent=self.root)
            self.conn.rollback()


if __name__ == "__main__":
    Viewcenter()
