from tkinter import *      #FOR GUI
from tkinter import ttk     #HAS SOME STYLING
from PIL import Image,ImageTk      #For manipulating images
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
from datetime import datetime
from time import strftime



mydata=[]
class attendance:
    def __init__(self,root):    #root is the window name
        self.root=root
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry('%dx%d+%d+%d' % (screen_width, screen_height, 0, 0))
        self.root.title("ATTENDANCE") 

        # ================= variables =============
        self.var_atten_id=StringVar()
        self.var_atten_roll=StringVar()
        self.var_atten_name=StringVar()
        self.var_atten_dep=StringVar()
        self.var_atten_time=StringVar()
        self.var_atten_date=StringVar()
        self.var_atten_attendance=StringVar()
    #FIRST IMAGE
        img=Image.open(r"SourceImages/header1.jpg")
        img=img.resize((int(screen_width/3),int(screen_height/6)),Image.ANTIALIAS) #height,width
        self.photoimg=ImageTk.PhotoImage(img) #setting the above pic

        f_lbl=Label(self.root,image=self.photoimg) #creating a label image
        f_lbl.place(x=0,y=0,width=int(screen_width/3),height=int(screen_height/6)) #placing the image label

        #SECOND IMAGE
        img1=Image.open("SourceImages/h2.jpg")
        img1=img1.resize((int(screen_width/3),int(screen_height/6)),Image.ANTIALIAS) #height,width
        self.photoimg1=ImageTk.PhotoImage(img1) #setting the above pic

        f_lbl=Label(self.root,image=self.photoimg1) #creating a label image
        f_lbl.place(x=int(screen_width/3),y=0,width=int(screen_width/3),height=int(screen_height/6)) #placing the image label

        #THIRD IMAGE
        img2=Image.open("SourceImages/header3.png")
        img2=img2.resize((int(screen_width/3),int(screen_height/6)),Image.ANTIALIAS) #height,width
        self.photoimg2=ImageTk.PhotoImage(img2) #setting the above pic

        f_lbl=Label(self.root,image=self.photoimg2) #creating a label image
        f_lbl.place(x=int(2*screen_width/3),y=0,width=int(screen_width/3),height=int(screen_height/6)) #placing the image label

        #background image
        img3=Image.open("SourceImages/background.jpg")
        img3=img3.resize((int(screen_width),int(5*screen_height/6)),Image.ANTIALIAS) #height,width
        self.photoimg3=ImageTk.PhotoImage(img3) #setting the above pic

        bg_img=Label(self.root,image=self.photoimg3) #creating a label image
        bg_img.place(x=0,y=int(screen_height/6),width=screen_width,height=int(5*screen_height/6)) #placing the image label
        title_lbl=Label(bg_img,text="ATTENDANCE MANAGMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=screen_width,height=int(screen_height/16))
        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)
        lbl = Label(title_lbl,font=("times new roman",int(screen_height/52.5),"bold"),background='white',foreground='blue')
        lbl.place(x=10,y=0,width=int(screen_width/13.9),height=int(screen_height/20))
        time()

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=int(screen_width/34.7),y=int(5*screen_height/55.2),width=int(screen_width/1.06),height=int(screen_height/1.38))


        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",int(screen_height/40),"bold"))
        left_frame.place(x=int(screen_width/63.6),y=int(screen_height/104.88),width=int(screen_width/2.3),height=int(screen_height/1.5))
        

        #id 
        atdId_label=Label(left_frame,text="Attendance Id:",font=("times new roman",int(screen_height/40),"bold"))
        atdId_label.grid(row=0,column=0,padx=int(screen_width/150),pady=int(screen_width/110),sticky=W)

        atdId_entry=ttk.Entry(left_frame,width=int(screen_width/95.6),textvariable=self.var_atten_id,font=("times new roman",int(screen_height/40),"bold"))
        atdId_entry.grid(row=0,column=1,padx=int(screen_width/150),pady=int(screen_width/110),sticky=W)

        Name_label=Label(left_frame,text="Student Name:",font=("times new roman",int(screen_height/40),"bold"))
        Name_label.grid(row=1,column=0,padx=int(screen_width/150),pady=int(screen_width/110),sticky=W)

        Name_entry=ttk.Entry(left_frame,width=int(screen_width/95.6),textvariable=self.var_atten_name,font=("times new roman",int(screen_height/40),"bold"))
        Name_entry.grid(row=1,column=1,padx=int(screen_width/150),pady=int(screen_width/110),sticky=W)

        roll_label=Label(left_frame,text="Roll No:",font=("times new roman",int(screen_height/40),"bold"))
        roll_label.grid(row=2,column=0,padx=int(screen_width/150),pady=int(screen_width/110),sticky=W)

        roll_entry=ttk.Entry(left_frame,width=int(screen_width/95.6),textvariable=self.var_atten_roll,font=("times new roman",int(screen_height/40),"bold"))
        roll_entry.grid(row=2,column=1,padx=int(screen_width/150),pady=int(screen_width/110),sticky=W)

        dep_label=Label(left_frame,text="Department",font=("times new roman",int(screen_height/40),"bold"))
        dep_label.grid(row=3,column=0,padx=int(screen_width/150),pady=int(screen_width/110),sticky=W)

        dep_combo=ttk.Combobox(left_frame,font=("times new roman",int(screen_height/40),"bold"),width=int(screen_width/100),textvariable=self.var_atten_dep,state="readonly")
        dep_combo["values"]=("Select Department","CSE","CSY","ECE","AI/ML")
        dep_combo.current(0)
        dep_combo.grid(row=3,column=1,padx=int(screen_width/150),pady=int(screen_width/110),sticky=W)

        timelabel=Label(left_frame,text="Time :",font=("times new roman",int(screen_height/40),"bold"))
        timelabel.grid(row=4,column=0,padx=int(screen_width/150),pady=int(screen_width/110),sticky=W)

        atten_time=ttk.Entry(left_frame,width=int(screen_width/95.6),textvariable=self.var_atten_time,font=("times new roman",int(screen_height/40),"bold"))
        atten_time.grid(row=4,column=1,padx=int(screen_width/150),pady=int(screen_width/110),sticky=W)

        datelabel=Label(left_frame,text="Date :",font=("times new roman",int(screen_height/40),"bold"))
        datelabel.grid(row=5,column=0,padx=int(screen_width/150),pady=int(screen_width/110),sticky=W)

        atten_date=ttk.Entry(left_frame,width=int(screen_width/95.6),textvariable=self.var_atten_date,font=("times new roman",int(screen_height/40),"bold"))
        atten_date.grid(row=5,column=1,padx=int(screen_width/150),pady=int(screen_width/110),sticky=W)

        attendance_label=Label(left_frame,text="Attendance Status :",font=("times new roman",int(screen_height/40),"bold"))
        attendance_label.grid(row=6,column=0,padx=int(screen_width/150),pady=int(screen_width/110),sticky=W)

        self.atten_status=ttk.Combobox(left_frame,font=("times new roman",int(screen_height/40),"bold"),textvariable=self.var_atten_attendance,width=int(screen_width/100),state="readonly")
        self.atten_status["values"]=("Status","Present","Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=6,column=1,padx=int(screen_width/150),pady=int(screen_width/110),sticky=W)

        btn_frame=Frame(left_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=int(screen_height/1.8),width=int(screen_width/2.42),height=int(screen_height/21))

        save_btn=Button(btn_frame,text="Import csv",command=self.importCsv,width=int(screen_width/75),height=int(screen_height/525),font=("times new roman",13,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Export csv",command=self.exportCsv,width=int(screen_width/76),height=int(screen_height/525),font=("times new roman",13,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)

        reset_btn=Button(btn_frame,text="Reset",width=int(screen_width/75),command=self.reset_data,height=int(screen_height/525),font=("times new roman",13,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=2)
       
       
        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Attendance Details",font=("times new roman",int(screen_height/52.5),"bold"))
        right_frame.place(x=int(screen_width/2.06),y=int(screen_height/104.88),width=int(screen_width/2.32),height=int(screen_height/1.5))

        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=int(screen_width/191.4),y=int(screen_height/105),width=int(screen_width/2.39),height=int(screen_height/1.65))

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)

        self.attendance_table=ttk.Treeview(table_frame,column=('id','roll','name','department','time','date','attendance'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.attendance_table.xview)
        scroll_y.config(command=self.attendance_table.yview)

        self.attendance_table.heading('id',text='ATTENDANCE ID')
        self.attendance_table.heading('roll',text='ROLL NO')
        self.attendance_table.heading('name',text='NAME')
        self.attendance_table.heading('department',text='DEPARTMENT')
        self.attendance_table.heading('time',text='TIME')
        self.attendance_table.heading('date',text='DATE')
        self.attendance_table.heading('attendance',text='ATTENDANCE')

        self.attendance_table["show"]="headings"

        self.attendance_table.column('id',width=100)
        self.attendance_table.column('roll',width=100)
        self.attendance_table.column('name',width=100)
        self.attendance_table.column('department',width=100)
        self.attendance_table.column('time',width=100)
        self.attendance_table.column('date',width=100)
        self.attendance_table.column('attendance',width=100)

        self.attendance_table.pack(fill=BOTH,expand=1)

        
        self.attendance_table.bind("<ButtonRelease>",self.get_cursor)



    def fetch_data(self,rows):
        self.attendance_table.delete(*self.attendance_table.get_children())
        for i in rows:
            self.attendance_table.insert("",END,values=i)

    # importing csv
    def importCsv(self):
        global mydata
        mydata.clear()
        fln=filedialog.askopenfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
        with open(fln) as myfile:
            csvread=csv.reader(myfile)
            for i in csvread:
                mydata.append(i)
            self.fetch_data(mydata)

    #exporting csv
    def exportCsv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("No Data","NO DATA FOUND!!",parent=self.root)
                return False
            fln=filedialog.asksaveasfilename(initialdir=os.getcwd(),title="Open CSV",filetypes=(("CSV File","*.csv"),("ALl File","*.*")),parent=self.root)
            with open(fln,mode="w",newline="\n") as myfile:
                exp_write=csv.writer(myfile,delimiter=",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Success","Your data has been exported to "+os.path.basename(fln)+" Successfully",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error",f"Due To {str(es)}",parent=self.root)

    def get_cursor(self,event=""):
        cursor_row=self.attendance_table.focus()
        content=self.attendance_table.item(cursor_row)
        rows=content['values']
        self.var_atten_id.set(rows[0])
        self.var_atten_roll.set(rows[1])
        self.var_atten_name.set(rows[2])
        self.var_atten_dep.set(rows[3])
        self.var_atten_time.set(rows[4])
        self.var_atten_date.set(rows[5])
        self.var_atten_attendance.set(rows[6])

    def reset_data(self):
        self.var_atten_id.set("")
        self.var_atten_roll.set("")
        self.var_atten_name.set("")
        self.var_atten_dep.set("Select Department")
        self.var_atten_time.set("")
        self.var_atten_date.set("")
        self.var_atten_attendance.set("Status")



if __name__ == '__main__':
    root=Tk()
    obj=attendance(root)
    root.mainloop()