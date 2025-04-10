import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("tk")
window.geometry("500x50")

entry1 = tk.Entry(window,text = "entry widgets can be typed in", width = 24)
leble1 = tk.Label(window,text = "x")
entry2 = tk.Entry(window,text = "entry widgets can be typed in", width = 24)
leble2 = tk.Label(window,text = "=")
entry3 = tk.Entry(window,text = "entry widgets can be typed in", width = 24)

entry1.grid(row = 1, column = 1)
leble1.grid(row = 1, column = 2, rowspan = 1)
entry2.grid(row = 1, column = 3)
leble2.grid(row = 1, column = 4)
entry3.grid(row = 1, column = 5)

window.mainloop()