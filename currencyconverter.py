from tkinter import *
import tkinter as tk


window=tk.Tk()

window.title("Currency Converter")
window.geometry("450x300+150+150")
window.resizable(width="False",height="False")
window.config(bg="black")

title = tk.Label(text="Dollar to Ruppee converter", font=("Arial",15),bg="white",fg="black",relief=FLAT,borderwidth=5).place(x=100,y=3)

curr1 = tk.Label(text="Enter your amount in Dollars").place(x=30,y=50)
curr2 = tk.Label(text="Your converted amount in Ruppees").place(x=250,y=50)

value1 = tk.Entry()
value1.place(x=30,y=80)

value2 = tk.Text(width=15,height=1)
value2.place(x=250,y=80)

def calc():
    v1 = int(value1.get())
    v2 = 80 * v1
    value2.config(state="normal")
    value2.delete('1.0',tk.END)
    value2.insert(tk.END,v2)
    value2.config(state="disabled")

def reset():
    value1.delete('0',tk.END)
    # value1.insert(tk.END, " ")
    value2.config(state="normal")
    value2.delete('1.0',tk.END)
    value2.config(state="disabled")
    

convert = tk.Button(text="Convert into Ruppees",command=calc).place(x=30,y=120)
reset = tk.Button(text="Reset",command=reset).place(x=30,y=150)

window.mainloop()
