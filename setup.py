import mysql.connector
from tqdm import tqdm


def setup():
    def reset_database():
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="yash",
                password="root"
            )

            mycursor = mydb.cursor()
            mycursor.execute("DROP DATABASE IF EXISTS calendar_db")

            # progress bar 
            with tqdm(total=100, desc="Dropping database ") as pbar:
                for i in range(100):
                    pbar.update(1)

            print("Database dropped!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            mycursor.close()
            mydb.close()

    def setup_environment():
        try:
            mydb = mysql.connector.connect(
                host="localhost",
                user="yash",
                password="root"
            )

            mycursor = mydb.cursor()
            mycursor.execute("CREATE DATABASE IF NOT EXISTS calendar_db")
            mycursor.execute("USE calendar_db")

            # Create a 'userdata' table if it doesn't exist
            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS userdata (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) UNIQUE,  # Make username unique
                    password VARCHAR(255),
                    whatsapp VARCHAR(255),
                    email VARCHAR(255)
                )
            """)

            # Create an events table if it doesn't exist, connecting it with 'userdata' using a foreign key
            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS events (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username_id INT,
                    reminders VARCHAR(255),
                    FOREIGN KEY (username_id) REFERENCES userdata(id)
                )
            """)

            # Close the cursor
            mycursor.close()
            mydb.close()

            # progress bar 
            with tqdm(total=100, desc="Creating database tables") as pbar:
                for i in range(100):
                    pbar.update(1)

            print("Database setup complete!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

    if __name__ == "__main__":
        # Choose what to do
        choice = input("Enter 1 to reset the database or 2 to setup the environment: ")
        if choice == "1":
            reset_database()
        elif choice == "2":
            setup_environment()
        elif choice == "3":
            reset_database()
            setup_environment()
        else:
            print("Invalid choice. Please enter 1 or 2.")



if __name__ == "__main__":
    setup() 