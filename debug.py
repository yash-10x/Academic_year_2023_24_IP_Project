import mysql.connector
import bcrypt
import customtkinter as ctk


#########################################################################################################################################
# registration page
def registration_page():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    window = ctk.CTk()
    window.geometry("400x300")
    window.title("User Registration")

    # Create and place widgets in the window
    label_username = ctk.CTkLabel(window, text="Username:")
    label_username.pack()

    username_entry = ctk.CTkEntry(window)
    username_entry.pack()

    label_password = ctk.CTkLabel(window, text="Password:")
    label_password.pack()

    password_entry = ctk.CTkEntry(window, show="*")
    password_entry.pack()

    label_whatsapp = ctk.CTkLabel(window, text="WhatsApp:")
    label_whatsapp.pack()

    whatsapp_entry = ctk.CTkEntry(window)
    whatsapp_entry.pack()

    label_email = ctk.CTkLabel(window, text="Email:")
    label_email.pack()

    email_entry = ctk.CTkEntry(window)
    email_entry.pack()

    def register_user():
        username = username_entry.get()
        password = password_entry.get()
        whatsapp = whatsapp_entry.get()
        email = email_entry.get()

        mydb = mysql.connector.connect(
            host="localhost",
            user="yash",
            password="root",
            database="calendar_db"
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
            result_label.config(text="Registration successful!")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            result_label.config(text="Registration failed")

        mydb.close()

    def close_window():
        window.after(500, window.destroy)

    register_button = ctk.CTkButton(window, text="Register", command=lambda:[register_user(), close_window()])
    register_button.pack()

    login_button = ctk.CTkButton(window, text="Login", command=lambda: [close_window(), login_page()])
    login_button.pack()

    result_label = ctk.CTkLabel(window, text="")
    result_label.pack()

    window.mainloop()


registration_page()


