from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect


class area:
    def __init__(self):
        self.root = Tk()
        self.root.state("zoomed")
        self.root.title("Criminal Database || View Area ")

        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.mainColor = '#2c3e50'
        self.secondColor = '#3498db'
        self.textColor = 'white'

        self.root.configure(bg=self.mainColor)

        self.mainlabel = Label(self.root, text="View Area", font=('Helvetica', 28, 'bold'), bg=self.mainColor, fg=self.textColor)
        self.mainlabel.pack(pady=20)

        self.searchFrame = Frame(self.root, bg=self.mainColor)
        self.searchFrame.pack(pady=10)

        self.searchLabel = Label(self.searchFrame, text="Search", font=('Helvetica', 14), bg=self.mainColor, fg=self.textColor)
        self.searchLabel.grid(row=0, column=0, padx=10, pady=20)
        self.searchField = Entry(self.searchFrame, font=('Helvetica', 14))
        self.searchField.grid(row=0, column=1, padx=10, pady=20)
        self.searchBtn = Button(self.searchFrame, text="Search", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.searchArea)
        self.searchBtn.grid(row=0, column=2, padx=10, pady=20)
        self.refreshBtn = Button(self.searchFrame, text="Refresh", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.refreshData)
        self.refreshBtn.grid(row=0, column=3, padx=10, pady=20)
        self.deleteBtn = Button(self.searchFrame, text="Delete", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.deleteArea)
        self.deleteBtn.grid(row=0, column=4, padx=10, pady=20)

        self.AreaTable = ttk.Treeview(self.root, columns=('AreaName', 'CityName', 'StateName', 'LandMark'))
        self.AreaTable.heading('AreaName', text='AreaName')
        self.AreaTable.heading('CityName', text='CityName')
        self.AreaTable.heading('StateName', text='StateName')
        self.AreaTable.heading('LandMark', text='LandMark')
        self.AreaTable['show'] = 'headings'
        self.AreaTable.column('AreaName', width=10)

        self.AreaTable.pack(expand=True, fill='both', padx=20, pady=20)
        self.getAreaInfo()

        self.style = ttk.Style()
        self.style.configure("Treeview.Heading", font=('Helvetica', 14, 'bold'), foreground='#000000')  # Set foreground color to black
        self.style.configure("Treeview", font=('Helvetica', 14), rowheight=50)

        self.AreaTable.bind("<Double-1>", self.openUpdateWindow)

        self.root.mainloop()

    def openUpdateWindow(self, event):
        row = self.AreaTable.selection()
        row_id = row[0]
        items = self.AreaTable.item(row_id)
        data = items['values']

        self.root1 = Toplevel()
        self.root1.geometry("700x600")

        self.mainlabel1 = Label(self.root1, text="Update Area", font=('', 24, 'bold'), fg="black")
        self.mainlabel1.pack(pady=20)

        self.updateForm = Frame(self.root1, bg=self.mainColor)

        font = ('', 14)

        self.lb1 = Label(self.updateForm, text="AreaName", font=font, bg=self.mainColor, fg=self.textColor)
        self.txt1 = Entry(self.updateForm, font=font)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[0])
        self.txt1.configure(state='readonly')

        self.lb2 = Label(self.updateForm, text="CityName", font=font, bg=self.mainColor, fg=self.textColor)
        self.txt2 = Entry(self.updateForm, font=font)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[1])

        self.lb3 = Label(self.updateForm, text="StateName", font=font, bg=self.mainColor, fg=self.textColor)
        self.txt3 = Entry(self.updateForm, font=font)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[2])

        self.lb4 = Label(self.updateForm, text="LandMark", font=font, bg=self.mainColor, fg=self.textColor)
        self.txt4 = Entry(self.updateForm, font=font)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)
        self.txt4.insert(0, data[3])

        self.updateForm.pack(pady=10)

        self.updateBtn = Button(self.root1, text="Update", font=('', 12), width=10, command=self.updateArea, bg=self.secondColor, fg=self.textColor)
        self.updateBtn.pack(pady=20)

        self.root1.mainloop()

    def updateArea(self):
        area_name = self.txt1.get()
        city_name = self.txt2.get()
        state_name = self.txt3.get()
        land_mark = self.txt4.get()

        # Assuming 'area_name' is the primary key or unique identifier
        q = f"UPDATE add_area SET city_name='{city_name}', state_name='{state_name}', land_mark='{land_mark}' WHERE area_name='{area_name}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo("Success", "Area has been Updated.", parent=self.root)
        self.root1.destroy()
        self.refreshData()

    def getAreaInfo(self):
        q = "select area_name, city_name, state_name, land_mark from add_area"
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.AreaTable.get_children():
            self.AreaTable.delete(row)

        for i in range(len(result)):
            self.AreaTable.insert('', index=i, values=result[i])

    def searchArea(self):
        data = self.searchField.get()
        q = f"select * from add_area where area_name like '%{data}%'"
        print(q)
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.AreaTable.get_children():
            self.AreaTable.delete(row)

        for i in range(len(result)):
            self.AreaTable.insert('', index=i, values=result[i])

    def refreshData(self):
        self.searchField.delete(0, 'end')
        self.getAreaInfo()

    def deleteArea(self):
        row = self.AreaTable.selection()
        if len(row) == 0:
            msg.showwarning("Warning", "Please select the Item", parent=self.root)
        else:
            row_id = row[0]
            items = self.AreaTable.item(row_id)
            data = items['values']
            confirm = msg.askyesno("", "Are you sure you want to delete ?", parent=self.root)
            if confirm:
                q = f"delete from add_area where area_name='{data[0]}'"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo("Success", "Area has been deleted", parent=self.root)
                self.refreshData()
            else:
                msg.showinfo("Success", "Deletion Aborted", parent=self.root)


if __name__ == "__main__":
    area()