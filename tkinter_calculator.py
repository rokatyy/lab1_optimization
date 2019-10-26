from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys

root = Tk()
root.title("Calculator")

bttn_list = [
"7", "8", "9", "+", "*",
"4", "5", "6", "-", "/",
"1", "2", "3",  "ln", "xⁿ",
"0", ".", "±",  "(",
")", "π", "e", "sin", "cos", "abs",
"√2","n!", "Clear", "=", "Exit"]

r = 1
c = 0
for i in bttn_list:
    rel = ""
    cmd=lambda x=i: calc(x)
    ttk.Button(root, text=i, command = cmd, width = 10).grid(row=r, column = c)
    c += 1
    if c > 4:
        c = 0
        r += 1

calc_entry = Entry(root, width = 33)
calc_entry.grid(row=0, column=0, columnspan=5)

#логика калькулятора
def calc(key):
    global memory
    if key == "=" or key == "sin" or key == "cos" or key == "ln" or key == "abs" or key == "√2" or key == "n!" or key == "xⁿ":
#исключение написания слов
        str1 = "-+0123456789.*/)("
        if not calc_entry.get():
            messagebox.showerror("Error!", "You did not enter the number!")
            return
        for char in calc_entry.get():
            if char not in str1:
                messagebox.showerror("Error!", "You did not enter the number!")
                return

    if key == "=":
#исчисления
        try:
            result = eval(calc_entry.get())
            calc_entry.insert(END, "=" + str(result))
        except:
            calc_entry.insert(END, "Error!")
            messagebox.showerror("Error!", "Check the correctness of data")

#очищение поля ввода
    elif key == "Clear":
        calc_entry.delete(0, END)

    elif key == "±":
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        try:
            if calc_entry.get()[0] == "-":
                calc_entry.delete(0)
            else:
                calc_entry.insert(0, "-")
        except IndexError:
            pass

    elif key == "π":
        calc_entry.insert(END, math.pi)

    elif key == "e":
        calc_entry.insert(END, math.e)

    elif key == "Exit":
        root.after(1, root.destroy)
        sys.exit
    elif key == "xⁿ":
        calc_entry.insert(END, "**")
    elif key == "sin":
        calc_entry.insert(END, "=" + str(math.sin(float(calc_entry.get()))))
    elif key == "cos":
        calc_entry.insert(END, "=" + str(math.cos(float(calc_entry.get()))))
    elif key == "(":
        calc_entry.insert(END, "(")
    elif key == ")":
        calc_entry.insert(END, ")")
    elif key == "n!":
        calc_entry.insert(END, "=" + str(math.factorial(float(calc_entry.get()))))
    elif key == "√2":
        calc_entry.insert(END, "=" + str(math.sqrt(float(calc_entry.get()))))
    elif key == "ln":
        calc_entry.insert(END, "=" + str(math.log(float(calc_entry.get()))))
    elif key == "abs":
        calc_entry.insert(END, "=" + str(math.fabs(float(calc_entry.get()))))
    else:
        if "=" in calc_entry.get():
            calc_entry.delete(0, END)
        calc_entry.insert(END, key)
root.mainloop()
