import mysql.connector
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="yash",
            password="root",
            database="chronicle_of_events"
        )
        mycursor = mydb.cursor()
        return mydb, mycursor
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None, None

def close_database_connection(mydb, mycursor):
    if mycursor:
        mycursor.close()
    if mydb and mydb.is_connected():
        mydb.close()


# get userid from user_temp table
def get_userid():
    try:
        mydb, mycursor = connect_to_database()
        mycursor.execute("SELECT id FROM user_temp LIMIT 1")
        userid = mycursor.fetchone()
        if userid:
            return userid[0]
        else:
            print("Userid not found.")
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        close_database_connection(mydb, mycursor)
userid = get_userid()

# get email from user_temp table
def get_email():
    try:
        mydb, mycursor = connect_to_database()
        mycursor.execute("SELECT email FROM user_temp LIMIT 1")
        email = mycursor.fetchone()
        if email:
            return email[0]
        else:
            print("Email not found.")
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        close_database_connection(mydb, mycursor)

# get events from events table
def get_events():
    try:
        mydb, mycursor = connect_to_database()
        mycursor.execute(f"SELECT events FROM events WHERE username_id={userid}")
        events = mycursor.fetchall()
        if events:
            return events
        else:
            print("Events not found.")
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        close_database_connection(mydb, mycursor)

# get username from user_temp table
def get_username():
    try:
        mydb, mycursor = connect_to_database()
        mycursor.execute("SELECT username FROM user_temp LIMIT 1")
        username = mycursor.fetchone()
        if username:
            return username[0]
        else:
            print("Username not found.")
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        close_database_connection(mydb, mycursor)

# get holidays from holidays table
def get_holidays():
    try:
        mydb, mycursor = connect_to_database()
        mycursor.execute(f"SELECT holiday FROM holidays WHERE username_id={userid}")
        holidays = mycursor.fetchall()
        if holidays:
            return holidays
        else:
            print("Holidays not found.")
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        close_database_connection(mydb, mycursor)

holiday = get_holidays()
events = get_events()
username = get_username()
email = get_email()

Postmideaxam = ["IP - 15 December","Chemistry - 18 December","Maths - 19 December","English - 20 December","Physics - 22 December"]

# Format holiday as a string with serial numbers and remove (' ')
formatted_holidays = "\n".join([f"[{i+1}] {h[0]}" for i, h in enumerate(holiday)])

# Format events as a string with serial numbers and remove (' ')
formatted_events = "\n".join([f"[{i+1}] {e[0]}" for i, e in enumerate(events)])

# Format Postmideaxam as a string with serial numbers
formatted_postmideaxam = "\n".join([f"[{i+1}] {exam}" for i, exam in enumerate(Postmideaxam)])

# Create the message
message = f"""
Hello yash!
[This is an automated message. Please do not reply to this email.]
Holidays are as follows:
{formatted_holidays}

Events are as follows:
{formatted_events}

Postmideaxam are as follows:
{formatted_postmideaxam}
"""
# a function that takes message as an input and sends it to eamil 
def send_email(sender_email, sender_password, to_email, subject, body):
    # Create the MIME object
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = subject

    # Attach the body of the email
    msg.attach(MIMEText(body, 'plain'))

    try:
        # Connect to Gmail's SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, to_email, msg.as_string())

        print("Email sent successfully!")
    except Exception as e:
        print(f"Error: {e}")

# Example usage:
sender_email = "ip.project.2024.20750@gmail.com"
sender_password = "vcya solo olcx hoba"
to_email = "yash890kk@gmail.com"
subject = "Chronicle of Events"
body = message

send_email(sender_email, sender_password, to_email, subject, body)



# todo
# 1. complete message from whatsapp and email
# 2. add otp forget password system








  

