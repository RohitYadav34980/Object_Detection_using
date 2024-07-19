import sqlite3
import os
from customtkinter import *
from PIL import ImageTk, Image
import tkinter.messagebox

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


rapp = CTk()
rapp.title('Registration Page')
rapp.geometry('500x500')

img = ImageTk.PhotoImage(Image.open("pattern.png"))
imgtk = CTkLabel(rapp, image = img)
imgtk.place(x=0,y=0)

frame = CTkFrame(master=rapp, width=320, height=360, corner_radius=15)
frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = CTkLabel(master=frame, text="Sign up to your Account", font=('Century Gothic', 20))
l2.place(x=50, y=45)

username_entry = CTkEntry(master=frame, width=220, placeholder_text='Username')
username_entry.place(x=50, y=110)

password_entry = CTkEntry(master=frame, width=220, placeholder_text='Password', show="*")
password_entry.place(x=50, y=165)

# def register_user():
#         # Insert new user data into the database
#         conn = sqlite3.connect("users.db")
#         cursor = conn.cursor()
#         cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
#                        (username_entry.get(), password_entry.get()))
#         conn.commit()
#         conn.close()
#         rapp.destroy()

def register_user():
    # Connect to the database
    conn = sqlite3.connect("users1.db")
    cursor = conn.cursor()

    # Check if the username already exists
    cursor.execute("SELECT * FROM users WHERE username = ?", (username_entry.get(),))
    if cursor.fetchone() is not None:
        # If the username exists, show a message box and return to the login page
        tkinter.messagebox.showinfo("Error", "Username already exists. Please login.")
        start_game()
    else:
        # If the username does not exist, insert the new user data into the database
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)",
                       (username_entry.get(), password_entry.get()))
        conn.commit()
        conn.close()
        tkinter.messagebox.showinfo("Success", "Username successfully registered. Please login.")
        start_game()
        # rapp.destroy()

sign_up_button = CTkButton(master=frame, text="Sign Up", command=register_user)
sign_up_button.place(x=50,y=195)

l3 = CTkLabel(master=frame, text="Dont have a account?", font=('Century Gothic', 12))
l3.place(x=50, y=290)

def start_game():
    rapp.destroy()
    os.system(f'python Login_page.py')
# Replace the command of the sign-up button with the sign_up function
button2 = CTkButton(master=frame, text="Sign in", command=start_game, fg_color='transparent', width=60)
button2.place(x=200, y=290)
rapp.mainloop()