import tkinter as tk

win = tk.Tk()
win.title("PERSION")


def cal():
    getentry = float(entry.get())
    
    one = getentry*1.90 # 144p for per minute
    two = getentry*2.70 # 240p for per minute
    three = getentry*4.40 # 360p for per minute
    four = getentry*7.70 # 480p for per minute
    five = getentry*14.50 # 720p for per minute
    six = getentry*27.61 # 1080p for per minute
    seven = getentry*42.87 # 2k for per minute
    eight = getentry*85.85 # 4k for per minute

    label_1["text"] = f"144p = {one} MB"
    label_2["text"] = f"240p = {two} MB"
    label_3["text"] = f"360p = {three} MB"
    label_4["text"] = f"480p = {four} MB"
    label_5["text"] = f"720p = {five} MB"
    label_6["text"] = f"1080p = {six} MB"
    label_7["text"] = f"2K = {seven} MB"
    label_8["text"] = f"4K = {eight} MB"

    label_1.pack()
    label_2.pack()
    label_3.pack()
    label_4.pack()
    label_5.pack()
    label_6.pack()
    label_7.pack()
    label_8.pack()


frm = tk.Frame(master=win).pack()


firstlabel = tk.Label(text= "PersioN Internet Data Consumption by Video Resolution")
entrylabel = tk.Label(text= "Enter video length by minute (minute.second)")

label_1    = tk.Label(text="")
label_2    = tk.Label(text="")
label_3    = tk.Label(text="")
label_4    = tk.Label(text="")
label_5    = tk.Label(text="")
label_6    = tk.Label(text="")
label_7    = tk.Label(text="")
label_8    = tk.Label(text="")

entry      = tk.Entry(master=frm)

button     = tk.Button(text="Calculate", command=cal)


firstlabel.pack()
entrylabel.pack()
entry.pack()
button.pack()


win.mainloop()