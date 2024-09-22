from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect


class criminal:
    def __init__(self):
        self.root = Tk()
        self.root.state("zoomed")
        self.root.title("Criminal Database || View Criminal")
        self.conn = Connect()
        self.cr = self.conn.cursor()
        self.mainColor = '#2c3e50'
        self.secondColor = '#3498db'
        self.textColor = 'white'

        self.root.configure(bg=self.mainColor)

        self.mainlabel = Label(self.root, text="View Criminal", font=('Helvetica', 28, 'bold'), bg=self.mainColor, fg=self.textColor)
        self.mainlabel.pack(pady=20)

        self.searchFrame = Frame(self.root, bg=self.mainColor)
        self.searchFrame.pack(pady=10)

        self.searchLabel = Label(self.searchFrame, text="Search", font=('Helvetica', 14), bg=self.mainColor, fg=self.textColor)
        self.searchLabel.grid(row=0, column=0, padx=10, pady=20)
        self.searchField = Entry(self.searchFrame, font=('Helvetica', 14))
        self.searchField.grid(row=0, column=1, padx=10, pady=20)
        self.searchBtn = Button(self.searchFrame, text="Search", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.searchcriminal)
        self.searchBtn.grid(row=0, column=2, padx=10, pady=20)
        self.refreshBtn = Button(self.searchFrame, text="Refresh", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.refreshData)
        self.refreshBtn.grid(row=0, column=3, padx=10, pady=20)
        self.deleteBtn = Button(self.searchFrame, text="Delete", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.deletecriminal)
        self.deleteBtn.grid(row=0, column=4, padx=10, pady=20)

        self.criminalTable = ttk.Treeview(self.root, columns=('id', 'Name', 'Email', 'Mobile', 'FatherName', 'Address', 'Image'), show="headings", height=15)
        self.criminalTable.heading('id', text='id')
        self.criminalTable.heading('Name', text='Name')
        self.criminalTable.heading('Email', text='Email')
        self.criminalTable.heading('Mobile', text='Mobile')
        self.criminalTable.heading('FatherName', text='FatherName')
        self.criminalTable.heading('Address', text='Address')
        self.criminalTable.heading('Image', text='Image')
        self.criminalTable.column('id',width=11)
        self.criminalTable.column('Name',width=55)
        self.criminalTable.column('FatherName', width=85)


        self.criminalTable.pack(expand=True, fill='both', padx=20, pady=20)
        self.getcriminalInfo()

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview.Heading", font=('Helvetica', 14, 'bold'), foreground='#000000')  # Set foreground color to black
        self.style.configure("Treeview", font=('Helvetica', 12), rowheight=40)

        self.criminalTable.bind("<Double-1>", self.openUpdateWindow)

        self.root.mainloop()

    def openUpdateWindow(self, event):
        row = self.criminalTable.selection()
        row_id = row[0]
        items = self.criminalTable.item(row_id)
        data = items['values']

        self.root1 = Toplevel()
        self.root1.geometry("700x600")

        self.mainlabel1 = Label(self.root1, text="Update criminal", font=('', 24, 'bold'))
        self.mainlabel1.pack(pady=20)

        self.updateForm = Frame(self.root1)

        font = ('', 14)

        self.lb1 = Label(self.updateForm, text="id", font=font)
        self.txt1 = Entry(self.updateForm, font=font)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[0])
        self.txt1.configure(state='readonly')

        self.lb2 = Label(self.updateForm, text="Name", font=font)
        self.txt2 = Entry(self.updateForm, font=font)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[1])

        self.lb3 = Label(self.updateForm, text="Email", font=font)
        self.txt3 = Entry(self.updateForm, font=font)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[2])

        self.lb4 = Label(self.updateForm, text="Mobile", font=font)
        self.txt4 = Entry(self.updateForm, font=font)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)
        self.txt4.insert(0, data[3])

        self.lb5 = Label(self.updateForm, text="FatherName", font=font)
        self.txt5 = Entry(self.updateForm, font=font)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.insert(0, data[4])

        self.lb6 = Label(self.updateForm, text="Address", font=font)
        self.txt6 = Entry(self.updateForm, font=font)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6.grid(row=5, column=1, padx=10, pady=10)
        self.txt6.insert(0, data[5])

        self.lb7 = Label(self.updateForm, text="Image", font=font)
        self.txt7 = Entry(self.updateForm, font=font)
        self.lb7.grid(row=6, column=0, padx=10, pady=10)
        self.txt7.grid(row=6, column=1, padx=10, pady=10)
        self.txt7.insert(0, data[6])

        self.updateForm.pack(pady=10)

        self.updateBtn = Button(self.root1, text="Update", font=('', 12), width=10, command=self.updatecriminal)
        self.updateBtn.pack(pady=20)

        self.root1.mainloop()

    def updatecriminal(self):
        id = self.txt1.get()
        name = self.txt2.get()
        email = self.txt3.get()
        mobile = self.txt4.get()
        father_name = self.txt5.get()
        address = self.txt6.get()
        image = self.txt7.get()

        q = (f"update criminals set id='{id}', name='{name}', email='{email}' , mobile='{mobile}' , "
             f"father_name='{father_name}', address='{address}' , image='{image}' where id='{id}'")

        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo("Success", "criminal has been Updated", parent=self.root)
        self.root1.destroy()
        self.refreshData()

    def getcriminalInfo(self):
        q = "select id, name, email, mobile, father_name, address, image from criminals"
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.criminalTable.get_children():
            self.criminalTable.delete(row)

        for i in range(len(result)):
            self.criminalTable.insert('', index=i, values=result[i])

    def searchcriminal(self):
        data = self.searchField.get()
        q = f" select id, name, email, mobile, father_name, address, image from criminals where name like '%{data}%'"
        print(q)
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.criminalTable.get_children():
            self.criminalTable.delete(row)

        for i in range(len(result)):
            self.criminalTable.insert('', index=i, values=result[i])

    def refreshData(self):
        self.searchField.delete(0, 'end')
        self.getcriminalInfo()

    def deletecriminal(self):
        row = self.criminalTable.selection()
        if len(row) == 0:
            msg.showwarning("Warning", "Please select the Item", parent=self.root)
        else:
            row_id = row[0]
            items = self.criminalTable.item(row_id)
            data = items['values']
            # print(data)
            confirm = msg.askyesno("", "Are you sure you want to delete ?", parent=self.root)
            if confirm:
                q = f"delete from criminals where id='{data[0]}'"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo("Success", "criminal has been deleted", parent=self.root)
                self.refreshData()
            else:
                msg.showinfo("Success", "Deletion Aborted", parent=self.root)


if __name__ == "__main__":
    criminal()
