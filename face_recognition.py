from tkinter import *      #FOR GUI
from tkinter import ttk     #HAS SOME STYLING
from PIL import Image,ImageTk      #For manipulating images
from student import Student
import cv2
import os
import numpy as np
from tkinter import messagebox
import mysql.connector
from datetime import datetime
from time import strftime

class Face_Recognition:
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

        title_lbl=Label(bg_img,text="FACE RECOGNITION",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=screen_width,height=int(screen_height/16))
        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)
        lbl = Label(title_lbl,font=("times new roman",int(screen_height/52.5),"bold"),background='white',foreground='blue')
        lbl.place(x=10,y=0,width=int(screen_width/13.9),height=int(screen_height/20))
        time()
        b=Button(bg_img,text=" Face Recognition",command=self.face_recog,cursor="hand2",font=("times new roman",15,"bold"),bg="#1a75ff",fg="white")
        b.place(x=int(screen_width/6),y=int(5*screen_height/9.3),width=int(screen_width/5),height=int(screen_height/17))
    
    # =============== Attendance ==============

    def mark_attendance(self,i,r,n,d):
        with open("Attendance.csv","r+",newline="\n") as f:
            myDataList=f.readlines()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if ((i not in name_list) and (r not in name_list) and (n not in name_list) and (d not in name_list)):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

    #===================== face recognition============

    def face_recog(self):
        # messagebox.showinfo("HFDS","1",parent=self.root)
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            # messagebox.showinfo("HFDS","2",parent=self.root)
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]

            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)

                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                #print(clf.predict(gray_image[y:y+h,x:x+w]),'/*+-*-+')
                confidence=int((100*(1-predict/300)))
                # messagebox.showinfo("HFDS","3",parent=self.root)
                conn=mysql.connector.connect(host="localhost",username='root',password="Karthik@123",database="face_recognizer")
                my_cursor=conn.cursor()
                # messagebox.showinfo("HFDS","4",parent=self.root)
                #print(id)
                my_cursor.execute("select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)
                # print(n)
                # messagebox.showinfo("HFDS","5",parent=self.root)
                my_cursor.execute("select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)
                # print(r)
                # messagebox.showinfo("HFDS","6",parent=self.root)
                my_cursor.execute("Select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("Select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i) 
                # print(d)
                # messagebox.showinfo("HFDS","7",parent=self.root)
                if confidence>77:
                    # messagebox.showinfo("HFDS","8",parent=self.root)
                    #cv2.putText(img,f"Id:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"ROLL:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"NAME:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    cv2.putText(img,f"DEPARTMENT:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(0,255,0),2)
                    self.mark_attendance(i,r,n,d)
                    # messagebox.showinfo("HFDS","8",parent=self.root)
                else:
                    # messagebox.showinfo("HFDS","9",parent=self.root)
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"UNKNOWN FACE",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),2)

                coord=[x,y,w,h]
                # messagebox.showinfo("HFDS","10",parent=self.root)
            return coord

        
        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"face",clf)
            return img

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")


        video_cap=cv2.VideoCapture(0)

        while True:
            ret,img=video_cap.read()
            img=recognize(img,clf,faceCascade)
            cv2.imshow("WELCOME TO FACE RECOGNITION",img)

            if cv2.waitKey(1)==13:
                break
        video_cap.release()
        cv2.destroyAllWindows()
    
 


if __name__ == '_main_':
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()