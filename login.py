import tkinter as tk
import mysql.connector
import bcrypt



#########################################################################################################################################
# registration page
def registration_page():
    window = tk.Tk()
    window.title("User Registration")

    # Create and place widgets in the window
    label_username = tk.Label(window, text="Username:")
    label_username.pack()

    username_entry = tk.Entry(window)
    username_entry.pack()

    label_password = tk.Label(window, text="Password:")
    label_password.pack()

    password_entry = tk.Entry(window, show="*")
    password_entry.pack()

    label_whatsapp = tk.Label(window, text="WhatsApp:")
    label_whatsapp.pack()

    whatsapp_entry = tk.Entry(window)
    whatsapp_entry.pack()

    label_email = tk.Label(window, text="Email:")
    label_email.pack()

    email_entry = tk.Entry(window)
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

    register_button = tk.Button(window, text="Register", command=lambda:[register_user(), close_window()])
    register_button.pack()

    login_button = tk.Button(window, text="Login", command=lambda: [close_window(), login_page()])
    login_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    window.mainloop()
#########################################################################################################################################
#########################################################################################################################################
# login page
def login_page():
    window = tk.Tk()
    window.title("User Login")

    label_username = tk.Label(window, text="Username:")
    label_username.pack()

    username_entry = tk.Entry(window)
    username_entry.pack()

    label_password = tk.Label(window, text="Password:")
    label_password.pack()

    password_entry = tk.Entry(window, show="*")
    password_entry.pack()


    def process_login():
        entered_username = username_entry.get()
        entered_password = password_entry.get()

        connection = mysql.connector.connect(
            host="localhost",
            user="yash",
            password="root",
            database="calendar_db"
        )

        cursor = connection.cursor()

        # Retrieve the hashed password from the database as bytes
        cursor.execute("SELECT password FROM userdata WHERE username=%s", (entered_username,))
        hashed_password_bytes = cursor.fetchone()

        if hashed_password_bytes:
            # Check if the entered password matches the stored hashed password
            if bcrypt.checkpw(entered_password.encode('utf-8'), hashed_password_bytes[0].encode('utf-8')):
                login_status_label.config(text="Login successful")
                # Close the window if login is successful
                window.after(2000, window.destroy)
            else:
                login_status_label.config(text="Login failed")
        else:
            login_status_label.config(text="User not found")

        cursor.close()

    def user_temp_data():
        username = username_entry.get()

        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="yash",
                password="root",
                database="calendar_db"
            )
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS user_temp (username VARCHAR(255), whatsapp VARCHAR(255), email VARCHAR(255))")
            cursor.execute("SELECT whatsapp, email FROM userdata WHERE username=%s", (username,))
            user_data = cursor.fetchone()
            if user_data:
                cursor.execute("INSERT INTO user_temp (username, whatsapp, email) VALUES (%s, %s, %s)", (username, user_data[0], user_data[1]))
                connection.commit()
                print("Data inserted into user_temp table.")
            else:
                print("User not found or missing data.")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
            connection.close()


    # executing all/multiple functions
    def execute_multiple_functions():
        process_login()
        user_temp_data()



    login_button = tk.Button(window, text="Login", command=execute_multiple_functions)
    login_button.pack()

    registration_button = tk.Button(window, text="Register", command=lambda: [window.destroy(), registration_page(), login_page()])
    registration_button.pack()

    login_status_label = tk.Label(window, text="")
    login_status_label.pack()

    window.mainloop()



if __name__ == "__main__":
    login_page()

