from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect


class report:
    def __init__(self):
        self.root = Tk()
        self.root.state("zoomed")
        self.root.title("Criminal Database || View Report ")
        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.mainColor = '#2c3e50'
        self.secondColor = '#3498db'
        self.textColor = 'white'

        self.root.configure(bg=self.mainColor)

        self.mainlabel = Label(self.root, text="View Report", font=('Helvetica', 28, 'bold'), bg=self.mainColor, fg=self.textColor)
        self.mainlabel.pack(pady=20)

        self.searchFrame = Frame(self.root, bg=self.mainColor)
        self.searchFrame.pack(pady=10)

        self.searchLabel = Label(self.searchFrame, text="Search", font=('Helvetica', 14), bg=self.mainColor, fg=self.textColor)
        self.searchLabel.grid(row=0, column=0, padx=10, pady=20)
        self.searchField = Entry(self.searchFrame, font=('Helvetica', 14))
        self.searchField.grid(row=0, column=1, padx=10, pady=20)
        self.searchBtn = Button(self.searchFrame, text="Search", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.searchreport)
        self.searchBtn.grid(row=0, column=2, padx=10, pady=20)
        self.refreshBtn = Button(self.searchFrame, text="Refresh", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.refreshData)
        self.refreshBtn.grid(row=0, column=3, padx=10, pady=20)
        self.deleteBtn = Button(self.searchFrame, text="Delete", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.deletereport)
        self.deleteBtn.grid(row=0, column=4, padx=10, pady=20)

        self.reportTable = ttk.Treeview(self.root, columns=('id', 'title', 'description', 'date', 'culprit_name', 'mobile', 'email', 'address', 'image'), show="headings", height=15)
        self.reportTable.heading('id', text='id')
        self.reportTable.heading('title', text='title')
        self.reportTable.heading('description', text='description')
        self.reportTable.heading('date', text='date')
        self.reportTable.heading('culprit_name', text='culprit_name')
        self.reportTable.heading('mobile', text='mobile')
        self.reportTable.heading('email', text='email')
        self.reportTable.heading('address', text='address')
        self.reportTable.heading('image', text='image')

        self.reportTable.pack(expand=True, fill='both', padx=20, pady=20)
        self.getreportInfo()

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview.Heading", font=('Helvetica', 14, 'bold'), foreground='#000000')  # Set foreground color to black
        self.style.configure("Treeview", font=('Helvetica', 12), rowheight=40)

        self.reportTable.bind("<Double-1>", self.openUpdateWindow)

        self.root.mainloop()

    def openUpdateWindow(self, event):
        row = self.reportTable.selection()
        row_id = row[0]
        items = self.reportTable.item(row_id)
        data = items['values']

        self.root1 = Toplevel()
        self.root1.geometry("700x600")
        self.mainlabel1 = Label(self.root1, text="Update report", font=('Helvetica', 24, 'bold'), fg="black")
        self.mainlabel1.pack(pady=20)
        self.updateForm = Frame(self.root1)

        font = ('Helvetica', 14)

        self.lb1 = Label(self.updateForm, text="id", font=font, fg="black")
        self.txt1 = Entry(self.updateForm, font=font)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[0])
        self.txt1.configure(state='readonly')

        self.lb2 = Label(self.updateForm, text="title", font=font, fg="black")
        self.txt2 = Entry(self.updateForm, font=font)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[1])

        self.lb3 = Label(self.updateForm, text="description", font=font, fg="black")
        self.txt3 = Entry(self.updateForm, font=font)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[2])

        self.lb4 = Label(self.updateForm, text="date", font=font, fg="black")
        self.txt4 = Entry(self.updateForm, font=font)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)
        self.txt4.insert(0, data[3])

        self.lb5 = Label(self.updateForm, text="culprit_name", fg="black")
        self.txt5 = Entry(self.updateForm, font=font)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.insert(0, data[4])

        self.lb6 = Label(self.updateForm, text="mobile", font=font, fg="black")
        self.txt6 = Entry(self.updateForm, font=font)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6.grid(row=5, column=1, padx=10, pady=10)
        self.txt6.insert(0, data[5])

        self.lb7 = Label(self.updateForm, text="email", font=font, fg="black")
        self.txt7 = Entry(self.updateForm, font=font)
        self.lb7.grid(row=6, column=0, padx=10, pady=10)
        self.txt7.grid(row=6, column=1, padx=10, pady=10)
        self.txt7.insert(0, data[6])

        self.lb8 = Label(self.updateForm, text="address", font=font, fg="black")
        self.txt8 = Entry(self.updateForm, font=font)
        self.lb8.grid(row=7, column=0, padx=10, pady=10)
        self.txt8.grid(row=7, column=1, padx=10, pady=10)
        self.txt8.insert(0, data[7])

        self.lb9 = Label(self.updateForm, text="image", font=font, fg="black")
        self.txt9 = Entry(self.updateForm, font=font)
        self.lb9.grid(row=8, column=0, padx=10, pady=10)
        self.txt9.grid(row=8, column=1, padx=10, pady=10)
        self.txt9.insert(0, data[8])

        self.updateForm.pack(pady=10)

        self.updateBtn = Button(self.root1, text="Update", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.updatereport)
        self.updateBtn.pack(pady=20)

        self.root1.mainloop()

    def updatereport(self):
        id = self.txt1.get()
        title = self.txt2.get()
        description = self.txt3.get()
        date = self.txt4.get()
        culprit_name = self.txt5.get()
        mobile = self.txt6.get()
        email = self.txt7.get()
        address = self.txt8.get()
        image = self.txt9.get()

        q = "UPDATE report SET id=%s, title=%s, description=%s, date=%s, culprit_name=%s, mobile=%s, email=%s, address=%s, image=%s WHERE id=%s"
        self.cr.execute(q, (id, title, description, date, culprit_name, mobile, email, address, image, id))
        self.conn.commit()
        msg.showinfo("Success", "report has been Updated", parent=self.root)
        self.root1.destroy()
        self.refreshData()

    def getreportInfo(self):
        q = "select id, title, description, date, culprit_name, mobile, email, address, image from report"
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.reportTable.get_children():
            self.reportTable.delete(row)

        for i in range(len(result)):
            self.reportTable.insert('', index=i, values=result[i])

    def searchreport(self):
        data = self.searchField.get()
        q = f"select id, title, description, date, culprit_name, mobile, email, address, image from report where title like '%{data}%'"
        print(q)
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.reportTable.get_children():
            self.reportTable.delete(row)

        for i in range(len(result)):
            self.reportTable.insert('', index=i, values=result[i])

    def refreshData(self):
        self.searchField.delete(0, 'end')
        self.getreportInfo()

    def deletereport(self):
        row = self.reportTable.selection()
        if len(row) == 0:
            msg.showwarning("Warning", "Please select the Item", parent=self.root)
        else:
            row_id = row[0]
            items = self.reportTable.item(row_id)
            data = items['values']
            # print(data)
            confirm = msg.askyesno("", "Are you sure you want to delete ?", parent=self.root)
            if confirm:
                q = f"delete from report where id='{data[0]}'"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo("Success", "report has been deleted", parent=self.root)
                self.refreshData()
            else:
                msg.showinfo("Success", "Deletion Aborted", parent=self.root)


if __name__ == "__main__":
    report()
