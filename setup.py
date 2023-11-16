#########################################################################################################################################
#########################################################################################################################################
# Importing required modules
import mysql.connector
from tqdm import tqdm
import subprocess

#########################################################################################################################################
#########################################################################################################################################
# Setup database
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

            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS userdata (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username VARCHAR(255) UNIQUE,
                    password VARCHAR(255),
                    whatsapp VARCHAR(255),
                    email VARCHAR(255)
                )
            """)

            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS events (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username_id INT,
                    reminder_of_events VARCHAR(255),
                    FOREIGN KEY (username_id) REFERENCES userdata(id)
                )
            """)

            mycursor.execute("""
                CREATE TABLE IF NOT EXISTS holidays (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    username_id INT,
                    holiday VARCHAR(255),
                    FOREIGN KEY (username_id) REFERENCES userdata(id)
                )
            """)

            mycursor.close()
            mydb.close()

            with tqdm(total=100, desc="Creating database tables") as pbar:
                for i in range(100):
                    pbar.update(1)

            print("Database setup complete!")

        except mysql.connector.Error as err:
            print(f"Error: {err}")

        finally:
            mycursor.close()
            mydb.close()

    if __name__ == "__main__":
        choice = input("Enter 1 to reset the database or 2 to setup the environment or 3 to do both at once: ")
        if choice == "1":
            reset_database()
        elif choice == "2":
            setup_environment()
        elif choice == "3":
            reset_database()
            setup_environment()
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

########################################################################################################################################
########################################################################################################################################
# Install dependencies
def install_dependencies():
    try:
        subprocess.run(["pip", "install", "-r", "requirments.txt"], check=True)
        print("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies: {e}")
        raise SystemExit(e)
########################################################################################################################################
########################################################################################################################################

if __name__ == "__main__":
    install_dependencies() # Install dependencies
    setup() # Setup database


