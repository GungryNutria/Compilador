import json
import tkinter as tk
from lexic_analizer import LexAnalizer
from tkinter import Menu, Text, ttk
from tkinter.constants import W

window = tk.Tk()
la = LexAnalizer()
window.title("Compilador") 
window.minsize(300,150)

def setCode(event):
    
    la.startAnalize(TextArea.get("1.0",'end-1c'))
    Console.insert(tk.END,'\n'+la.getResult())

menubar = Menu(window)
window.config(menu=menubar)
filemenu = Menu(menubar,tearoff=0)
compilemenu = Menu(menubar,tearoff=0)

menubar.add_cascade(label='Archivos',menu=filemenu)
menubar.add_cascade(label='Compilar',menu=compilemenu)

TextArea = tk.Text(window, height=20,width=100)
TextArea.grid(column=0,row=0)

Console = tk.Text(window, height=20,width=100)
Console.insert(tk.END,'Consola.')
Console.grid(column=0,row=1)

lex = tk.Text(window, height=20,width=40)
lex.grid(column=1,row=0)

button = ttk.Button(window, text = "Compilar")
button.grid(column= 1, row = 1)
button.bind("<Button>",setCode)
#Eventos
window.mainloop()