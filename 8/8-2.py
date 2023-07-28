import tkinter as tk

def celsius_to_fahrenheit():
    c = int(entry.get())
    fah = (c*1.8) +32
    print(c,fah)
    fah_label["text"] = f"{fah}\N{DEGREE Fahrenheit}"  

win = tk.Tk()
win.title("Celsius to Fahrenheit Converter")

frmentry = tk.Frame(master=win)
entry = tk.Entry(master=frmentry,font=25,width=5)
entry.grid(row=0, column=0,padx=5)
lbl_cel = tk.Label(text="\N{DEGREE CELSIUS}",font=25)
lbl_cel.grid(row=0, column=1,sticky="w")

btn = tk.Button(text="Convert", command=celsius_to_fahrenheit,font=25)
btn.grid(row=0, column=1,padx=30)

fah_label = tk.Label(text="Fahrenheit",font=25)
fah_label.grid(row=0,column=2, padx=5)
frmentry.grid(row=0, column=0)

win.mainloop()