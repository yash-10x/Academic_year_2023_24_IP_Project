import customtkinter as ctk
import mysql.connector 

mydb = mysql.connector.connect(
    host="localhost",
    user="yash",
    password="root",
    database="calendar_db"
)

mycursor = mydb.cursor()


root = ctk.CTk()


######################################################################################################
#chanhe theme of the application
# ###################################

###################################################################################################




#not needed
left_frame = ctk.CTkFrame(root, width=100, height=10)
right_frame = ctk.CTkFrame(root, width=100, height=10)

left_frame.grid(row=0, column=0, sticky="nsew")
right_frame.grid(row=20, column=0, sticky="nsew")

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=2)

label = ctk.CTkLabel(master=left_frame, text="This is a label.")
button = ctk.CTkButton(master=right_frame, text="This is a button.")

label.grid(row=0, column=0, sticky="nsew")
button.grid(row=0, column=0, sticky="nsew")

root.mainloop()