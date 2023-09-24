import re
import tkinter as tk


def center_window(root, window_width, window_height):
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x_coordinate = int((screen_width / 2) - (window_width / 2))
    y_coordinate = int((screen_height / 2) - (window_height / 2))

    return f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}"


class Calculator:
    def __init__(self):
        self.expression = ""
        self.equation = tk.StringVar()
        self.signs = ["+", "-", "/", "*", "."]

    def set_equation(self):
        self.equation.set(self.expression)

    def calculate(self):
        if self.expression[-1] not in self.signs:
            try:
                self.expression = str(eval(self.expression))
            except SyntaxError:
                self.expression = "error"
            finally:
                self.set_equation()

    def clear(self):
        self.expression = ""
        self.set_equation()

    def press_button(self, button):
        expressions = re.split(r'[-/+*]', self.expression)

        button_text = button.cget("text").strip()

        if button_text == "." and "." in expressions[-1]:
            self.expression = self.expression
        else:
            if len(self.expression) == 0 and button_text in self.signs \
                    or button_text == "." and self.expression[-1] in self.signs \
                    or button_text == "0" and len(expressions[-1]) == 1 and expressions[-1] == "0":
                self.expression = self.expression
            elif len(self.expression) > 0 and self.expression[-1] in self.signs and button_text in self.signs:
                self.expression = self.expression[:-1] + button_text
            else:
                self.expression += button_text

        self.set_equation()
