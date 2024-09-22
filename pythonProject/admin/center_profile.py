import tkinter
import tkinter.messagebox as msg
from PIL import Image, ImageTk
from connection import Connect


class CenterProfile:
    def __init__(self, center_id):
        self.id = center_id
        self.root = tkinter.Toplevel()
        self.root.title("Manage Profile")
        self.root.state('zoomed')

        self.mainColor = '#444b6e'
        self.secondColor = '#8d95b9'
        self.thirdColor = '#272c3f'

        self.font = ('', 15, 'bold')
        self.font1 = ('', 15)
        self.root.configure(bg=self.mainColor)
        self.mainLabel = tkinter.Label(self.root, text="Center Profile", relief="solid", borderwidth=4, font=("Arial", 35, 'bold'))
        self.mainLabel.pack(pady=10, padx=10)

        width = int(self.root.winfo_screenwidth())
        height = int(self.root.winfo_screenheight())

        # Parent frame with black background
        self.parent_frame = tkinter.Frame(self.root, bg="black", padx=10, pady=10)
        self.parent_frame.pack(fill=tkinter.BOTH, expand=True)

        self.frame = tkinter.Frame(self.parent_frame, highlightthickness=2, bg="white", padx=10, pady=10)
        self.frame.pack(fill=tkinter.BOTH, expand=True, padx=15, pady=15)

        # Frame on the left side with increased width and height
        self.frame1 = tkinter.Frame(self.frame, bg="grey", width=width // 1.2, height=height // 1.2)  # Increased width and height
        self.frame1.grid(row=0, column=0, padx=15, pady=15, sticky="nsew")

        # Load and display the image with black highlight
        img = Image.open('C:\\Users\\manjo\\Downloads\\sgykcbywk.jpg')
        img = img.resize((width // 2, height // 2))  # Resize to fit the frame
        bg = ImageTk.PhotoImage(img)

        self.image_label = tkinter.Label(self.frame1, image=bg, highlightthickness=2, highlightbackground="black")
        self.image_label.image = bg
        self.image_label.pack(fill='both', expand=True)

        # Frame on the right side with increased width and height
        self.frame2 = tkinter.Frame(self.frame, bg="grey", width=width // 1.5, height=height // 1.2)  # Increased width and height
        self.frame2.grid(row=0, column=1, padx=15, pady=15, sticky="nsew")

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)

        self.lb1 = tkinter.Label(self.frame2, text="Center Name", relief="solid", font=self.font, borderwidth=4, padx=5, pady=5)
        self.lb1.grid(row=0, column=0, padx=10, pady=5, sticky="w")  # Align left

        self.lb2 = tkinter.Label(self.frame2, text="Enter Email", relief="solid", borderwidth=4, font=self.font, padx=5, pady=5)
        self.lb2.grid(row=1, column=0, pady=10, padx=10, sticky="w")  # Align left

        self.lb3 = tkinter.Label(self.frame2, text="Mobile", relief="solid", borderwidth=4, font=self.font, padx=5, pady=5)
        self.lb3.grid(row=2, column=0, pady=10, padx=10, sticky="w")  # Align left

        # Entries
        self.txt1 = tkinter.Entry(self.frame2, font=self.font1, width=30, relief="solid", borderwidth=4)
        self.txt1.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.txt2 = tkinter.Entry(self.frame2, font=self.font1, width=30, relief="solid", borderwidth=4)
        self.txt2.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.txt3 = tkinter.Entry(self.frame2, font=self.font1, width=30, relief="solid", borderwidth=4)
        self.txt3.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        # Button
        self.btn = tkinter.Button(self.frame2, text="Submit", font=self.font, width=15, relief="solid", borderwidth=5, command=self.add_center)
        self.btn.grid(row=3, column=1, pady=20)

        self.load_data()

        self.root.mainloop()

    def load_data(self):
        try:
            conn = Connect()
            cr = conn.cursor()
            query = f"SELECT name, email, mobile FROM add_center WHERE id={self.id}"
            cr.execute(query)
            data = cr.fetchone()
            if data:
                self.txt1.insert(0, data[0])
                self.txt2.insert(0, data[1])
                self.txt3.insert(0, data[2])
            else:
                msg.showwarning("No Data", "No data found for the given ID", parent=self.root)
            cr.close()
            conn.close()
        except Exception as e:
            msg.showerror("Error", f"An error occurred while fetching data: {e}", parent=self.root)
            print(f"Error fetching data: {e}")

    def add_center(self):
        try:
            conn = Connect()
            cr = conn.cursor()
            center_name = self.txt1.get()
            email = self.txt2.get()
            mobile = self.txt3.get()

            if len(center_name) == 0 or len(email) == 0 or len(mobile) == 0:
                msg.showwarning("Warning", "Please enter all the fields", parent=self.root)
            else:
                query = f"UPDATE add_center SET name='{center_name}', email='{email}', mobile='{mobile}' WHERE id={self.id}"
                cr.execute(query)
                conn.commit()
                msg.showinfo("Success", "Center updated successfully", parent=self.root)
                self.txt1.delete(0, 'end')
                self.txt2.delete(0, 'end')
                self.txt3.delete(0, 'end')
            cr.close()
            conn.close()
        except Exception as e:
            conn.rollback()
            msg.showerror("Error", f"An error occurred: {e}", parent=self.root)
            print(f"Error updating data: {e}")


center_id = 2
#obj = CenterProfile(center_id)
