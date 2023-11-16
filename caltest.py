""" from tkcalendar import Calendar
import customtkinter as ctk
from tkinter import ttk

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.geometry("550x400")

frame = ctk.CTkFrame(root)
frame.pack(fill="both", padx=10, pady=10, expand=True)

style = ttk.Style(root)
style.theme_use("default")

cal = Calendar(frame, selectmode='day', locale='en_US', disabledforeground='red',
               cursor="hand2", background=ctk.ThemeManager.theme["CTkFrame"]["fg_color"][1],
               selectbackground=ctk.ThemeManager.theme["CTkButton"]["fg_color"][1])
cal.pack(fill="both", expand=True, padx=10, pady=10)

root.mainloop()

 """
"""
   # Create a frame for calendar
    frame_for_calendar = ctk.CTkFrame(window, width=820, height=350)
    frame_for_calendar.place(x=350, y=100)

    cal = Calendar(frame_for_calendar, selectmode="day", year=2023, month=11, day=1,font="Arial 14", selectforeground="white", cursor="hand2")
    cal.place(x=0, y=100)
"""

