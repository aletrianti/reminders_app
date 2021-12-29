import datetime
import time

from plyer import notification
from tkinter import *

from db import DB
from form import Form

# DB
db_init = DB()

# UI
window = Tk()

win = Form(window)

window.title('Reminders')
window.geometry('300x300+10+20')
window.resizable(False, False)
window.mainloop()
