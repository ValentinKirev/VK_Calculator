import re
from tkinter import StringVar


# define function to center window
def center_window(root, window_width, window_height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))

    return f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}"


# define Calculator Class
class Calculator:
    def __init__(self):
        self.expression = "0"
        self.equation = StringVar()
        self.signs = ["+", "-", "/", "*", "."]
        self.set_equation()

    # define function to change expression field textvariable attribute
    def set_equation(self):
        self.equation.set(self.expression)

    # define function to calculate result
    def calculate(self):
        try:
            if self.expression[-1] not in self.signs:
                self.expression = str(eval(self.expression))
        except ZeroDivisionError as ex:
            self.expression = f"ERROR: {ex}"
        finally:
            self.set_equation()

    # define function to clear expression field
    def clear(self):
        self.expression = "0"
        self.set_equation()

    # define function to remove last character from expression field
    def remove(self):
        self.expression = self.expression[:-1]

        if len(self.expression) == 0:
            self.expression = "0"

        self.set_equation()

    # define function to add or change characters in expression field
    def press_button(self, button):
        entries = re.split(r'[-/+*]', self.expression)
        button_text = button.cget("text").strip()

        if button_text == "." and "." in entries[-1]:
            self.expression = self.expression
        else:
            if len(self.expression) == 0 and button_text in self.signs \
                    or button_text == "." and self.expression[-1] in self.signs \
                    or button_text == "0" and len(entries[-1]) == 1 and entries[-1] == "0":
                self.expression = self.expression
            elif button_text != "0" and button_text not in self.signs and len(entries[-1]) == 1 and \
                    entries[-1][-1] == "0":
                self.expression = self.expression[:-1] + button_text
            elif len(self.expression) > 0 and self.expression[-1] in self.signs and button_text in self.signs:
                self.expression = self.expression[:-1] + button_text
            else:
                self.expression += button_text

        self.set_equation()
