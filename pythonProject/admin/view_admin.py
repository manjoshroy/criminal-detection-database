from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect


class ViewAdmin:
    def __init__(self):
        self.root = Toplevel()
        self.root.title("Criminal Database || View Admin")
        self.root.state("zoomed")

        self.conn = Connect()
        self.cr = self.conn.cursor()

        # Main color scheme
        self.mainColor = '#2c3e50'
        self.textColor = 'black'
        self.buttonColor = 'blue'
        self.entryColor = '#E3F2FD'

        # Create a frame for the top area
        self.top_frame = Frame(self.root, background=self.mainColor)
        self.top_frame.pack(fill=X)

        # Create the main label inside the top frame
        self.mainlabel = Label(self.top_frame, text="View Admin", font=('', 28, 'bold'), background=self.mainColor, fg="white")
        self.mainlabel.pack(pady=20, fill=X)

        # Create a frame for the buttons
        self.button_frame = Frame(self.top_frame, background=self.mainColor)
        self.button_frame.pack(pady=10)

        self.searchLabel = Label(self.button_frame, text="Search", font=('', 14), background=self.mainColor, fg="white")
        self.searchLabel.pack(side=LEFT, padx=10, pady=20)

        self.searchField = Entry(self.button_frame, font=('', 14), bg=self.entryColor)
        self.searchField.pack(side=LEFT, padx=10, pady=20)

        self.searchBtn = Button(self.button_frame, text="Search", font=('', 12), width=10, command=self.searchAdmin, bg=self.buttonColor, fg="white")
        self.searchBtn.pack(side=LEFT, padx=10, pady=20)

        self.refreshBtn = Button(self.button_frame, text="Refresh", font=('', 12), width=10, command=self.refreshData, bg=self.buttonColor, fg="white")
        self.refreshBtn.pack(side=LEFT, padx=10, pady=20)

        self.deleteBtn = Button(self.button_frame, text="Delete", font=('', 12), width=10, command=self.deleteAdmin, bg=self.buttonColor, fg="white")
        self.deleteBtn.pack(side=LEFT, padx=10, pady=20)

        self.adminTable = ttk.Treeview(self.root, columns=('id', 'name', 'email', 'mobile', 'role'))
        self.adminTable.heading('id', text='Admin ID')
        self.adminTable.heading('name', text='Name')
        self.adminTable.heading('email', text='Email')
        self.adminTable.heading('mobile', text='Mobile')
        self.adminTable.heading('role', text='Role')
        self.adminTable['show'] = 'headings'
        self.adminTable.column('id', width=10)
        self.adminTable.pack(expand=True, fill='both', padx=20, pady=20)

        self.getAdminInfo()

        # Styling the Treeview
        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=("", 14, 'bold'), background=self.mainColor, foreground=self.textColor)
        self.style.configure("Treeview", font=("", 14), rowheight=50, background=self.entryColor)

        self.adminTable.bind("<Double-1>", self.openUpdateWindow)

        self.root.mainloop()

    def openUpdateWindow(self, event):
        row = self.adminTable.selection()
        row_id = row[0]
        items = self.adminTable.item(row_id)
        data = items['values']

        self.root1 = Toplevel()
        self.root1.geometry("700x600")

        self.mainlabel1 = Label(self.root1, text="Update Admin", font=('', 24, 'bold'), fg="black")
        self.mainlabel1.pack(pady=20)
        self.updateForm = Frame(self.root1, background="white")

        font = ('', 14)

        self.lb1 = Label(self.updateForm, text="Admin ID", font=font, fg=self.textColor)
        self.txt1 = Entry(self.updateForm, font=font)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[0])
        self.txt1.configure(state='readonly')

        self.lb2 = Label(self.updateForm, text="Admin Name", font=font, fg=self.textColor)
        self.txt2 = Entry(self.updateForm, font=font)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[1])

        self.lb3 = Label(self.updateForm, text="Admin Email", font=font, fg=self.textColor)
        self.txt3 = Entry(self.updateForm, font=font)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[2])

        self.lb4 = Label(self.updateForm, text="Admin Mobile", font=font, fg=self.textColor)
        self.txt4 = Entry(self.updateForm, font=font)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)
        self.txt4.insert(0, data[3])

        self.lb5 = Label(self.updateForm, text="Admin Role", font=font, fg=self.textColor)
        self.txt5 = ttk.Combobox(self.updateForm, font=font, values=['Super Admin', 'Admin'], state='readonly')
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.set(data[4])

        self.updateForm.pack(pady=10)

        self.updateBtn = Button(self.root1, text="Update", font=('', 12), width=10, command=self.updateAdmin, bg=self.buttonColor, fg="white")
        self.updateBtn.pack(pady=20)

        self.root1.mainloop()

    def updateAdmin(self):
        id = self.txt1.get()
        name = self.txt2.get()
        email = self.txt3.get()
        mobile = self.txt4.get()
        role = self.txt5.get()

        q = f"update add_admin set name='{name}', email='{email}', mobile='{mobile}', role='{role}' where id='{id}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo("Success", "Admin has been Updated", parent=self.root)
        self.root1.destroy()
        self.refreshData()

    def getAdminInfo(self):
        q = "select id, name, email, mobile, role from add_admin"
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.adminTable.get_children():
            self.adminTable.delete(row)

        for i in range(len(result)):
            self.adminTable.insert('', index=i, values=result[i])

    def searchAdmin(self):
        data = self.searchField.get()
        q = f"select id, name, email, mobile, role from add_admin where name like '%{data}%'"
        print(q)
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.adminTable.get_children():
            self.adminTable.delete(row)

        for i in range(len(result)):
            self.adminTable.insert('', index=i, values=result[i])

    def refreshData(self):
        self.searchField.delete(0, 'end')
        self.getAdminInfo()

    def deleteAdmin(self):
        row = self.adminTable.selection()
        if len(row) == 0:
            msg.showwarning("Warning", "Please select the Item", parent=self.root)
        else:
            row_id = row[0]
            items = self.adminTable.item(row_id)
            data = items['values']
            confirm = msg.askyesno("", "Are you sure you want to delete ?", parent=self.root)
            if confirm:
                q = f"delete from add_admin where id='{data[0]}'"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo("Success", "Admin has been deleted", parent=self.root)
                self.refreshData()
            else:
                msg.showinfo("Success", "Deletion Aborted", parent=self.root)


if __name__ == "__main__":
    ViewAdmin()