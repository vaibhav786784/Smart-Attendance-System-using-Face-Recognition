from tkinter import*
from tkinter import ttk  #Containes style toolkit
from PIL import Image,ImageTk  # pil-pillow
from tkinter import messagebox
import mysql.connector

class Developer:
    def __init__(self,root):
        self.root=root
        # geometry set
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        title_lb1=Label(self.root,text="DEVELOPER",font=("time new roman",35,"bold"),bg="blue",fg="red")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        img_top=Image.open("Images/dev.jpg")
        img_top=img_top.resize((1366,768),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        first_lb=Label(self.root, image=self.photoimg_top)
        first_lb.place(x=0,y=50,width=1366,height=768)


        # Frame
        main_frame=Frame(first_lb,bd=2,bg="white")
        main_frame.place(x=850,y=0,width=500,height=300)

        img_l=Image.open("Images/developergif.gif")
        img_l=img_l.resize((200,200),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_l=ImageTk.PhotoImage(img_l)

        first_lb=Label(main_frame, image=self.photoimg_l)
        first_lb.place(x=300,y=0,width=200,height=150)

        # Developer Info
        dev_lb=Label(main_frame,text="SHIVIKA GUPTA(0114CS181100)",font=("time new roman",15,"bold"),bg="white",fg="#142552")
        dev_lb.place(x=10,y=200)

        dev_lb=Label(main_frame,text="VAIBHAV BILLORE(0114CS181113)",font=("time new roman",15,"bold"),bg="white",fg="#142552")
        dev_lb.place(x=10,y=225)

        dev_lb=Label(main_frame,text="VIDUSHI CHATURVEDI(0114CS181114)",font=("time new roman",15,"bold"),bg="white",fg="#142552")
        dev_lb.place(x=10,y=250)

      






















if __name__== "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()