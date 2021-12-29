from tkinter import *
from db import DB

import datetime

class Form:
    def __init__(self, win):
        # Elements
        self.label_text = Label(win, text='Add a reminder')
        self.field_text = Entry()

        self.label_time = Label(win, text='Add a time')
        self.field_time = Entry()

        self.save_btn = Button(win, text='Save', command=self.save)

        # Positioning
        self.label_text.place(x=50, y=10)
        self.field_text.place(x=50, y=30)

        self.label_time.place(x=50, y=50)
        self.field_time.place(x=50, y=70)

        self.save_btn.place(x=50, y=90)
    def save(self):
        reminder_text = self.field_text.get()
        date_text = self.field_time.get()

        if not date_text:
            date_text = datetime.datetime.now().timestamp()

        save = DB.save_reminder(
            DB,
            reminder=reminder_text, 
            date=date_text
        )
