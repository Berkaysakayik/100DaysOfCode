from tkinter import *
import tkinter as tk
window = Tk()



entry =tk.Entry(window).pack()
e = entry.get()
label = Label(window,text=e)
buton = Button(window,text="Buton")
buton.pack()
label.pack()



























window.mainloop()