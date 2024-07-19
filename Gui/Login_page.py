import sqlite3
import tkinter
import customtkinter
from PIL import ImageTk, Image
import tkinter.messagebox
import os

# Initialize the database
def init_database():
    conn = sqlite3.connect("users1.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            password TEXT
        )
    """)
    conn.commit()
    conn.close()


init_database()

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


def button_function():
    # Fetch user data from the database
    conn = sqlite3.connect("users1.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (entry1.get(), entry2.get()))
    user = cursor.fetchone()
    conn.close()
    if user:
        app.destroy()  # destroy current window and create a new one
        os.system("python Home_page.py")
    else:
        tkinter.messagebox.showerror("Error", "Invalid credentials: \n Username or Password is incorrect\n if you dont have account please sign up")
        # print("Invalid credentials")




app = customtkinter.CTk()  # creating custom tkinter windowapp.geometry("600x440")
app.title('Login')
app.geometry("500x500")
img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
l1 = customtkinter.CTkLabel(master=app, image=img1)
l1.place(x=0,y=0)

# creating custom frame
frame = customtkinter.CTkFrame(master=app, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = customtkinter.CTkLabel(master=frame, text="Log into your Account", font=('Century Gothic', 20))
l2.place(x=50, y=45)

entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Username')
entry1.place(x=50, y=110)

entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
entry2.place(x=50, y=165)

b3 = customtkinter.CTkButton(master=frame, text="Forget password?", font=('Century Gothic', 12), fg_color='transparent')
b3.place(x=155, y=195)

# Create custom button
button1 = customtkinter.CTkButton(master=frame, width=220, text="Login", command=button_function, corner_radius=6)
button1.place(x=50, y=240)

l3 = customtkinter.CTkLabel(master=frame, text="Dont have a account?", font=('Century Gothic', 12))
l3.place(x=50, y=290)

def start_game():
    app.destroy()
    os.system(f'python registration_page.py')
# Replace the command of the sign-up button with the sign_up function
button2 = customtkinter.CTkButton(master=frame, text="Sign up", command=start_game, fg_color='transparent', width=60)
button2.place(x=200, y=290)
app.mainloop()
