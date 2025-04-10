import tkinter as tk 
from tkinter import *
from tkinter import ttk

window = tk.Tk()
window.title("Example")
window.geometry("255x135")

dogphoto = PhotoImage(file="dog.png")
label1 = tk.Label(window, image = dogphoto)
label2 = tk.Label(window, text = "Pochacco")
label3 = tk.Label(window, text = "A cuddly little puppy! This is from the same\ncreators who brought you keropi and kero kero.", background="#aaffff")
label4 = tk.Label(window, text = '        ')
label5 = tk.Label(window, text = '        ')

label1.grid(row = 1, column = 2)
label2.grid(row = 1, column = 3)
label3.grid(row = 2, column = 1, columnspan = 4)
label4.grid(row = 1, column = 1)
label5.grid(row = 1, column = 4)




window.mainloop()