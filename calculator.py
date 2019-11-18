from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import math
import sys


class Calculator:
    root = Tk()
    raw_button_size = 4
    button_titles = [
        "7", "8", "9", "+", "*",
        "4", "5", "6", "-", "/",
        "1", "2", "3", "ln", "xⁿ",
        "0", ".", "±", "(",
        ")", "π", "e", "sin", "cos", "abs",
        "√2", "n!", "Clear", "=", "Exit"]

    functions_required_filled_field = ["=", "sin", "cos", "ln", "abs", "√2", "n!", "xⁿ"]
    allowed_for_typing_symbols = "-+0123456789.*/)("

    def __init__(self):
        """
        Initializing calculator window.
        """
        self.root.title("Calculator")
        self.draw_buttons()
        self.entry = Entry(self.root, width=33)
        self.entry.grid(row=0, column=0, columnspan=5)
        self.actions = {
            "π": lambda: math.pi,
            "e": lambda: math.e,
            "xⁿ": lambda: "**",
            "sin": lambda: "=" + str(math.sin(float(eval(self.entry.get())))),
            "cos": lambda: "=" + str(math.cos(float(eval(self.entry.get())))),
            "(": lambda: "(",
            ")": lambda: ")",
            "n!": lambda: "=" + str(math.factorial(float(eval(self.entry.get())))),
            "√2": lambda: "=" + str(math.sqrt(float(eval(self.entry.get())))),
            "ln": lambda: "=" + str(math.log(float(eval(self.entry.get())))),
            "abs": lambda: "=" + str(math.fabs(float(eval(self.entry.get())))),
            "=": lambda: self.handle_equally_action(),
            "±": lambda: self.handle_plus_minus_action(),
        }

    def handle_equally_action(self):
        """
        Handling click on equally button.
        Returns:
            (string) - result of calculation or error text
        """
        try:
            return "=" + str(eval(self.entry.get()))
        except:
            messagebox.showerror("Error!", "Check the correctness of data")
            return "Error!"

    def handle_plus_minus_action(self):
        """
        Handling click on plus-minus button.
        """
        if "=" in self.entry.get():
            self.entry.delete(0, END)
        typed_symbol = self.entry.get()
        if len(typed_symbol) > 0 and typed_symbol[0] == "-":
            self.entry.delete(0)
        else:
            self.entry.insert(0, "-")

    def draw_buttons(self):
        """
        Draw buttons for calculation actions.
        """
        row = 1
        column = 0
        for i in self.button_titles:
            cmd = lambda x=i: self.on_click(x)
            ttk.Button(self.root, text=i, command=cmd, width=10).grid(row=row, column=column)
            column += 1
            if column > self.raw_button_size:
                column = 0
                row += 1

    @staticmethod
    def show_empty_error():
        """
        Show error for empty expressions field.
        """
        messagebox.showerror("Error!", "You did not enter the number!")

    def on_click(self, key):
        """
        Handling click on calculator button.
        Args:
            key (string) - type of calculation action
        """
        global memory
        if key in self.functions_required_filled_field:
            if not self.entry.get():
                self.show_empty_error()
                return
            for char in self.entry.get():
                if char not in self.allowed_for_typing_symbols:
                    self.show_empty_error()
                    return

        if key == "Clear":
            self.entry.delete(0, END)
        elif key == "Exit":
            self.root.after(1, self.root.destroy)
            sys.exit()
        elif key in self.actions:
            self.entry.insert(END, self.actions[key]())
        else:
            if "=" in self.entry.get():
                self.entry.delete(0, END)
            self.entry.insert(END, key)

    def run(self):
        self.root.mainloop()


Calculator().run()
