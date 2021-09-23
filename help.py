from tkinter import*
from tkinter import ttk  #Containes style toolkit
from PIL import Image,ImageTk  # pil-pillow
from tkinter import messagebox
import mysql.connector

class Help:
    def __init__(self,root):
        self.root=root
        # geometry set
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition System")

        title_lb1=Label(self.root,text="HELP DESK",font=("time new roman",35,"bold"),bg="dark blue",fg="red")
        title_lb1.place(x=0,y=0,width=1366,height=45)

        img_top=Image.open("Images/help.jpg")
        img_top=img_top.resize((1366,768),Image.ANTIALIAS)   #High level img to Low level img
        self.photoimg_top=ImageTk.PhotoImage(img_top)

        first_lb=Label(self.root, image=self.photoimg_top)
        first_lb.place(x=0,y=55,width=1366,height=768)

        help_lb=Label(first_lb,text="Email: vaibhavbillore786@gmail.com",font=("time new roman",15,"bold"),fg="white",bg="black")
        help_lb.place(x=500,y=125)

        help_lb2=Label(first_lb,text="Email: shivikagupta2000@gmail.com",font=("time new roman",15,"bold"),fg="white",bg="black")
        help_lb2.place(x=500,y=165)

        help_lb3=Label(first_lb,text="Email: vidushichaturvedi333@gmail.com",font=("time new roman",15,"bold"),fg="white",bg="black")
        help_lb3.place(x=500,y=205)















if __name__== "__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()