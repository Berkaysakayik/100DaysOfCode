import tkinter as tk

win = tk.Tk()
from tkinter import ttk
from tkinter import messagebox

win.title("PERSION Temperature Conversion Calculator")
win.geometry("730x220")
win.resizable(False,False)

def clear():
    tempCombo1.set('')
    tempCombo2.set('')
    lbl_res["text"] = f"Results: " 
    entry.delete(first=0, last='end')

def get_index1(*arg):
    # lbl=tk.Label(win, text=" " + str(varCombo1.get()), font=('Helvetica 12')).grid(column=2,row=4) #str(tempCombo1.current()) # index almak için
    return str(tempCombo1.current())
    # return str(varCombo1.get()) # combo üstündeki değeri almak

def get_index2(*arg):
    return str(tempCombo2.current())
    # return str(varCombo2.get())  # combo üstündeki değeri almak



def calc():
    if entry.get() :
        # **************** fah to other termo values ****************
        if get_index1() == "0": 
            if get_index2()=="0":
                f = int(entry.get())
                lbl_res["text"] = f"Results: {f} °F"  
                print(f)
            elif get_index2()=="1":
                c=int(float(entry.get())-32)/9*5
                lbl_res["text"] = f"Results: {c} °C"  
                print(c)

            elif get_index2()=="2":
                r=int(float(entry.get())+459.67)
                lbl_res["text"] = f"Results: {r} °R"  
                print(r)

            elif get_index2()=="3":
                k=int(float(entry.get())+459.67)/9*5
                lbl_res["text"] = f"Results: {k} °K"  
                print(k)


        # **************** celcius to other termo values ****************
        if get_index1() == "1":
            if get_index2()=="0":
                f = int(float(entry.get())) *9/5+32
                lbl_res["text"] = f"Results: {f} °F"  
                print(f)
            elif get_index2()=="1":
                c = int(entry.get())
                lbl_res["text"] = f"Results: {c} °C"  
                print(c)

            elif get_index2()=="2":
                r=int(float(entry.get())) / 9*5 + 491.67
                lbl_res["text"] = f"Results: {r} °R"  
                print(r)

            elif get_index2()=="3":
                k=int(float(entry.get())+273.15)            
                lbl_res["text"] = f"Results: {k} °K"  
                print(k)


        # **************** Reaumur to other termo values ****************
        if get_index1() == "2":
            if get_index2()=="0":
                fah = int(float(entry.get()))-459.67
                lbl_res["text"] = f"Results: {fah} °F"  
                print(fah)
            elif get_index2()=="1":
                c=int(float(entry.get())) / 9*5 -273.15
                lbl_res["text"] = f"Results: {c} °C"  
                print(c)

            elif get_index2()=="2":
                r = int(entry.get())
                lbl_res["text"] = f"Results: {r} °R"  
                print(r)

            elif get_index2()=="3":
                k=int(float(entry.get()))/5*9
                lbl_res["text"] = f"Results: {k} °K"  
                print(k)



        # **************** kelvin to other termo values ****************
        if get_index1() == "3":
            if get_index2()=="0":
                f = int(float(entry.get()))/5*9- 459.67
                lbl_res["text"] = f"Results: {f} °F"  
                print(f)
            elif get_index2()=="1":
                c=int(float(entry.get())) - 273.15
                lbl_res["text"] = f"Results: {c} °C"  
                print(c)

            elif get_index2()=="2":
                r=int(float(entry.get()))/5*9
                lbl_res["text"] = f"Results: {r} °R"  
                print(r)

            elif get_index2()=="3":
                k = int(entry.get())
                lbl_res["text"] = f"Results: {k} °K"  
                print(k)
    else:
        messagebox.showerror("Error", "Please enter a valid temperature value")

varCombo1 = tk.StringVar()

varCombo2 = tk.StringVar()

tempCombo1 = ttk.Combobox(win, width = 27, textvariable = varCombo1)
tempCombo2 = ttk.Combobox(win, width = 27, textvariable = varCombo2)


tempCombo1['values'] = ('Fahrenheit (Fahrenhayt)(°F)',
                          ' Santigrat (Celcius)(°C) ',
                          ' Reaumur (Reomür)(°R) ',
                          ' Kelvin (°K)')
  
tempCombo1.grid(column = 1, row = 0,pady=5)
varCombo1.trace('w', get_index1)


tempCombo2['values'] = ('Fahrenheit (Fahrenhayt)(°F)',
                          ' Santigrat (Celcius)(°C) ',
                          ' Reaumur (Reomür)(°R) ',
                          ' Kelvin (°K)')
  
tempCombo2.grid(column = 5, row = 0)
varCombo2.trace('w', get_index2)



temperature = tk.Frame(master=win)
entry = tk.Entry(master=temperature,font=25,width=5)
entry.grid(row=1, column=2,padx=5,pady=5)



from_lbl = tk.Label(text="From:",font=5)
from_lbl.grid(row=0, column=0,padx=20,pady=5)

btn = tk.Button(text="Convert", command=calc,font=25)
btn.grid(row=3, column=5,padx=30)

btn_clr = tk.Button(text="Clear", command=clear,font=25)
btn_clr.grid(row=3, column=1)

to_lbl = tk.Label(text="To:",font=25)
to_lbl.grid(row=0,column=2, padx=100,pady=15)
temperature.grid(row=2, column=2,pady=5)


lbl_res = tk.Label(text="Results:",font=5)
lbl_res.grid(row=4, column=2,pady=5)

win.mainloop()