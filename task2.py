import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("T-Town Veterinary Clinic Database")
window.geometry("550x200")

label1 = tk.Label(window, text = "search by name", relief = 'groove')
label2 = tk.Label(window, text = "Client Database")
label3 = tk.Label(window, text = "Name")
label4 = tk.Label(window, text = "Type")
label5 = tk.Label(window, text = "Breed")
label6 = tk.Label(window, text = "Owner")
label7 = tk.Label(window, text = "Birthdate")
dogphoto = PhotoImage(file="dog.png")
label8 = tk.Label(window, image = dogphoto)
press1 = tk.Button(window, text = "Save Entry")
entry1 = tk.Entry(window,text = "entry widgets can be typed in", width = 17)
entry2 = tk.Entry(window,text = "entry widgets can be typed in", width = 17)
entry3 = tk.Entry(window,text = "entry widgets can be typed in", width = 17)
entry4 = tk.Entry(window,text = "entry widgets can be typed in", width = 17)
entry5 = tk.Entry(window,text = "entry widgets can be typed in", width = 17)
entry6 = tk.Entry(window,text = "entry widgets can be typed in", width = 20)
press2 = tk.Button(window, text = "< Previous")
press3 = tk.Button(window, text = "Next >")


label1.grid(row = 1, column = 4)

label2.grid(row = 2, column = 3)
label3.grid(row = 3, column = 1)
label4.grid(row = 3, column = 2)
label5.grid(row = 3, column = 3)
label6.grid(row = 3, column = 4)
label7.grid(row = 3, column = 5)
label8.grid(row = 2, column = 1)
press1.grid(row = 5, column = 3)
entry1.grid(row = 4, column = 1)
entry2.grid(row = 4, column = 2)
entry3.grid(row = 4, column = 3)
entry4.grid(row = 4, column = 4)
entry5.grid(row = 4, column = 5)
entry6.grid(row = 1, column = 5)
press2.grid(row = 5, column = 1)
press3.grid(row = 5, column = 5)



window.mainloop()
