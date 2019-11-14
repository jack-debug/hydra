#!/usr/bin/env python

from Tkinter import *
import tkMessageBox

window = Tk()
window.wm_withdraw()

#centre screen message
window.geometry("1x1+"+str(window.winfo_screenwidth()/2)+"+"+str(window.winfo_screenheight()/2))
tkMessageBox.showinfo(title="Hydra", message="Cut one head off, two more will grow back.")

def onclick():
    window.geometry("1x1+"+str(window.winfo_screenwidth()/2)+"+"+str(window.winfo_screenheight()/2))
    tkMessageBox.showinfo(title="Hydra", message="Cut one head off, two more will grow back.")
    window.geometry("1x1+"+str(window.winfo_screenwidth()/2)+"+"+str(window.winfo_screenheight()/2))
    tkMessageBox.showinfo(title="Hydra", message="Cut one head off, two more will grow back.")
