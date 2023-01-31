from tkinter import *      #FOR GUI
from tkinter import ttk     #HAS SOME STYLING
import tkinter
from PIL import Image,ImageTk      #For manipulating images
from student import Student
import numpy as np
from tkinter import messagebox
import cv2
import os
from face_recognition import Face_Recognition
from attendance import attendance
from developer import developer
from datetime import datetime
from time import strftime



class Face_Recognition_System:
    def __init__(self,root):    #root is the window name
        self.root=root
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry('%dx%d+%d+%d' % (screen_width, screen_height, 0, 0))
        self.root.title("Attendance")
        

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

        title_lbl=Label(bg_img,text="FACE RECOGNITION BASED ATTENDANCE SYSTEM",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=screen_width,height=int(screen_height/16))

        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)
        lbl = Label(title_lbl,font=("times new roman",int(screen_height/52.5),"bold"),background='white',foreground='blue')
        lbl.place(x=10,y=0,width=int(screen_width/13.9),height=int(screen_height/20))
        time()


        #student button
        img4=Image.open("SourceImages/SD.jpg")
        img4=img4.resize((int(screen_width/8.7),int(screen_height/4.77)),Image.ANTIALIAS) #height,width
        self.photoimg4=ImageTk.PhotoImage(img4) #setting the above pic

        b1=Button(bg_img,image=self.photoimg4,command=self.student_details,cursor="hand2")
        b1.place(x=int(screen_width/19.2),y=int(5*screen_height/55.2),width=int(screen_width/8.7),height=int(screen_height/4.77))

        b1_1=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",int(screen_height/52.5),"bold"),bg="#1a75ff",fg="white")
        b1_1.place(x=int(screen_width/19.2),y=int((5*screen_height/55.2)+(screen_height/4.77)),width=int(screen_width/8.7),height=int(screen_height/26.25))


        #Detect face button
        img5=Image.open("SourceImages/FR.png")
        img5=img5.resize((int(screen_width/8.7),int(screen_height/4.77)),Image.ANTIALIAS) #height,width
        self.photoimg5=ImageTk.PhotoImage(img5) #setting the above pic

        b2=Button(bg_img,command=self.face_data,image=self.photoimg5,cursor="hand2")
        b2.place(x=int(screen_width/4.5),y=int(5*screen_height/55.2),width=int(screen_width/8.7),height=int(screen_height/4.77))

        b2_1=Button(bg_img,text="Face Detection",command=self.face_data,cursor="hand2",font=("times new roman",int(screen_height/52.5),"bold"),bg="#1a75ff",fg="white")
        b2_1.place(x=int(screen_width/4.5),y=int((5*screen_height/55.2)+(screen_height/4.77)),width=int(screen_width/8.7),height=int(screen_height/26.25))

        
        #Attendance Button
        img6=Image.open("SourceImages/A.png")
        img6=img6.resize((int(screen_width/8.7),int(screen_height/4.77)),Image.ANTIALIAS) #height,width
        self.photoimg6=ImageTk.PhotoImage(img6) #setting the above pic

        b3=Button(bg_img,image=self.photoimg6,command=self.attendance_data,cursor="hand2")
        b3.place(x=int(screen_width/2.55),y=int(5*screen_height/55.2),width=int(screen_width/8.7),height=int(screen_height/4.77))

        b3_1=Button(bg_img,text="Attendance",command=self.attendance_data,cursor="hand2",font=("times new roman",int(screen_height/52.5),"bold"),bg="#1a75ff",fg="white")
        b3_1.place(x=int(screen_width/2.55),y=int((5*screen_height/55.2)+(screen_height/4.77)),width=int(screen_width/8.7),height=int(screen_height/26.25))

        #Training Image
        img7=Image.open("SourceImages/TI1.png")
        img7=img7.resize((int(screen_width/8.7),int(screen_height/4.77)),Image.ANTIALIAS) #height,width
        self.photoimg7=ImageTk.PhotoImage(img7) #setting the above pic

        b4=Button(bg_img,image=self.photoimg7,command=self.train_classifier,cursor="hand2")
        b4.place(x=int(screen_width/7.28),y=int(5*screen_height/9.2),width=int(screen_width/8.7),height=int(screen_height/4.77))

        b4_1=Button(bg_img,text="Train Image",command=self.train_classifier,cursor="hand2",font=("times new roman",int(screen_height/52.5),"bold"),bg="#1a75ff",fg="white")
        b4_1.place(x=int(screen_width/7.28),y=int((5*screen_height/9.2)+(screen_height/4.77)),width=int(screen_width/8.7),height=int(screen_height/26.25))

        #Developer Button
        img8=Image.open("SourceImages/5.jpg")
        img8=img8.resize((int(screen_width/8.7),int(screen_height/4.77)),Image.ANTIALIAS) #height,width
        self.photoimg8=ImageTk.PhotoImage(img8) #setting the above pic

        b5=Button(bg_img,image=self.photoimg8,command=self.developer_data,cursor="hand2")
        b5.place(x=int(screen_width/3.2),y=int(5*screen_height/9.2),width=int(screen_width/8.7),height=int(screen_height/4.77))

        b5_1=Button(bg_img,text="Developers",cursor="hand2",command=self.developer_data,font=("times new roman",int(screen_height/52.5),"bold"),bg="#1a75ff",fg="white")
        b5_1.place(x=int(screen_width/3.2),y=int((5*screen_height/9.2)+(screen_height/4.77)),width=int(screen_width/8.7),height=int(screen_height/26.25))

        #Exit
        img9=Image.open("SourceImages/exit.png")
        img9=img9.resize((int(screen_width/12.7),int(screen_height/14)),Image.ANTIALIAS) #height,width
        self.photoimg9=ImageTk.PhotoImage(img9) #setting the above pic

        b6=Button(bg_img,image=self.photoimg9,cursor="hand2",command=self.iExit)
        b6.place(x=int(screen_width/1.12),y=int(5*screen_height/7.5),width=int(screen_width/12.7),height=(screen_height/14))

        # b6_1=Button(bg_img,text="Exit",cursor="hand2",font=("times new roman",int(screen_height/52.5),"bold"),bg="#1a75ff",fg="white")
        # b6_1.place(x=1600,y=900,width=220,height=40)


# ====================Functions buttons ========================

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=attendance(self.new_window)
    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=developer(self.new_window)
     
    def train_classifier(self):
        data_dir=("Data")
        path=[os.path.join(data_dir,file) for file in os.listdir(data_dir)]

        faces=[]
        ids=[]
        for image in path:
            img=Image.open(image).convert('L')      #gray scale image
            imageNp=np.array(img,'uint8')
            id=int(os.path.split(image)[1].split('.')[1])
            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training",imageNp)
            cv2.waitKey(1)==13
        ids=np.array(ids)

        #================ train the classifier and save ===========
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces,ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result","Training datasets completed!!")   
    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face Recognition"," Are you sure to exit!",parent=self.root)
        if self.iExit>0:
            self.root.destroy()
        else:
            return

if __name__ == '__main__':
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()