from tkinter import *      #FOR GUI
from tkinter import ttk     #HAS SOME STYLING
from PIL import Image,ImageTk      #For manipulating images
from tkinter import messagebox
import mysql.connector
import cv2
from datetime import datetime
from time import strftime

class Student:
    def __init__(self,root):    #root is the window name
        self.root=root
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry('%dx%d+%d+%d' % (screen_width, screen_height, 0, 0))
        self.root.title("STUDENT DETAILS")

        #==============variables===========
        self.var_dep=StringVar()
        self.var_course=StringVar()
        self.var_year=StringVar()
        self.var_semester=StringVar()
        self.va_std_id=StringVar()
        self.var_std_name=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()

    #setting images
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
        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="green")
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
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Information",font=("times new roman",int(screen_height/52.5),"bold"))
        left_frame.place(x=int(screen_width/63.6),y=int(screen_height/104.88),width=int(screen_width/2.3),height=int(screen_height/1.5))

        #current course frame
        curr_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",int(screen_height/52.5),"bold"))
        curr_frame.place(x=int(screen_width/189.75),y=int(screen_height/105),width=int(screen_width/2.39),height=int(screen_height/5.83))

        #Department
        dep_label=Label(curr_frame,text="Department",font=("times new roman",int(screen_height/52.5),"bold"))
        dep_label.grid(row=0,column=0,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        dep_combo=ttk.Combobox(curr_frame,textvariable=self.var_dep,font=("times new roman",int(screen_height/52.5),"bold"),width=int(screen_width/112),state="readonly")
        dep_combo["values"]=("Select Department","CSE","CSY","ECE","AI/ML")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        # course
        course_label=Label(curr_frame,text="Courses",font=("times new roman",int(screen_height/52.5),"bold"))
        course_label.grid(row=0,column=2,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        course_combo=ttk.Combobox(curr_frame,textvariable=self.var_course,font=("times new roman",int(screen_height/52.5),"bold"),width=int(screen_width/112),state="readonly")
        course_combo["values"]=("Select Course","ICS","IMA","ISC","IEC","IHS")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        #year
        year_label=Label(curr_frame,text="Year",font=("times new roman",int(screen_height/52.5),"bold"))
        year_label.grid(row=1,column=0,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        year_combo=ttk.Combobox(curr_frame,textvariable=self.var_year,font=("times new roman",int(screen_height/52.5),"bold"),width=int(screen_width/112),state="readonly")
        year_combo["values"]=("Select Year","1st year","2nd year","3rd year","4th year")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)
    
       #semester
        sem_label=Label(curr_frame,text="Semester",font=("times new roman",int(screen_height/52.5),"bold"))
        sem_label.grid(row=1,column=2,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        sem_combo=ttk.Combobox(curr_frame,textvariable=self.var_semester,font=("times new roman",int(screen_height/52.5),"bold"),width=int(screen_width/112),state="readonly")
        sem_combo["values"]=("Select Semester","Semester 1","Semester 2")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        # class info
        class_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course Information",font=("times new roman",int(screen_height/52.5),"bold"))
        class_frame.place(x=int(screen_width/189.75),y=int(screen_height/5),width=int(screen_width/2.39),height=int(screen_height/2.3))

        stuId_label=Label(class_frame,text="StudentId No:",font=("times new roman",int(screen_height/52.5),"bold"))
        stuId_label.grid(row=0,column=0,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        stuId_entry=ttk.Entry(class_frame,textvariable=self.va_std_id,width=int(screen_width/95.6),font=("times new roman",int(screen_height/52.5),"bold"))
        stuId_entry.grid(row=0,column=1,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)
        
        stuName_label=Label(class_frame,text="Student Name:",font=("times new roman",int(screen_height/52.5),"bold"))
        stuName_label.grid(row=0,column=2,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        stuName_entry=ttk.Entry(class_frame,textvariable=self.var_std_name,width=int(screen_width/95.6),font=("times new roman",int(screen_height/52.5),"bold"))
        stuName_entry.grid(row=0,column=3,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        classDiv_label=Label(class_frame,text="Class Division:",font=("times new roman",int(screen_height/52.5),"bold"))
        classDiv_label.grid(row=1,column=0,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        classDiv_combo=ttk.Combobox(class_frame,textvariable=self.var_div,font=("times new roman",int(screen_height/52.5),"bold"),width=int(screen_width/108),state="readonly")
        classDiv_combo["values"]=("Select Batch","Batch-1","Batch-2","Batch-3")
        classDiv_combo.current(0)
        classDiv_combo.grid(row=1,column=1,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        rollNo_label=Label(class_frame,text="Roll No:",font=("times new roman",int(screen_height/52.5),"bold"))
        rollNo_label.grid(row=1,column=2,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        rollNo_entry=ttk.Entry(class_frame,textvariable=self.var_roll,width=int(screen_width/95.6),font=("times new roman",int(screen_height/52.5),"bold"))
        rollNo_entry.grid(row=1,column=3,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        gender_label=Label(class_frame,text="Gender:",font=("times new roman",int(screen_height/52.5),"bold"))
        gender_label.grid(row=2,column=0,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        gender_combo=ttk.Combobox(class_frame,textvariable=self.var_gender,font=("times new roman",int(screen_height/52.5),"bold"),width=int(screen_width/108),state="readonly")
        gender_combo["values"]=("Select Gender","Male","Female","Others")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        dob_label=Label(class_frame,text="Date Of Birth:",font=("times new roman",int(screen_height/52.5),"bold"))
        dob_label.grid(row=2,column=2,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        dob_entry=ttk.Entry(class_frame,textvariable=self.var_dob,width=int(screen_width/95.6),font=("times new roman",int(screen_height/52.5),"bold"))
        dob_entry.grid(row=2,column=3,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        email_label=Label(class_frame,text="Email:",font=("times new roman",int(screen_height/52.5),"bold"))
        email_label.grid(row=3,column=0,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        email_entry=ttk.Entry(class_frame,textvariable=self.var_email,width=int(screen_width/95.6),font=("times new roman",int(screen_height/52.5),"bold"))
        email_entry.grid(row=3,column=1,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        phNo_label=Label(class_frame,text="Phone No:",font=("times new roman",int(screen_height/52.5),"bold"))
        phNo_label.grid(row=3,column=2,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        phNo_entry=ttk.Entry(class_frame,textvariable=self.var_phone,width=int(screen_width/95.6),font=("times new roman",int(screen_height/52.5),"bold"))
        phNo_entry.grid(row=3,column=3,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        addr_label=Label(class_frame,text="Address:",font=("times new roman",int(screen_height/52.5),"bold"))
        addr_label.grid(row=4,column=0,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        addr_entry=ttk.Entry(class_frame,textvariable=self.var_address,width=int(screen_width/95.6),font=("times new roman",int(screen_height/52.5),"bold"))
        addr_entry.grid(row=4,column=1,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        teachName_label=Label(class_frame,text="Teacher Name:",font=("times new roman",int(screen_height/52.5),"bold"))
        teachName_label.grid(row=4,column=2,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        teachName_entry=ttk.Entry(class_frame,textvariable=self.var_teacher,width=int(screen_width/95.6),font=("times new roman",int(screen_height/52.5),"bold"))
        teachName_entry.grid(row=4,column=3,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radionbtn1=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0,padx=int(screen_width/250),pady=int(screen_width/210))
        
        radionbtn2=ttk.Radiobutton(class_frame,variable=self.var_radio1,text="No Photo Sample",value="No")
        radionbtn2.grid(row=6,column=1,padx=int(screen_width/250),pady=int(screen_width/210))

        #bbuttons frame
        btn_frame=Frame(class_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=int(screen_height/3.3),width=int(screen_width/2.42),height=int(screen_height/21))

        save_btn=Button(btn_frame,text="Save",command=self.add_data,width=int(screen_width/100),height=int(screen_height/525),font=("times new roman",13,"bold"),bg="green",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",command=self.update_data,width=int(screen_width/100),height=int(screen_height/525),font=("times new roman",13,"bold"),bg="green",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",command=self.delete_data,width=int(screen_width/100),height=int(screen_height/525),font=("times new roman",13,"bold"),bg="green",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",command=self.reset_data,width=int(screen_width/100),height=int(screen_height/525),font=("times new roman",13,"bold"),bg="green",fg="white")
        reset_btn.grid(row=0,column=3)
        
        btn2_frame=Frame(class_frame,bd=2,relief=RIDGE)
        btn2_frame.place(x=0,y=int(screen_height/2.9),width=int(screen_width/2.42),height=int(screen_height/21))

        add_photo_btn=Button(btn2_frame,text="Add Photo Sample",command=self.generate_dataset,width=int(screen_width/25),height=int(screen_height/525),font=("times new roman",13,"bold"),bg="green",fg="white")
        add_photo_btn.grid(row=1,column=0)
        
        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",int(screen_height/52.5),"bold"))
        right_frame.place(x=int(screen_width/2.06),y=int(screen_height/104.88),width=int(screen_width/2.32),height=int(screen_height/1.5))

        #search
        # search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search System",font=("times new roman",int(screen_height/52.5),"bold"))
        # search_frame.place(x=int(screen_width/191.4),y=int(screen_height/105),width=int(screen_width/2.39),height=int(screen_height/5.25))
        
        # search_label=Label(search_frame,text="Search By:",font=("times new roman",int(screen_height/52.5),"bold"),bg="green",fg="white")
        # search_label.grid(row=0,column=0,padx=int(screen_width/250),pady=int(screen_width/210),sticky=W)
        
        # search_combo=ttk.Combobox(search_frame,font=("times new roman",int(screen_height/52.5),"bold"),width=int(screen_width/76.5),state="readonly")
        # search_combo["values"]=("Select","Roll_No","Phone_No")
        # search_combo.current(0)
        # search_combo.grid(row=0,column=1,padx=int(screen_width/250),pady=int(screen_width/52.5),sticky=W)

        # search_entry=ttk.Entry(search_frame,width=int(screen_width/76.5),font=("times new roman",int(screen_height/52.5),"bold"))
        # search_entry.grid(row=0,column=2,padx=int(screen_width/127),pady=int(screen_width/210),sticky=W)

        # Search_btn=Button(search_frame,text="Search",width=int(screen_width/106),height=int(screen_height/525),font=("times new roman",13,"bold"),bg="green",fg="white")
        # Search_btn.grid(row=1,column=1)

        # Showall_btn=Button(search_frame,text="Show All",width=int(screen_width/106),height=int(screen_height/525),font=("times new roman",13,"bold"),bg="green",fg="white")
        # Showall_btn.grid(row=1,column=2)
        
        #table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=int(screen_width/191.4),y=int(screen_height/105),width=int(screen_width/2.39),height=int(screen_height/1.65))

        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        self.student_table=ttk.Treeview(table_frame,column=('Dep','course','Year','Semester','Student_id','Name','Division' ,'Roll','Gender','Dob','Email','Phone','Address','Teacher','PhotoSample'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading('Dep',text='DEPARTMENT')
        self.student_table.heading('course',text='COURSE')
        self.student_table.heading('Year',text='YEAR')
        self.student_table.heading('Semester',text='SEMESTER')
        self.student_table.heading('Student_id',text='STUDENT ID')
        self.student_table.heading('Name',text='NAME')
        self.student_table.heading('Roll',text='ROLL NO')
        self.student_table.heading('Gender',text='GENDER')
        self.student_table.heading('Division',text='DIVISION')
        self.student_table.heading('Dob',text='DATE OF BIRTH')
        self.student_table.heading('Email',text='EMAIL')
        self.student_table.heading('Phone',text='PHONE NO')
        self.student_table.heading('Address',text='ADDRESS')
        self.student_table.heading('Teacher',text='TEACHER')
        self.student_table.heading('PhotoSample',text='PHOTO SAMPLE STATUS')

        self.student_table["show"]="headings"

        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.column('Dep',width=100)
        self.student_table.column('course',width=100)
        self.student_table.column('Year',width=100)
        self.student_table.column('Semester',width=100)
        self.student_table.column('Student_id',width=100)
        self.student_table.column('Name',width=100)
        self.student_table.column('Roll',width=100)
        self.student_table.column('Gender',width=100)
        self.student_table.column('Division',width=100)
        self.student_table.column('Dob',width=100)
        self.student_table.column('Email',width=100)
        self.student_table.column('Phone',width=100)
        self.student_table.column('Address',width=100)
        self.student_table.column('Teacher',width=100)
        self.student_table.column('PhotoSample',width=150)
        
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        
    #============Function declaration==============
    def add_data(self):
        if self.var_dep.get()=='Select Department' or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            # messagebox.showinfo("Success","All the details are saved")
            try:
                conn=mysql.connector.connect(host="localhost",username='root',password="Karthik@123",database="face_recognizer")
                #messagebox.showinfo("DATABASE ",parent=self.root)
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.va_std_id.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get()
                                                                                                            
                                                                                                            ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success","All the details are added succesfully",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due To : {str(es)}",parent=self.root)
    

    #======fetch data==========
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username='root',password="Karthik@123",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("Select * from student")
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)
            conn.commit()
        conn.close()


    #============ get cursor =============
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]
        self.var_dep.set(data[0]),
        self.var_course.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.va_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])

    #===update function=========
    def update_data(self):
        if self.var_dep.get()=='Select Department' or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                update=messagebox.askyesno("Update","Are you sure want to update the student details?",parent=self.root)
                if update>0:
                    conn=mysql.connector.connect(host="localhost",username='root',password="Karthik@123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                                                                                                                self.var_dep.get(),
                                                                                                                self.var_course.get(),
                                                                                                                self.var_year.get(),
                                                                                                                self.var_semester.get(),
                                                                                                                self.var_std_name.get(),
                                                                                                                self.var_div.get(),
                                                                                                                self.var_roll.get(),
                                                                                                                self.var_gender.get(),
                                                                                                                self.var_dob.get(),
                                                                                                                self.var_email.get(),
                                                                                                                self.var_phone.get(),
                                                                                                                self.var_address.get(),
                                                                                                                self.var_teacher.get(),
                                                                                                                self.var_radio1.get(),
                                                                                                                self.va_std_id.get()
                    ))
                else:
                    if not update:
                        return
                messagebox.showinfo("Success","Student details successfully updated!!",parent=self.root)
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)

    #============== delete function ===========
    def delete_data(self):
        if self.va_std_id.get()=="":
            messagebox.showerror("Error","Student Id is mandatory!!",parent=self.root)
        else:
            try:
                delete=messagebox.askyesno("Student Delete Page","Are you sure want to delete the data?",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username='root',password="Karthik@123",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.va_std_id.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                    
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Successfully deleted the details of the student",parent=self.root)
            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)                

    #====== reset ====
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_course.set("Select Course"),
        self.var_year.set("Select Year"),
        self.var_semester.set("Select Semester"),
        self.va_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("Select Batch"),
        self.var_roll.set(""),
        self.var_gender.set("Select Gender"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")


    # ================ generate data set or take photo samples ===============

    def generate_dataset(self):
        if self.var_dep.get()=='Select Department' or self.var_std_name.get()=="" or self.va_std_id.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username='root',password="Karthik@123",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,course=%s,Year=%s,Semester=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,Dob=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSample=%s where Student_id=%s",(
                    self.var_dep.get(),
                    self.var_course.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.va_std_id.get() == id+1
                    ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                # ======== load predefined data on face frontals from opencv ========
                face_classifier=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    # scaling factor = 1.3
                    # minimum neighbour =5

                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(600,600))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="Data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,255,0),1)
                        cv2.imshow("Cropped Face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Successfully generated the data set!!",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due to {str(es)}",parent=self.root)
if __name__ == '__main__':
    root=Tk()
    obj=Student(root)
    root.mainloop()