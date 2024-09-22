from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect


class viewidentifycriminal:
    def __init__(self):
        self.root = Tk()
        self.root.state("zoomed")
        self.root.title("Criminal Database || View Identify Criminal ")
        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.mainColor = '#2c3e50'
        self.secondColor = '#3498db'
        self.textColor = 'white'

        self.root.configure(bg=self.mainColor)

        self.mainlabel = Label(self.root, text="View Identify Criminal", font=('Helvetica', 28, 'bold'), bg=self.mainColor, fg=self.textColor)
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

        self.reportTable = ttk.Treeview(self.root, columns=('id', 'criminal_name', 'criminal_id', 'center_id', 'date', 'time'), show="headings", height=15)
        self.reportTable.heading('id', text='id')
        self.reportTable.heading('criminal_name', text='criminal_name')
        self.reportTable.heading('criminal_id', text='criminal_id')
        self.reportTable.heading('center_id', text='center_id')
        self.reportTable.heading('date', text='date')
        self.reportTable.heading('time', text='time')

        self.reportTable.pack(expand=True, fill='both', padx=20, pady=20)
        self.getreportInfo()

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview.Heading", font=('Helvetica', 14, 'bold'), foreground='#000000')
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
        self.mainlabel1 = Label(self.root1, text="Update identify criminal", font=('Helvetica', 24, 'bold'), fg="black")
        self.mainlabel1.pack(pady=20)
        self.updateForm = Frame(self.root1)

        font = ('Helvetica', 14)

        self.lb1 = Label(self.updateForm, text="id", font=font, fg="black")
        self.txt1 = Entry(self.updateForm, font=font)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[0])
        self.txt1.configure(state='readonly')

        self.lb2 = Label(self.updateForm, text="criminal_name", font=font, fg="black")
        self.txt2 = Entry(self.updateForm, font=font)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[1])

        self.lb3 = Label(self.updateForm, text="criminal_id", font=font, fg="black")
        self.txt3 = Entry(self.updateForm, font=font)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[2])

        self.lb4 = Label(self.updateForm, text="center_id", font=font, fg="black")
        self.txt4 = Entry(self.updateForm, font=font)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)
        self.txt4.insert(0, data[3])

        self.lb5 = Label(self.updateForm, text="date", fg="black")
        self.txt5 = Entry(self.updateForm, font=font)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.insert(0, data[4])

        self.lb6 = Label(self.updateForm, text="time", font=font, fg="black")
        self.txt6 = Entry(self.updateForm, font=font)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6.grid(row=5, column=1, padx=10, pady=10)
        self.txt6.insert(0, data[5])

        self.updateForm.pack(pady=10)

        self.updateBtn = Button(self.root1, text="Update", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.updatereport)
        self.updateBtn.pack(pady=20)

        self.root1.mainloop()

    def updatereport(self):
        id = self.txt1.get()
        criminal_name = self.txt2.get()
        criminal_id = self.txt3.get()
        center_id = self.txt4.get()
        date = self.txt5.get()
        time = self.txt6.get()

        q = "UPDATE remarks SET id=%s, criminal_name=%s, criminal_id=%s ,center_id=%s, date=%s, time=%s WHERE id=%s"
        self.cr.execute(q, (id, criminal_name, criminal_id, center_id, date, time, id))
        self.conn.commit()
        msg.showinfo("Success", "identify criminal has been Updated", parent=self.root)
        self.root1.destroy()
        self.refreshData()

    def getreportInfo(self):
        q = "select id, criminal_name, criminal_id, center_id, date, time from remarks"
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.reportTable.get_children():
            self.reportTable.delete(row)

        for i in range(len(result)):
            self.reportTable.insert('', index=i, values=result[i])

    def searchreport(self):
        data = self.searchField.get()
        q = f" select id, criminal_name, criminal_id, center_id, date, time from remarks where criminal_id like '%{data}%'"
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
                q = f"delete from remarks where id='{data[0]}'"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo("Success", "identify criminal has been deleted", parent=self.root)
                self.refreshData()
            else:
                msg.showinfo("Success", "Deletion Aborted", parent=self.root)


if __name__ == "__main__":
    viewidentifycriminal()
