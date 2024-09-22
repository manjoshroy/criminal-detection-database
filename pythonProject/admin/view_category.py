from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect


class Category:
    def __init__(self):
        self.root = Toplevel()
        self.root.state("zoomed")
        self.root.title("View Category")

        self.conn = Connect()
        self.cr = self.conn.cursor()

        self.mainColor = '#2c3e50'
        self.secondColor = '#3498db'
        self.textColor = 'white'

        self.root.configure(bg=self.mainColor)

        self.mainlabel = Label(self.root, text="View Category", font=('Helvetica', 28, 'bold'), bg=self.mainColor, fg=self.textColor)
        self.mainlabel.pack(pady=20)

        self.searchFrame = Frame(self.root, bg=self.mainColor)
        self.searchFrame.pack(pady=10)

        self.searchLabel = Label(self.searchFrame, text="Search", font=('Helvetica', 14), bg=self.mainColor, fg=self.textColor)
        self.searchLabel.grid(row=0, column=0, padx=10, pady=20)
        self.searchField = Entry(self.searchFrame, font=('Helvetica', 14))
        self.searchField.grid(row=0, column=1, padx=10, pady=20)
        self.searchBtn = Button(self.searchFrame, text="Search", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.searchCategory)
        self.searchBtn.grid(row=0, column=2, padx=10, pady=20)
        self.refreshBtn = Button(self.searchFrame, text="Refresh", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.refreshData)
        self.refreshBtn.grid(row=0, column=3, padx=10, pady=20)
        self.deleteBtn = Button(self.searchFrame, text="Delete", font=('Helvetica', 12), bg=self.secondColor, fg=self.textColor, width=10, command=self.deleteCategory)
        self.deleteBtn.grid(row=0, column=4, padx=10, pady=20)

        self.categoryTable = ttk.Treeview(self.root, columns=('name', 'Description'), show="headings", height=15)
        self.categoryTable.heading('name', text='Name')
        self.categoryTable.heading('Description', text='Description')

        self.categoryTable.pack(expand=True, fill='both', padx=20, pady=20)
        self.getCategoryInfo()

        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("Treeview.Heading", font=('Helvetica', 14, 'bold'), foreground='#000000')  # Set foreground color to black
        self.style.configure("Treeview", font=('Helvetica', 12), rowheight=40)

        self.categoryTable.bind("<Double-1>", self.openUpdateWindow)

        self.root.mainloop()

    def getCategoryInfo(self):
        q = "SELECT name, description FROM category"
        self.cr.execute(q)
        result = self.cr.fetchall()

        for row in self.categoryTable.get_children():
            self.categoryTable.delete(row)

        for i, row_data in enumerate(result):
            self.categoryTable.insert('', index=i, values=row_data)

    def searchCategory(self):
        data = self.searchField.get()
        try:
            q = f"SELECT name, description FROM category WHERE name LIKE '%{data}%'"
            self.cr.execute(q)
            result = self.cr.fetchall()

            for row in self.categoryTable.get_children():
                self.categoryTable.delete(row)

            for i, row_data in enumerate(result):
                self.categoryTable.insert('', index=i, values=row_data)
        except Exception as e:
            msg.showerror("Error", f"Failed to search category: {str(e)}", parent=self.root)
            self.conn.rollback()

    def refreshData(self):
        self.searchField.delete(0, 'end')
        self.getCategoryInfo()

    def deleteCategory(self):
        row = self.categoryTable.selection()
        if len(row) == 0:
            msg.showwarning("Warning", "Please select the Item", parent=self.root)
        else:
            row_id = row[0]
            items = self.categoryTable.item(row_id)
            data = items['values']
            confirm = msg.askyesno("", "Are you sure you want to delete ?", parent=self.root)
            if confirm:
                q = f"DELETE FROM category WHERE name='{data[0]}'"
                self.cr.execute(q)
                self.conn.commit()
                msg.showinfo("Success", "Category has been deleted", parent=self.root)
                self.refreshData()
            else:
                msg.showinfo("Success", "Deletion Aborted", parent=self.root)

    def openUpdateWindow(self, event):
        row = self.categoryTable.selection()
        row_id = row[0]
        items = self.categoryTable.item(row_id)
        data = items['values']

        self.root1 = Toplevel()
        self.root1.geometry("700x600")

        self.mainlabel1 = Label(self.root1, text="Update Category", font=('', 24, 'bold'), fg="black")
        self.mainlabel1.pack(pady=20)

        self.updateForm = Frame(self.root1, bg=self.mainColor)

        font = ('', 14)

        self.lb1 = Label(self.updateForm, text="Name", font=font, bg=self.mainColor, fg=self.textColor)
        self.txt1 = Entry(self.updateForm, font=font)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1.grid(row=0, column=1, padx=10, pady=10)
        self.txt1.insert(0, data[0])

        self.lb2 = Label(self.updateForm, text="Description", font=font, bg=self.mainColor, fg=self.textColor)
        self.txt2 = Entry(self.updateForm, font=font)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)
        self.txt2.insert(0, data[1])

        self.updateForm.pack(pady=10)

        self.updateBtn = Button(self.root1, text="Update", font=('', 12), width=10, command=self.updateCategory, bg=self.secondColor, fg=self.textColor)
        self.updateBtn.pack(pady=20)

        self.root1.mainloop()

    def updateCategory(self):
        name = self.txt1.get()
        description = self.txt2.get()

        q = f"UPDATE category SET name='{name}', description='{description}' WHERE name='{name}'"
        try:
            self.cr.execute(q)
            self.conn.commit()
            msg.showinfo("Success", "Category has been updated", parent=self.root)
            self.root1.destroy()
            self.refreshData()  # Refresh the view after update
        except Exception as e:
            msg.showerror("Error", f"Failed to update category: {str(e)}", parent=self.root)
            self.conn.rollback()


if __name__ == "__main__":
    Category()
