import datetime
from tkinter import *
from PIL import Image, ImageTk
import cv2
from deepface import DeepFace
import os
import tkinter.messagebox as msg
from connection import Connect
import tkinter
from email_validate import sendEmail


class identifycriminal:

    def __init__(self, data):
        self.center_id = data
        print(self.center_id)
        self.root = Toplevel()
        self.root.title("Criminal Detection || Add Remark")
        self.root.state("zoomed")

        self.font = ('Times New Roman', 14)
        self.font1 = ('Times New Roman', 16, 'bold')

        self.mainBackground = "#2c3e50"
        self.frameBackground = "#B4A6AB"
        self.textColor = 'white'
        self.root.configure(bg=self.mainBackground)
        self.conn = Connect()
        self.cr = self.conn.cursor()

        width = int(self.root.winfo_screenwidth())
        height = int(self.root.winfo_screenheight())
        print(width, height)

        self.root.columnconfigure(1, weight=1)  # Expand the right column

        self.frame = Frame(self.root, pady=10, padx=10, bg=self.mainBackground, width=int(width), height=int(height))
        self.frame.pack(expand=True, fill='both')
        self.frame.pack_propagate(0)

        width_1 = int(self.frame.winfo_screenwidth() / 2)
        height_2 = int(self.frame.winfo_screenheight() - 200)

        self.frame1 = Frame(self.frame, highlightthickness=4, highlightbackground='black', width=int(width_1),
                            height=int(height_2), bg=self.frameBackground, padx=2, pady=2)
        self.frame1.grid(row=0, column=0, padx=12, pady=35)
        self.frame1.grid_propagate(0)

        self.frame2 = Frame(self.frame, highlightthickness=4, bg=self.frameBackground, highlightbackground='black',
                            width=width_1, height=height_2)
        self.frame2.grid(row=0, column=1, pady=35)
        self.frame2.grid_propagate(0)

        self.mainLabel1 = Label(self.frame1, text="CRIMINAL DETECTION SYSTEM", font=("Times New Roman", 20, 'bold'),
                                fg='black', bg=self.frameBackground)
        self.mainLabel1.pack(padx=30, pady=10)

        self.frm = Frame(self.frame1, bg=self.mainBackground)
        self.frm.pack(pady=10, padx=30)

        self.lb1 = Label(self.frm, text='Criminal ID:', font=self.font, bg=self.mainBackground, foreground=self.textColor)
        self.lb1.grid(row=0, column=0, padx=10, pady=10)
        self.txt1 = Entry(self.frm, font=self.font, width=30, highlightthickness=4, highlightbackground='black')
        self.txt1.grid(row=0, column=1, padx=10, pady=10)

        self.lb2 = Label(self.frm, text='Criminal Name:', font=self.font, bg=self.mainBackground, foreground=self.textColor)
        self.lb2.grid(row=1, column=0, padx=10, pady=10)
        self.txt2 = Entry(self.frm, font=self.font, width=30, highlightbackground='black', highlightthickness=4)
        self.txt2.grid(row=1, column=1, padx=10, pady=10)

        self.lb3 = Label(self.frm, text='Date:', font=self.font, bg=self.mainBackground, foreground=self.textColor)
        self.lb3.grid(row=2, column=0, padx=10, pady=10)
        self.txt3 = Entry(self.frm, font=self.font, width=30, highlightthickness=4, highlightbackground='black')
        self.txt3.grid(row=2, column=1, padx=10, pady=10)

        self.lb4 = Label(self.frm, text='Timing:', font=self.font, bg=self.mainBackground, foreground=self.textColor)
        self.lb4.grid(row=3, column=0, padx=10, pady=10)
        self.txt4 = Entry(self.frm, font=self.font, width=30, highlightthickness=4, highlightbackground='black')
        self.txt4.grid(row=3, column=1, padx=10, pady=10)

        self.lb5 = Label(self.frm, text='Center Id :', font=self.font, bg=self.mainBackground, foreground=self.textColor)
        self.lb5.grid(row=4, column=0, padx=10, pady=10)
        self.txt5 = Entry(self.frm, font=self.font, width=30, highlightbackground='black', highlightthickness=4)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.grid(row=4, column=1, padx=10, pady=10)
        self.txt5.insert(0,self.center_id[0])


        self.lb6 = Label(self.frm, text="Enter Remarks:", font=self.font, bg=self.mainBackground, foreground=self.textColor)
        self.lb6.grid(row=5, column=0, padx=10, pady=10)
        self.txt6 = Text(self.frm, font=self.font, width=30, height=4, highlightbackground='black',
                         highlightthickness=4)
        self.txt6.grid(row=5, column=1, padx=10, pady=10)

        self.btn = Button(self.frame1, text='Submit', font=self.font, width=35, relief=tkinter.SOLID,
                          borderwidth=2, command=self.getSubmit)
        self.btn.pack(pady=42, padx=25)

        self.displayFrame = Frame(self.frame2, width=self.frame2.winfo_width(), padx=40, pady=40,
                                  height=int(self.frame2.winfo_screenheight()) - 350)
        self.displayFrame.pack(pady=10, expand=True, fill='both', padx=10)
        self.displayFrame.pack_propagate(0)

        width_2 = int(self.displayFrame.winfo_screenheight() - 200)
        height_2 = int(self.displayFrame.winfo_screenheight() - 500)

        self.label = Label(self.displayFrame)
        self.label.pack(anchor=NE)

        self.camLabel = Label(self.displayFrame)
        self.camLabel.pack(anchor=NW)

        self.btnFrame = Frame(self.frame2, width=int(width_2 / 3 * 4), bg=self.frameBackground, height=height_2)
        self.btnFrame.pack(pady=20, padx=20)
        self.btnFrame.pack_propagate(0)

        self.cameraButton = Button(self.btnFrame, text='Open Camera',
                                   font=self.font, width=18, relief=tkinter.SOLID, command=self.openCamera,
                                   anchor='center', bg=self.mainBackground)
        self.cameraButton.grid(row=0, column=0, pady=20, padx=15)

        self.cameraClose = Button(self.btnFrame, text="Capture ",
                                  font=self.font, width=18, relief=tkinter.SOLID, bg=self.mainBackground)
        self.cameraClose.grid(row=0, column=2, pady=20, padx=15)

        self.imageButton = Button(self.btnFrame, text="Close Button",
                                  font=self.font, width=18, relief=tkinter.SOLID, bg=self.mainBackground)
        self.imageButton.grid(row=0, column=3, pady=20, padx=15)

        self.cameraButton.bind("<Enter>", self.on_enter_btn)
        self.cameraButton.bind("<Leave>", self.on_leave_btn)

        self.cameraClose.bind("<Enter>", self.on_enter_btn)
        self.cameraClose.bind("<Leave>", self.on_leave_btn)

        self.imageButton.bind("<Enter>", self.on_enter_btn)
        self.imageButton.bind("<Leave>", self.on_leave_btn)

        self.root.mainloop()

    def openCamera(self):
        self.cap = cv2.VideoCapture(0)
        self.show_frames()
        self.cameraClose.configure(command=self.closeCamera, text='Close Camera')
        self.imageButton.configure(command=self.recface, text='Capture')

    def closeCamera(self):
        self.cap.release()
        cv2.destroyAllWindows()
        self.camLabel.configure(image='')
        self.cameraButton.configure(command=self.openCamera, text='Open Camera')

    def recface(self):
        image_list = os.listdir('../criminal_image')
        found = False  # To track if a match is found

        for img in image_list:
            print(img)
            try:
                result = DeepFace.verify(img1_path=self.frame, img2_path=f"../criminal_image/{img}",
                                         model_name='VGG-Face')
                print(result)

                if result['verified']:
                    msg.showinfo("Success", "Criminal found", parent=self.root)
                    self.getValues(img)
                    found = True
                    break
            except Exception as e:
                print(f"Error verifying face: {e}")
                msg.showerror("Error", f"An error occurred during face verification: {e}", parent=self.root)
                return

        if not found:
            msg.showwarning("Verification Failed",
                            "Face verification failed. Please ensure the image is clear and try again.",
                            parent=self.root)

    def getValues(self, img):
        try:
            with Connect() as conn:
                cr = conn.cursor()
                q = f"select * from criminals where image='{img}'"
                cr.execute(q)
                data = cr.fetchall()
                print(data)
                print(self.center_id)

                self.txt1.delete(0, 'end')
                self.txt2.delete(0, 'end')
                self.txt3.delete(0, 'end')
                self.txt4.delete(0, 'end')

                self.txt1.insert(0, data[0][0])
                self.txt2.insert(0, data[0][1])
                current_date = datetime.date.today().strftime("%Y-%m-%d")
                current_time = datetime.datetime.now().strftime("%H:%M")
                print(current_date, current_time)
                self.txt3.insert(0, current_date)
                self.txt4.insert(0, current_time)
                # self.txt5.insert(0, self.center_id[0])
        except Exception as e:
            msg.showerror("Error", f"Failed to fetch values: {str(e)}", parent=self.root)

    def getSubmit(self):
        criminal_id = self.txt1.get()
        criminal_name = self.txt2.get()
        date = self.txt3.get()
        time = self.txt4.get()
        center_id = self.txt5.get()
        remark = self.txt6.get('1.0', 'end-1c')

        if criminal_id == "" or criminal_name == "" or date == "" or time == "" or center_id == "" or remark == "":
            msg.showerror("Validation Error", "All fields are required", parent=self.root)
            return

        try:
            with Connect() as conn:
                if conn is None:
                    print("Database connection failed")
                    return
                cr = conn.cursor()
                q = """
                    INSERT INTO remarks (criminal_name, criminal_id, center_id, date, time, remark) 
                    VALUES (%s, %s, %s, %s, %s, %s)
                    """
                cr.execute(q, (criminal_name, criminal_id, center_id, date, time, remark))

                conn.commit()
                msg.showinfo("Success", "Remark added successfully", parent=self.root)
                # self.clearFields()
                self.sendRemarks(criminal_id)  # Call sendRemarks after adding the remark
        except Exception as e:
            msg.showerror("Error", f"Failed to submit remark: {str(e)}", parent=self.root)

    def sendRemarks(self, criminal_id):
        q = f"select name, email from criminals where id='{criminal_id}'"
        self.cr.execute(q)
        criminals_data = self.cr.fetchone()
        center_id = self.txt5.get()

        q1 = f"select name, email, mobile, area, location from add_center where id='{center_id}'"
        self.cr.execute(q1)
        center_data = self.cr.fetchone()
        date = self.txt3.get()
        time = self.txt4.get()
        description = self.txt6.get('1.0', 'end-1c')

        message = f'''
            Criminal Name - {criminals_data[0]} has been identified at {time} on {date}.

            Here are Center Details - 
            Center Name - {center_data[0]}
            Center Mobile - {center_data[2]}
            Center Email - {center_data[1]}
            Location - {center_data[4]}
            Area - {center_data[3]}

            Here are Center Remarks - 
            {description}
        '''
        subject = "Criminal Report"
        x = sendEmail(to=center_data[1], message=message, subject=subject)
        if x:
            msg.showinfo("Sent", "mail has been sent")
        else:
            msg.showwarning('Warn', 'Mail not sent')

    def clearFields(self):
        self.txt1.delete(0, 'end')
        self.txt2.delete(0, 'end')
        self.txt3.delete(0, 'end')
        self.txt4.delete(0, 'end')
        self.txt5.delete(0, 'end')
        self.txt6.delete('1.0', 'end')

    def on_enter_btn(self, e):
        e.widget['background'] = 'white'
        e.widget['foreground'] = 'black'

    def on_leave_btn(self, e):
        e.widget['background'] = self.mainBackground
        e.widget['foreground'] = 'black'

    def show_frames(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
                img = Image.fromarray(cv2image)
                imgtk = ImageTk.PhotoImage(image=img)
                self.camLabel.imgtk = imgtk
                self.camLabel.configure(image=imgtk)
                self.camLabel.after(10, self.show_frames)
                self.frame = frame


if __name__ == "__main__":
    data = [[2]]
    identifycriminal(data)