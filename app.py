import customtkinter as ctk
import mysql.connector 

mydb = mysql.connector.connect(
    host="localhost",
    user="yash",
    password="root",
    database="calendar_db"
)

mycursor = mydb.cursor()



import customtkinter as ctk

root = ctk.CTk()

left_frame = ctk.CTkFrame(root)
right_frame = ctk.CTkFrame(root)

left_frame.grid(row=0, column=0, sticky="nsew")
right_frame.grid(row=0, column=1, sticky="nsew")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)

label = ctk.CTkLabel(left_frame, text="This is a label.")
button = ctk.CTkButton(right_frame, text="This is a button.")

label.grid(row=0, column=0, sticky="nsew")
button.grid(row=0, column=0, sticky="nsew")

root.mainloop()
