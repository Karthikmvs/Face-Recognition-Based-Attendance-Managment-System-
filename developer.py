from tkinter import *      #FOR GUI
from tkinter import ttk     #HAS SOME STYLING
from PIL import Image,ImageTk      #For manipulating images
from tkinter import messagebox
import mysql.connector
import cv2
from datetime import datetime
from time import strftime

class developer:
    def __init__(self,root):    #root is the window name
        self.root=root
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        root.geometry('%dx%d+%d+%d' % (screen_width, screen_height, 0, 0))
        self.root.title("Developers")
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
        img3=Image.open("SourceImages/developers.jpg")
        img3=img3.resize((int(screen_width),int(5*screen_height/6)),Image.ANTIALIAS) #height,width
        self.photoimg3=ImageTk.PhotoImage(img3) #setting the above pic

        bg_img=Label(self.root,image=self.photoimg3) #creating a label image
        bg_img.place(x=0,y=int(screen_height/6),width=screen_width,height=int(5*screen_height/6)) #placing the image label

        title_lbl=Label(bg_img,text="DEVELOPERS",font=("times new roman",25,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=screen_width,height=int(screen_height/16))
        #time
        def time():
            string=strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000,time)
        lbl = Label(title_lbl,font=("times new roman",int(screen_height/52.5),"bold"),background='white',foreground='blue')
        lbl.place(x=10,y=0,width=int(screen_width/13.9),height=int(screen_height/20))
        time()


        #Karthik
        img4=Image.open("SourceImages/karthik.jpg")
        img4=img4.resize((int(screen_width/8.7),int(screen_height/4.77)),Image.ANTIALIAS) #height,width
        self.photoimg4=ImageTk.PhotoImage(img4) #setting the above pic

        b1=Button(bg_img,image=self.photoimg4,cursor="hand2")
        b1.place(x=int(screen_width/19.2),y=int(5*screen_height/55.2),width=int(screen_width/8.7),height=int(screen_height/4.77))

        b1_1=Button(bg_img,text="KARTHIK",cursor="hand2",font=("times new roman",int(screen_height/52.5),"bold"),bg="#1a75ff",fg="white")
        b1_1.place(x=int(screen_width/19.2),y=int((5*screen_height/55.2)+(screen_height/4.77)),width=int(screen_width/8.7),height=int(screen_height/26.25))


        #charan
        img5=Image.open("SourceImages/charan1.jpg")
        img5=img5.resize((int(screen_width/8.7),int(screen_height/4.77)),Image.ANTIALIAS) #height,width
        self.photoimg5=ImageTk.PhotoImage(img5) #setting the above pic

        b2=Button(bg_img,image=self.photoimg5,cursor="hand2")
        b2.place(x=int(screen_width/4.5),y=int(5*screen_height/55.2),width=int(screen_width/8.7),height=int(screen_height/4.77))

        b2_1=Button(bg_img,text="CHARAN",cursor="hand2",font=("times new roman",int(screen_height/52.5),"bold"),bg="#1a75ff",fg="white")
        b2_1.place(x=int(screen_width/4.5),y=int((5*screen_height/55.2)+(screen_height/4.77)),width=int(screen_width/8.7),height=int(screen_height/26.25))

        
        #ANISH
        img6=Image.open("SourceImages/anish.jpg")
        img6=img6.resize((int(screen_width/8.7),int(screen_height/4.77)),Image.ANTIALIAS) #height,width
        self.photoimg6=ImageTk.PhotoImage(img6) #setting the above pic

        b3=Button(bg_img,image=self.photoimg6,cursor="hand2")
        b3.place(x=int(screen_width/2.55),y=int(5*screen_height/55.2),width=int(screen_width/8.7),height=int(screen_height/4.77))

        b3_1=Button(bg_img,text="ANISH",cursor="hand2",font=("times new roman",int(screen_height/52.5),"bold"),bg="#1a75ff",fg="white")
        b3_1.place(x=int(screen_width/2.55),y=int((5*screen_height/55.2)+(screen_height/4.77)),width=int(screen_width/8.7),height=int(screen_height/26.25))

        #LADDU
        img7=Image.open("SourceImages/laddu.jpg")
        img7=img7.resize((int(screen_width/8.7),int(screen_height/4.77)),Image.ANTIALIAS) #height,width
        self.photoimg7=ImageTk.PhotoImage(img7) #setting the above pic

        b4=Button(bg_img,image=self.photoimg7,cursor="hand2")
        b4.place(x=int(screen_width/7.28),y=int(5*screen_height/10.2),width=int(screen_width/8.7),height=int(screen_height/4.77))

        b4_1=Button(bg_img,text="BHUVAN",cursor="hand2",font=("times new roman",int(screen_height/52.5),"bold"),bg="#1a75ff",fg="white")
        b4_1.place(x=int(screen_width/7.28),y=int((5*screen_height/10.2)+(screen_height/4.77)),width=int(screen_width/8.7),height=int(screen_height/26.25))

        #UJWAL
        img8=Image.open("SourceImages/ujwal.jpg")
        img8=img8.resize((int(screen_width/8.7),int(screen_height/4.77)),Image.ANTIALIAS) #height,width
        self.photoimg8=ImageTk.PhotoImage(img8) #setting the above pic

        b5=Button(bg_img,image=self.photoimg8,cursor="hand2")
        b5.place(x=int(screen_width/3.2),y=int(5*screen_height/10.2),width=int(screen_width/8.7),height=int(screen_height/4.77))

        b5_1=Button(bg_img,text="UJWAL",cursor="hand2",font=("times new roman",int(screen_height/52.5),"bold"),bg="#1a75ff",fg="white")
        b5_1.place(x=int(screen_width/3.2),y=int((5*screen_height/10.2)+(screen_height/4.77)),width=int(screen_width/8.7),height=int(screen_height/26.25))

if __name__ == '__main__':
    root=Tk()
    obj=developer(root)
    root.mainloop()