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
        except:
            self.expression = "ERROR!"
        finally:
            self.__check_expression_length()
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

    # define function to change number sign e.g. from negative to positive number
    def change_sign(self):
        last_entry = self.__find_last_entry()
        last_sign = self.__find_last_sign()

        if last_sign == "-":
            last_sign = ""
        elif last_sign == "+" or not last_sign:
            last_sign = "-"
        elif last_sign == "*" or last_sign == "/":
            last_sign = last_sign + "-"

        expression_length_without_last_entry = len(self.expression) - len(last_entry)

        if expression_length_without_last_entry > 0:
            self.expression = self.expression[:expression_length_without_last_entry - 1] + last_sign + last_entry
        else:
            self.expression = last_sign + last_entry

        self.__check_expression_length()
        self.set_equation()

    # define function to add or change characters in expression field
    def press_button(self, button):
        last_entry = self.__find_last_entry()
        button_text = button.cget("text").strip()

        try:
            if button_text == "." and "." in last_entry:
                self.expression = self.expression
            else:
                if len(self.expression) == 0 and button_text in self.signs \
                        or button_text == "." and self.expression[-1] in self.signs \
                        or button_text == "0" and last_entry == "0":
                    self.expression = self.expression
                elif button_text != "0" and button_text not in self.signs and last_entry == "0":
                    self.expression = self.expression[:-1] + button_text
                elif len(self.expression) > 0 and self.expression[-1] in self.signs and button_text in self.signs:
                    self.expression = self.expression[:-1] + button_text
                else:
                    self.expression += button_text
        except:
            self.expression = "ERROR!"

        self.__check_expression_length()
        self.set_equation()

    # define function that calculate percentage of last entry
    def percentage(self):
        last_entry = self.__find_last_entry()
        last_sign = self.__find_last_sign()

        expression_length_without_last_entry = len(self.expression) - len(last_entry)

        try:
            if expression_length_without_last_entry > 0:
                self.expression = self.expression[:expression_length_without_last_entry - 1] + last_sign + \
                                  str(float(last_entry) / 100)
            else:
                self.expression = last_sign + str(float(last_entry) / 100)
        except:
            self.expression = "ERROR!"
        finally:
            self.__check_expression_length()
            self.set_equation()

    # define function to find and return the index of last sign
    def __find_last_sign_index(self):
        return len(self.expression) - len(self.__find_last_entry()) - 1

    # define function to find and return the last sign
    def __find_last_sign(self):
        last_sign = ""
        last_sign_index = self.__find_last_sign_index()

        if last_sign_index >= 0:
            last_sign = self.expression[last_sign_index]

        return last_sign

    # define function to find and return last entry of calculator
    def __find_last_entry(self):
        return re.split(r'[-/+*]', self.expression)[-1]

    # define function to check if expression is with length above 25 characters
    def __check_expression_length(self):
        if len(self.expression) >= 21:
            self.expression = "Max 20 characters allowed"
