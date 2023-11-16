import customtkinter as ctk
from tkcalendar import Calendar  # Import the Calendar widget
import mysql.connector
from tkinter import ttk
mydb = mysql.connector.connect(
    host="localhost",
    user="yash",
    password="root",
    database="calendar_db"
)

mycursor = mydb.cursor()


def app():
    window = ctk.CTk()
    window.title("Chronicle's of Events")
    window.geometry("1444x800")
    ctk.set_appearance_mode("Light")
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
    #Heading for the frame
    frame_for_holidays = ctk.CTkFrame(window, width=335, height=710)
    frame_for_holidays.place(x=5, y=69)

    heading_for_holidays = ctk.CTkLabel(frame_for_holidays, text="Holidays", font=("Times New Roman", 30))
    heading_for_holidays.place(x=110, y=5)
    #####################################################################################################################################


    #####################################################################################################################################
    # Create a frame for Events
    frame_for_events = ctk.CTkFrame(window, width=335, height=700)
    frame_for_events.place(x=1180, y=69)

    heading_for_events = ctk.CTkLabel(frame_for_events, text="Events", font=("Times New Roman", 30))
    heading_for_events.place(x=135, y=5)
    #####################################################################################################################################


    #####################################################################################################################################
    # Create a frame for calendar
    frame_for_calendar = ctk.CTkFrame(window, width=820, height=350)
    frame_for_calendar.place(x=350, y=100)
    style = ttk.Style(window)
    style.theme_use("default")
    cal = Calendar(frame_for_calendar, selectmode="day", year=2023,locale='en_US',disabledforeground='red', month=11, day=1,font="Arial 32", selectforeground="white", cursor="hand2",background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][1],selectbackground=ctk.ThemeManager.theme["CTkButton"]["fg_color"][1],showweeknumbers=False,firstweekday="monday",showothermonthdays=False)
    cal.place(x=150, y=0)
    ##################################################################################################################################### 

    #todo: (i)Create a function to add holidays
       # (ii)Create a function to add events
        #(iii)Create a function to send email and whatsapp message to the user on the day of the event

    window.mainloop()


if __name__ == "__main__":
    app()
