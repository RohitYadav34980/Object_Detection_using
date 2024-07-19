from tkinter.ttk import Label
import os
from PIL import ImageTk, Image
from customtkinter import *

home = CTk()
home.title("Home Page")
home.geometry("900x500")

l1 = CTkLabel(master=home, text="Welcome to Object Detection!!!", font=("Arial Bold",20))
l1.place(x=90, y=50)

l2 = CTkLabel(master=home, text="This is our project here can detect object in two ways: ", font=("Arial",16))
l2.place(x=90,y=90)

l3 = CTkLabel(master=home, text="(1) uploading an image",font=("Arial",16))
l3.place(x=90,y=120)

l4 = CTkLabel(master=home, text="(2) by using webcam",font=("Arial",16))
l4.place(x=90,y=150)

img = Image.open("jpg_7271030.png")
img = img.resize((50,50), resample=Image.LANCZOS)
img1 = ImageTk.PhotoImage(img)

l5 = Label(master=home, image=img1, background="#242424")
l5.image = img1  # keep a reference to the image
l5.place(x=225,y=250)

def image_call():
    home.destroy()
    os.system(r"python C:\\Users\\muska\\Desktop\\objectdetection\\object\\image.py")
l6 = CTkButton(master=home, text="By Image", command=image_call)
l6.place(x=250,y=210)

img2 = Image.open("pngwing.com(3).png")
img2 = img2.resize((50,50), resample=Image.LANCZOS)
img3 = ImageTk.PhotoImage(img2)

l5 = Label(master=home, image=img3, background="#242424")
l5.image = img1  # keep a reference to the image
l5.place(x=225,y=380)

def webcam_call():
    home.destroy()
    os.system(r"python C:\Users\muska\Desktop\objectdetection\object\webcam.py")
l7 = CTkButton(master=home, text="By Webcam", command=webcam_call)
l7.place(x=250,y=310)
home.mainloop()
