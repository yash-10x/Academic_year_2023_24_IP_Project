# Description: This file contains all the utility functions used in the project.
#messiging using whatsapp and email
#get whatsapp number and email id from database calendar_db tabel user_temp
#send message using twilio for whatsapp and for email using smtplib
import mysql.connector
import smtplib
import twilio
import random
import customtkinter as ctk

import mysql.connector

def get_whatsapp_number():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="yash",
            password="root",
            database="chronicle_of_events"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT whatsapp FROM user_temp LIMIT 1")
        whatsapp_number = mycursor.fetchone()
        if whatsapp_number:
            return whatsapp_number[0]
        else:
            print("WhatsApp number not found.")
            return None
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None
    finally:
        if mydb.is_connected():
            mydb.close()

whatsapp_number=get_whatsapp_number()
print(whatsapp_number)


mydb = mysql.connector.connect(
    host="localhost",
    user="yash",
    password="root",
    database="chronicle_of_events"
)

mycursor = mydb.cursor()

# Fetch events
mycursor.execute("SELECT events FROM events")
myresult_events = mycursor.fetchall()
events = "\n".join([event[0] for event in myresult_events])

# Fetch holidays
mycursor.execute("SELECT holiday FROM holidays")
myresult_holidays = mycursor.fetchall()
holidays = "\n".join([holiday[0] for holiday in myresult_holidays])

# Get WhatsApp number
whatsapp_number = get_whatsapp_number()

# Create the message
message = f"""Hello, this is a test message from Chronicle of Events \n
Your Upcoming Events/Holidays are:-
[i] Events: {events or 'No upcoming events'}
[ii] Holidays: {holidays or 'No upcoming holidays'} 
"""

# Print the message
print(message)

# Close the database connection
mydb.close()

""" def get_holiday_events(user_id):
    connection_with_db()
    mycursor.execute("select*from events where user_id=%s",userid)
    mycursor.execute("select*from holidays where user_id=%s",userid)


def send_email(email):
    s=smtplib.SMTP("localhost")
    s.putcmd("vrfy","%s{email}",user_temp[1])
    s.getreply(250, "Somebody OverHere <%s{email}>,"use_temp[1])
    data=get_holiday_events()
    smtplib.send("YOUR UP COMMING EVENT/HOLIDAYS \n %s{data)",data)
    s.quit()






def forgot_password():
    def opt():
        pass
    def update_pass_indb():
        pass
    def send_update_message():
        pass


 """












  

