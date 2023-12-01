import customtkinter as ctk
from tkcalendar import Calendar  # Import the Calendar widget
import mysql.connector
from tkinter import ttk
import openai
import datetime
from utils import get_holidays, get_events, get_username, get_email
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def app():
    window = ctk.CTk()
    window.title("Chronicle's of Events")
    window.geometry("1444x800")
    ctk.set_appearance_mode("Dark")
    ctk.set_default_color_theme("dark-blue")
    #Create a function to change the theme
    def change_theme():
        current_theme = ctk.get_appearance_mode()
        if current_theme == "Light":
            ctk.set_appearance_mode("Dark")
        else:
            ctk.set_appearance_mode("Light")
    switch = ctk.CTkSwitch(window, text="Light/Dark Mode", font=("Times New Roman", 10), width=15, height=2, fg_color="black")
    switch.configure(command=change_theme)
    switch.place(x=1400, y=20)
    #Heading for the window
    heading = ctk.CTkLabel(window, text="Chronicle's of Events", font=("Times New Roman", 70))
    heading.place(x=478, y=0)
    #####################################################################################################################################
    #Holiday for the frame
    frame_for_holidays = ctk.CTkFrame(window, width=335, height=710,fg_color="#18161e")
    frame_for_holidays.place(x=5, y=69)
    heading_for_holidays = ctk.CTkLabel(frame_for_holidays, text="Holidays", font=("Times New Roman", 30))
    heading_for_holidays.place(x=110, y=5)
    textbox_holiday = ctk.CTkTextbox(frame_for_holidays, width=325, height=650, font=("Times New Roman", 20))
    indian_holidays = ["Maha Shivaratri - 8th March","Republic Day - January 26th","Independence Day - August 15th","Gandhi Jayanti - October 2th","Diwali - November 1st","Holi - March 25th","Eid al-Fitr - April 8th","Eid al-Adha - June 16th","Christmas - December 25th","New Year's Day - January 1st","Makar Sankranti - January 15th","Pongal - January 15th","Baisakhi - April 14th","Navratri - 3th to 12th October","Durga Puja - 13th October","Ganesh Chaturthi - 7th September","Raksha Bandhan - 19th August","Janmashtami - 26th August","Onam - 5th September","Lohri - January 13","Guru Nanak Jayanti - 15th November ","Easter - 31th March","Good Friday - 29th"]
    textbox_holiday.insert("1.0", "\n\n".join(indian_holidays))
    textbox_holiday.place(x=5, y=50)
    # Add the holidays to the database and display them in the textbox
    def holiday():
        cal_date_str = cal.get_date()
        cal_date_obj = datetime.datetime.strptime(cal_date_str, "%m/%d/%y")
        # Extract year, month, and day
        year, month, day = cal_date_obj.year, cal_date_obj.month, cal_date_obj.day
        # Format the date as "January 26"
        formatted_date = cal_date_obj.strftime("%B %d")
        holiday_text = text_box.get("1.0", "end-1c")
        mydb = mysql.connector.connect(
            host="localhost",
            user="yash",
            password="root",
            database="chronicle_of_events"
        )
        mycursor = mydb.cursor()
        holiday = f"{formatted_date} - {holiday_text}"
        # Add the holiday to the database
        # Get the username_id from the user_temp table
        mycursor.execute("SELECT id FROM user_temp")
        myresult = mycursor.fetchone()
        if myresult:
            username_id = myresult[0]
            # Insert the holiday into the holidays table
            mycursor.execute("INSERT INTO holidays (username_id, holiday) VALUES (%s, %s)", (username_id, holiday))
            mydb.commit()
            print("Holiday added to the database.")
            # Display updated holidays
            textbox_holiday.delete("1.0", "end")
            textbox_holiday.insert("1.0", "\n\n".join(indian_holidays))
            mycursor.execute("SELECT holiday FROM holidays")
            myresult = mycursor.fetchall()
            if myresult:
                holidays_text = "\n\n".join([holiday[0] for holiday in myresult])
                textbox_holiday.insert("end", f"\n\n{holidays_text}")
            else:
                print("No holidays found.")
        mycursor.close()
        mydb.close()


    #####################################################################################################################################


    #####################################################################################################################################
    # Create a frame for Events
    frame_for_events = ctk.CTkFrame(window, width=335, height=710,fg_color="#18161e")
    frame_for_events.place(x=1180, y=69)

    heading_for_events = ctk.CTkLabel(frame_for_events, text="Events", font=("Times New Roman", 30))
    heading_for_events.place(x=135, y=5)
    user_events = ["POST MID SEMESTER EXAM","IP - 15 December","Chemistry - 18 December","Maths - 19 December","English - 20 December","Physics - 22 December"]
    
    textbox_events = ctk.CTkTextbox(frame_for_events, width=325, height=650, font=("Times New Roman", 20))
    textbox_events.place(x=5, y=50)

    textbox_events.insert("3.0", "\n\n".join(user_events))
    # Add the events to the database and display them in the textbox
    def event():
        cal_date_str = cal.get_date()
        cal_date_obj = datetime.datetime.strptime(cal_date_str, "%m/%d/%y")
        # Extract year, month, and day
        year, month, day = cal_date_obj.year, cal_date_obj.month, cal_date_obj.day
        # Format the date as "January 26"
        formatted_date = cal_date_obj.strftime("%B %d")
        event_text = text_box.get("1.0", "end-1c")
        event = f"{formatted_date} - {event_text}"

        # Add the event to the database
        mydb = mysql.connector.connect(
            host="localhost",
            user="yash",
            password="root",
            database="chronicle_of_events"
        )
        mycursor = mydb.cursor()

        # Get the username_id from the user_temp table
        mycursor.execute("SELECT id FROM user_temp")
        myresult = mycursor.fetchone()

        if myresult:
            username_id = myresult[0]

            # Insert the event into the events table
            mycursor.execute("INSERT INTO events (username_id, events) VALUES (%s, %s)", (username_id, event))
            mydb.commit()
            print("Event added to the database.")

            # Display updated events
            textbox_events.delete("1.0", "end")
            textbox_events.insert("1.0", "\n\n".join(user_events))
            mycursor.execute("SELECT events FROM events")
            myresult = mycursor.fetchall()
            if myresult:
                events_text = "\n\n".join([event[0] for event in myresult])
                textbox_events.insert("end", f"\n\n{events_text}")
            else:
                print("No events found.")
        else:
            print("Error: User ID not found.")
        mycursor.close()
        mydb.close()



    #####################################################################################################################################


    #####################################################################################################################################
    # Create a frame for calendar
    frame_for_calendar = ctk.CTkFrame(window, width=820, height=350,fg_color="#18161e")
    frame_for_calendar.place(x=350, y=100)
    style = ttk.Style(window)
    style.theme_use("default")
    cal = Calendar(frame_for_calendar, selectmode="day", year=2023,locale='en_US',disabledforeground='red', month=11, day=1,font="Arial 32", selectforeground="white", cursor="hand2",background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][1],selectbackground=ctk.ThemeManager.theme["CTkButton"]["fg_color"][1],showweeknumbers=False,firstweekday="monday",showothermonthdays=False)
    cal.place(x=150, y=0)
    ##################################################################################################################################### 

    #####################################################################################################################################
    # Create a Tabview
    tabview = ctk.CTkTabview(window, width=820, height=320, segmented_button_fg_color="#262330", fg_color="#18161e",segmented_button_unselected_color="#262330",anchor="W")
    custom_font = ctk.CTkFont("Times", 25)
    
    tabview._segmented_button.configure(font=custom_font)
    tabview._segmented_button.grid(row = 0, column=0, sticky="W")
    tabview.grid(row=1,column=0)

    tabview.add("Notes")
    tabview.add("Assistant")
 
    tabview.place(x=350, y=460)

    #Add a text box to write notes
    text_box = ctk.CTkTextbox(tabview.tab("Notes"), width=800, height=200, font=("Times New Roman", 20))
    text_box.place(x=0, y=0)
    #Add a button to save in holidays
    holiday_button = ctk.CTkButton(tabview.tab("Notes"), text="HOLIDAY", font=("Times New Roman", 20),command=holiday)
    holiday_button.place(x=0, y=220)
    #Add a button to save in events
    event_button = ctk.CTkButton(tabview.tab("Notes"), text="EVENT", font=("Times New Roman", 20),command=event)
    event_button.place(x=650, y=220)
    #####################################################################################################################################
    #send message to Email button


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
    Hello {username}!
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

    
    email_button = ctk.CTkButton(tabview.tab("Notes"), text="Send mail", font=("Times New Roman", 20),command= send_email("ip.project.2024.20750@gmail.com","vcya solo olcx hoba",email,"Chronicle of Events",message))
    email_button.place(x=300, y=220)
    
    #####################################################################################################################################

    # Add assiant in the assistant tab

    openai.api_key = "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"

    def ask_gpt(prompt):
        try:
            response = openai.Completion.create(
                engine="text-davinci-003",
                prompt=prompt,
                max_tokens=150
            )
            generated_text = response['choices'][0]['text']
            return generated_text
        except Exception as e:
            print(f"Error interacting with GPT: {e}")
            return "An error occurred while processing your request."
        
    def handle_assistant_query(assistant_input):
        user_query = assistant_input.get("1.0", "end-1c")  # Get user input
        if user_query.strip():  # Check if the input is not empty
            # Create a prompt including information about holidays and events
            cal_date_str = cal.get_date()
            cal_date_obj = datetime.datetime.strptime(cal_date_str, "%m/%d/%y")
            formatted_date = cal_date_obj.strftime("%B %d")
            
            prompt = f"""User Query: {user_query}\n\nindian_holidays=["Maha Shivaratri- 8th March","Republic Day - January 26th","Independence Day - August 15th","Gandhi Jayanti - October 2th","Diwali - November 1st","Holi - March 25th","Eid al-Fitr - April 8th","Eid al-Adha - June 16th","Christmas - December 25th","New Year's Day - January 1st","Makar Sankranti - January 15th","Pongal - January 15th","Baisakhi - April 14th","Navratri - 3th to 12th October","Durga Puja - 13th October","Ganesh Chaturthi - 7th September","Raksha Bandhan - 19th August","Janmashtami - 26th August","Onam - 5th September","Lohri - January 13","Guru Nanak Jayanti - 15th November ","Easter - 31th March","Good Friday - 29th"]
            
            \nEvents: ["POST MID SEMESTER EXAM","IP - 15 December","Chemistry - 18 December","Maths - 19 December","English - 20 December","Physics - 22 December"] \n 
            tell me what to in 100 words or less in 3 to 4 points bullet points

            if i ask about holidays then tell me about holidays in india in 100 words or less in 3 to 4 points bullet points
            if i ask when is the holiday then tell me the date of the holiday in 40 words or less
            for example query: when is diwali answer: diwali is on 1st november
            date = {formatted_date}
            when asked how many days are left for holiday or event then tell me the number of days left for the holiday or event
            for example query: how many days are left for diwali answer: 10 days are left for diwali
            """

            # Ask GPT for a response
            response = ask_gpt(prompt)

            # Display GPT's response to the user
            assistant_input.insert("end", "\n\n"+"ASSISTANT: " +response + "\n\n")
        else:
            print("Please enter a query.")




    assistant_input = ctk.CTkTextbox(tabview.tab("Assistant"), width=800, height=200, font=("Times New Roman", 20))
    assistant_input.place(x=0, y=0)

    assistant_button = ctk.CTkButton(tabview.tab("Assistant"), text="ASK", font=("Times New Roman", 20),command=lambda: handle_assistant_query(assistant_input))
    assistant_button.place(x=0, y=220)

    clear_button = ctk.CTkButton(tabview.tab("Assistant"), text="CLEAR", font=("Times New Roman", 20),command=lambda: assistant_input.delete("1.0", "end"))
    clear_button.place(x=650, y=220)

    window.mainloop()


if __name__ == "__main__":
    app()


