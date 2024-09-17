import tkinter as tk
from tkinter import *
import math

root = Tk()
root.title("Scientific Calculator")
root.iconbitmap(r"F:\Python Certication Practice\Python Tk inter projects\calculator.ico")
root.geometry("400x650")
root.resizable(False, False)

input_text = StringVar()
input_text.set("")

entry = Entry(root, font=("Arial", 20), textvariable=input_text, bd=8, insertwidth=2, width=22, borderwidth=4, relief=RIDGE, bg="#f7f7f7", fg="black", justify='right')
entry.grid(row=0, column=0, columnspan=4, pady=10)

def btn_click(item):
    current = input_text.get()
    input_text.set(current + str(item))

def btn_clear():
    input_text.set("")

def btn_delete():
    current = input_text.get()
    input_text.set(current[:-1])

def btn_equal():
    try:
        result = str(eval(input_text.get()))
        input_text.set(result)
    except:
        input_text.set("Error")

def btn_sqrt():
    current = input_text.get()
    input_text.set(str(math.sqrt(float(current))))

def btn_square():
    current = input_text.get()
    input_text.set(str(float(current) ** 2))

def btn_log():
    current = input_text.get()
    input_text.set(str(math.log10(float(current))))

def btn_ln():
    current = input_text.get()
    input_text.set(str(math.log(float(current))))

def btn_sin():
    current = input_text.get()
    input_text.set(str(math.sin(math.radians(float(current)))))

def btn_cos():
    current = input_text.get()
    input_text.set(str(math.cos(math.radians(float(current)))))

def btn_tan():
    current = input_text.get()
    input_text.set(str(math.tan(math.radians(float(current)))))

def btn_pi():
    input_text.set(str(math.pi))

def btn_exp():
    current = input_text.get()
    input_text.set(str(math.exp(float(current))))

def btn_power():
    current = input_text.get()
    input_text.set(current + "**")

def btn_mod():
    current = input_text.get()
    input_text.set(current + "%")

def btn_cancel():
    input_text.set("")

button_config = {
    "font": ("Arial", 14),
    "bd": 4,
    "relief": "raised",
    "bg": "#1f1f1f",
    "fg": "white",
    "activebackground": "#ffcc00",
    "activeforeground": "black",
    "width": 4,
    "height": 2
}

scientific_button_config = button_config.copy()
scientific_button_config["bg"] = "#2d2d2d"
scientific_button_config["fg"] = "#ffcc00"

buttons = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
]

for (text, row, col) in buttons:
    Button(root, text=text, command=lambda txt=text: btn_click(txt), **button_config).grid(row=row, column=col, padx=5, pady=5, sticky="nsew")

Button(root, text="C", command=btn_clear, **scientific_button_config).grid(row=5, column=0, padx=5, pady=5, sticky="nsew")
Button(root, text="DEL", command=btn_delete, **scientific_button_config).grid(row=5, column=1, padx=5, pady=5, sticky="nsew")
Button(root, text="√", command=btn_sqrt, **scientific_button_config).grid(row=5, column=2, padx=5, pady=5, sticky="nsew")
Button(root, text="x²", command=btn_square, **scientific_button_config).grid(row=5, column=3, padx=5, pady=5, sticky="nsew")

Button(root, text="log", command=btn_log, **scientific_button_config).grid(row=6, column=0, padx=5, pady=5, sticky="nsew")
Button(root, text="ln", command=btn_ln, **scientific_button_config).grid(row=6, column=1, padx=5, pady=5, sticky="nsew")
Button(root, text="sin", command=btn_sin, **scientific_button_config).grid(row=6, column=2, padx=5, pady=5, sticky="nsew")
Button(root, text="cos", command=btn_cos, **scientific_button_config).grid(row=6, column=3, padx=5, pady=5, sticky="nsew")

Button(root, text="tan", command=btn_tan, **scientific_button_config).grid(row=7, column=0, padx=5, pady=5, sticky="nsew")
Button(root, text="π", command=btn_pi, **scientific_button_config).grid(row=7, column=1, padx=5, pady=5, sticky="nsew")
Button(root, text="exp", command=btn_exp, **scientific_button_config).grid(row=7, column=2, padx=5, pady=5, sticky="nsew")
Button(root, text="^", command=btn_power, **scientific_button_config).grid(row=7, column=3, padx=5, pady=5, sticky="nsew")

Button(root, text="%", command=btn_mod, **scientific_button_config).grid(row=8, column=0, padx=5, pady=5, sticky="nsew")
Button(root, text="Cancel", command=btn_cancel, **scientific_button_config).grid(row=8, column=1, padx=5, pady=5, sticky="nsew", columnspan=2)
Button(root, text="=", command=btn_equal, **button_config).grid(row=8, column=3, padx=5, pady=5, sticky="nsew")

for i in range(9):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1)

root.mainloop()
