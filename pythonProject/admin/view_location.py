from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect


class location:
    def __init__(self):
        self.root = Tk()
        self.root.state("zoomed")
        self.root.title("Criminal Database || View location")
        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.mainColor = '#2c3e50'
        self.secondColor = '#3498db'
        self.textColor = 'white'

        self.root.configure(bg=self.mainColor)

        self.mainlabel = Label(self.root, text="View location", font=('Helvetica', 28, 'bold'), bg=self.mainColor, fg=self.textColor)
        self.mainlabel.pack(pady=20)

        self.searchFrame = Frame(self.root, bg=self.mainColor)
        self.searchFrame.pack(pady=10)

        self.searchLabel = Label(self.searchFrame, text="Search", font=('Helvetica', 14), bg=self.mainColor, fg=self.textColor)
        self.searchLabel.grid(row=0, column=0, padx=10, pady=20)
        self.searchField = Entry(self.searchFrame, font=('Helvetica', 14))
        self.searchField.grid(row=0, column=1, padx=10, pady=20)
        self.searchBtn = Button(self.searchFrame, text="Search", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.searchlocation)
        self.searchBtn.grid(row=0, column=2, padx=10, pady=20)
        self.refreshBtn = Button(self.searchFrame, text="Refresh", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.refreshData)
        self.refreshBtn.grid(row=0, column=3, padx=10, pady=20)
        self.deleteBtn = Button(self.searchFrame, text="Delete", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.deletelocation)
        self.deleteBtn.grid(row=0, column=4, padx=10, pady=20)

        self.locationTable = ttk.Treeview(self.root, columns=('LocationName', 'Description', 'LocationArea', 'Timings'), show="headings", height=15)
        self.locationTable.heading('LocationName', text='LocationName')
        self.locationTable.heading('Description', text='Description')
        self.locationTable.heading('LocationArea', text='LocationArea')
        self.locationTable.heading('Timings', text='Timings')

        self.locationTable.pack(expand=True, fill='both', padx=20, pady=20)
        self.getlocationInfo()

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview.Heading", font=('Helvetica', 14, 'bold'), foreground='#000000')  # Set foreground color to black
        self.style.configure("Treeview", font=('Helvetica', 12), rowheight=40)

        self.locationTable.bind("<Double-1>", self.openUpdateWindow)

        self.root.mainloop()

    def openUpdateWindow(self, event):
        row = self.locationTable.selection()
        row_id = row[0]
        items = self.locationTable.item(row_id)
        data = items['values']

        self.root1 = Toplevel()
        self.root1.geometry("700x600")

        self.mainlabel1 = Label(self.root1, text="Update location", font=('Helvetica', 24, 'bold'))
        self.mainlabel1.pack(pady=20)

        self.updateForm = Frame(self.root1)

        font = ('Helvetica', 14)

        self.lb1 = Label(self.updateForm, text="LocationName", font=font, fg="black")
        self.txt1 = Entry(self.updateForm, font=font)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[0])
        self.txt1.configure(state='readonly')

        self.lb2 = Label(self.updateForm, text="Description", font=font, fg="black")
        self.txt2 = Entry(self.updateForm, font=font)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[1])

        self.lb3 = Label(self.updateForm, text="LocationArea", font=font, fg="black")
        self.txt3 = ttk.Combobox(self.updateForm,  width=30, values=self.getArea(), state='readonly')
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3.grid(row=2, column=1, padx=10, pady=10)
        self.txt3.insert(0, data[2])

        self.lb4 = Label(self.updateForm, text="Timings", font=font, fg="black")
        self.txt4 = Entry(self.updateForm, font=font)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4.grid(row=3, column=1, padx=10, pady=10)
        self.txt4.insert(0, data[3])

        self.updateForm.pack(pady=10)

        self.updateBtn = Button(self.root1, text="Update", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.updatelocation)
        self.updateBtn.pack(pady=20)

        self.root1.mainloop()

    def getArea(self):
        conn = Connect()
        cr = conn.cursor()
        q = f"select * from add_area"
        cr.execute(q)
        result = cr.fetchall()
        list = []
        for i in result:
            list.append(i[0])
        return list

    def updatelocation(self):
        location_name = self.txt1.get()
        description = self.txt2.get()
        new_location_area = self.txt3.get()  # New value for location_area
        timings = self.txt4.get()

        # Check if the new_location_area exists in the location table
        q_check_area = f"SELECT * FROM location1 WHERE location_area='{new_location_area}'"
        self.cr.execute(q_check_area)
        result = self.cr.fetchone()

        if result:
            # Update the record in the location table
            q_update_location = f"UPDATE location1 SET description='{description}', location_area='{new_location_area}', timings='{timings}' WHERE location_name='{location_name}'"
            self.cr.execute(q_update_location)
            self.conn.commit()
            msg.showinfo("Success", "Location has been updated", parent=self.root)
            self.root1.destroy()
            self.refreshData()
        else:
            msg.showerror("Error", f"The new location area '{new_location_area}' does not exist in the database", parent=self.root)

    def getlocationInfo(self):
        q = "select location_name, description, location_area, timings from location1"
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.locationTable.get_children():
            self.locationTable.delete(row)

        for i in range(len(result)):
            self.locationTable.insert('', index=i, values=result[i])

    def searchlocation(self):
        data = self.searchField.get()
        q = f"select  * from location1 where location_name like '%{data}%'"
        self.cr.execute(q)
        result = self.cr.fetchall()
        for row in self.locationTable.get_children():
            self.locationTable.delete(row)
        for i in range(len(result)):
            self.locationTable.insert('', index=i, values=result[i])

    def refreshData(self):
        self.getlocationInfo()

    def deletelocation(self):
        row = self.locationTable.selection()
        if len(row) == 0:
            msg.showwarning("Warning", "Please select the Item", parent=self.root)
        else:
            row_id = row[0]
            items = self.locationTable.item(row_id)
            data = items['values']
            confirm = msg.askyesno("", "Are you sure you want to delete ?", parent=self.root)
            if confirm:
                q = f"delete from location1 where location_name='{data[0]}'"
                print(q)
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo("Success", "location has been deleted", parent=self.root)
                self.refreshData()
            else:
                msg.showinfo("Success", "Deletion Aborted", parent=self.root)


if __name__ == '__main__':
    location()
