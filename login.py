#########################################################################################################################################
#########################################################################################################################################
# Importing modules
import tkinter as tk
import mysql.connector
import bcrypt
import customtkinter as ctk
from PIL import Image, ImageTk
from app import app

#########################################################################################################################################
#########################################################################################################################################
# login page
def login_page():
    window = ctk.CTk()
    window.title("User Login")
    window.geometry("1444x800")
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")

    def change_theme():
        current_theme = ctk.get_appearance_mode()
        if current_theme == "Light":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light") 
        
    switch = ctk.CTkSwitch(window, text="Light/Dark Mode",font=("Times New Roman",10),width=15, height=2,fg_color="black")
    switch.configure(command=change_theme)
    switch.place(x=1400,y=0)

    def process_login():
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        connection = mysql.connector.connect(
            host="localhost",
            user="yash",
            password="root",
            database="chronicle_of_events"
        )

        cursor = connection.cursor()

        # Retrieve the hashed password from the database as bytes
        cursor.execute("SELECT password FROM userdata WHERE username=%s", (entered_username,))
        hashed_password_bytes = cursor.fetchone()

        if hashed_password_bytes:
            # Check if the entered password matches the stored hashed password
            if bcrypt.checkpw(entered_password.encode('utf-8'), hashed_password_bytes[0].encode('utf-8')):
                login_status_label.configure(text="Login successful!", text_color="green")
                # store login user data in user_temp table
                cursor.execute("CREATE TABLE IF NOT EXISTS user_temp (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), whatsapp VARCHAR(255), email VARCHAR(255))")
                cursor.execute("SELECT whatsapp, email FROM userdata WHERE username=%s", (entered_username,))
                user_data = cursor.fetchone()
                if user_data:
                    cursor.execute("INSERT INTO user_temp (username, whatsapp, email) VALUES (%s, %s, %s)", (entered_username, user_data[0], user_data[1]))
                    connection.commit()
                    print("Data inserted into user_temp table.")
                else:
                    print("User not found or missing data.")
            
                # Close the login window
                window.destroy()
                # Open the calendar app
                app()

            else:
                login_status_label.configure(window, text="Login failed", text_color="red")
        else:
            login_status_label.configure(window, text="User not found", text_color="red")

        cursor.close()


    img = tk.PhotoImage(file="login.png",master=window)
    label = ctk.CTkLabel(window, text=" ", image=img,font=("Times New Roman",10))
    label.grid(row=0,column=0,)

    label_headding = ctk.CTkLabel(master=window,text="Login",font=("Times New Roman",70))
    label_headding.place(x=700,y=0,)

    label_username = ctk.CTkLabel(window, text="Username:",font=("Times New Roman",40))
    label_username.place(x=750,y=200)

    username_entry = ctk.CTkEntry(window,width=400,font=("Times New Roman",30))
    username_entry.place(x=930,y=205)

    label_password = ctk.CTkLabel(window, text="Password:",font=("Times New Roman",40))
    label_password.place(x=750,y=300)

    password_entry = ctk.CTkEntry(window, show="*",font=("Times New Roman",30),width=400)
    password_entry.place(x=930,y=305)

    login_status_label = ctk.CTkLabel(window, text=" ",font=("Times New Roman",20))
    login_status_label.place(x=740,y=80)

    login_button = ctk.CTkButton(window, text="Login", command=lambda: [process_login()],font=("Times New Roman",30),width=400)
    login_button.place(x=850,y=400)

    forgot_password_button = ctk.CTkButton(window, text="Forgot Password?", font=("Times New Roman",30),width=400,fg_color="transparent",bg_color="transparent",text_color=("#4158D0","white"),hover_color=("grey","grey"),command=lambda:[forgot_password_window()])
    forgot_password_button.place(x=850,y=500)

    registration_button = ctk.CTkButton(window, text="Register", command=lambda: [window.destroy(), registration_page()],font=("Times New Roman",30),width=400)
    registration_button.place(x=850,y=450)



    window.mainloop()



#########################################################################################################################################
#########################################################################################################################################
# registration page
def registration_page():

    ctk.set_appearance_mode("Light")
    ctk.set_default_color_theme("dark-blue")
    window = ctk.CTk()
    window.geometry("1444x800")
    window.title("User Registration")
    my_image = ctk.CTkImage(light_image=Image.open("register.png"),dark_image=Image.open("register.png"),size=(700, 800))
    label = ctk.CTkLabel(window, text=" ", image=my_image,width=50,height=50)
    label.grid(row=0,column=0,sticky="nsew")

    label_headding = ctk.CTkLabel(window,text="Register",font=("Times New Roman",50))
    label_headding.place(x=680,y=0,)
    
    def change_theme():
        current_theme = ctk.get_appearance_mode()
        if current_theme == "Light":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light") 
        
    switch = ctk.CTkSwitch(window, text="Light/Dark Mode",font=("Times New Roman",10),width=15, height=2,fg_color="black")
    switch.configure(command=change_theme)
    switch.place(x=1400,y=0)
    
    label_username = ctk.CTkLabel(window, text="Username:",font=("Times New Roman",40))
    label_username.place(x=750,y=200)

    username_entry = ctk.CTkEntry(window,width=400,font=("Times New Roman",30))
    username_entry.place(x=930,y=205)

    label_password = ctk.CTkLabel(window, text="Password:",font=("Times New Roman",40))
    label_password.place(x=750,y=270)

    password_entry = ctk.CTkEntry(window, show="*",font=("Times New Roman",30),width=400)
    password_entry.place(x=930,y=275)

    label_whatsapp = ctk.CTkLabel(window, text="WhatsApp:",font=("Times New Roman",40))
    label_whatsapp.place(x=740,y=340)

    whatsapp_entry = ctk.CTkEntry(window,width=400,font=("Times New Roman",30))
    whatsapp_entry.place(x=930,y=345)

    label_email = ctk.CTkLabel(window, text="Email:",font=("Times New Roman",40))
    label_email.place(x=780,y=410)

    email_entry = ctk.CTkEntry(window,width=400,font=("Times New Roman",30))
    email_entry.place(x=930,y=415)

    def register_user():
        username = username_entry.get()
        password = password_entry.get()
        whatsapp = whatsapp_entry.get()
        email = email_entry.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user="yash",
            password="root",
            database="chronicle_of_events"
        )

        mycursor = mydb.cursor()

        # Hash the password before storing it in the database
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

        # Insert user data into the 'userdata' table
        sql = "INSERT INTO userdata (username, password, whatsapp, email) VALUES (%s, %s, %s, %s)"
        values = (username, hashed_password, whatsapp, email)

        try:
            mycursor.execute(sql, values)
            mydb.commit()
            result_label.configure(text="Registration successful!",text_color = "green")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            result_label.configure(text="Registration failed",text_color="red",font=("Times New Roman",20))

        mydb.close()

    def close_window():
        window.after(50, window.destroy)

    register_button = ctk.CTkButton(window, text="Register", command=lambda:[register_user(),close_window(),login_page()],font=("Times New Roman",30),width=400)
    register_button.place(x=850,y=555)
    
    result_label = ctk.CTkLabel(window, text="",font=("Times New Roman",20))
    result_label.place(x=700,y=55)

    window.mainloop()

#########################################################################################################################################
#########################################################################################################################################
if __name__ == "__main__":
    login_page()

#########################################################################################################################################
#########################################################################################################################################
