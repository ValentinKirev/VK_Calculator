import tkinter as tk
from utils import center_window, Calculator
from PIL import Image, ImageTk

# define window
root = tk.Tk()

# window configuration
root.title("VK_CALCULATOR")
root.resizable(False, False)
root.geometry(center_window(root, 352, 428))
ico = Image.open('logo.jpg')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# initialize calculator object
calculator = Calculator()

# configure and place expression field
expression_field = tk.Label(root, textvariable=calculator.equation, bg="#c4abab", font="sans 20 bold", anchor="e")
expression_field.grid(row=1, column=0, columnspan=4, sticky="nesw", ipady=14)

# configure and place buttons
button_clear = tk.Button(root, text=" C ", fg="black", bg="#d914e3", font="sans 11 bold", width=8, height=3,
                         borderwidth=5, relief="raised", command=calculator.clear)
button_clear.grid(row=2, column=0)

button_percentage = tk.Button(root, text=" % ", fg="black", bg="#d914e3", font="sans 11 bold", width=8, height=3,
                              borderwidth=5, relief="raised", command=calculator.percentage)
button_percentage.grid(row=2, column=1)

button_power = tk.Button(root, text=" \u232b ", fg="black", bg="#d914e3", font="sans 11 bold", width=8, height=3,
                         borderwidth=5, relief="raised", command=calculator.remove)
button_power.grid(row=2, column=2)

button_plus = tk.Button(root, text=" + ", fg="black", bg="#14e3a5", font="sans 11 bold", width=8, height=3,
                        borderwidth=5, relief="raised", command=lambda: calculator.press_button(button_plus))
button_plus.grid(row=2, column=3)

button1 = tk.Button(root, text=" 1 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3,
                    borderwidth=5, relief="raised", command=lambda: calculator.press_button(button1))
button1.grid(row=3, column=0)

button2 = tk.Button(root, text=" 2 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3,
                    borderwidth=5, relief="raised", command=lambda: calculator.press_button(button2))
button2.grid(row=3, column=1)

button3 = tk.Button(root, text=" 3 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3,
                    borderwidth=5, relief="raised", command=lambda: calculator.press_button(button3))
button3.grid(row=3, column=2)

button_minus = tk.Button(root, text=" - ", fg="black", bg="#14e3a5", font="sans 11 bold", width=8, height=3,
                         borderwidth=5, relief="raised", command=lambda: calculator.press_button(button_minus))
button_minus.grid(row=3, column=3)

button4 = tk.Button(root, text=" 4 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3,
                    borderwidth=5, relief="raised", command=lambda: calculator.press_button(button4))
button4.grid(row=4, column=0)

button5 = tk.Button(root, text=" 5 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3,
                    borderwidth=5, relief="raised", command=lambda: calculator.press_button(button5))
button5.grid(row=4, column=1)

button6 = tk.Button(root, text=" 6 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3,
                    borderwidth=5, relief="raised", command=lambda: calculator.press_button(button6))
button6.grid(row=4, column=2)

button_multiply = tk.Button(root, text=" * ", fg="black", bg="#14e3a5", font="sans 11 bold", width=8, height=3,
                            borderwidth=5, relief="raised", command=lambda: calculator.press_button(button_multiply))
button_multiply.grid(row=4, column=3)

button7 = tk.Button(root, text=" 7 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3,
                    borderwidth=5, relief="raised", command=lambda: calculator.press_button(button7))
button7.grid(row=5, column=0)

button8 = tk.Button(root, text=" 8 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3,
                    borderwidth=5, relief="raised", command=lambda: calculator.press_button(button8))
button8.grid(row=5, column=1)

button9 = tk.Button(root, text=" 9 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3,
                    borderwidth=5, relief="raised", command=lambda: calculator.press_button(button9))
button9.grid(row=5, column=2)

button_divide = tk.Button(root, text=" / ", fg="black", bg="#14e3a5", font="sans 11 bold", width=8, height=3,
                          borderwidth=5, relief="raised", command=lambda: calculator.press_button(button_divide))
button_divide.grid(row=5, column=3)

button_sign_change = tk.Button(root, text=" +/- ", fg="black", bg="#d914e3", font="sans 11 bold", width=8, height=3,
                               borderwidth=5, relief="raised", command=calculator.change_sign)
button_sign_change.grid(row=6, column=0)

button0 = tk.Button(root, text=" 0 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3,
                    borderwidth=5, relief="raised", command=lambda: calculator.press_button(button0))
button0.grid(row=6, column=1)

button_decimal = tk.Button(root, text=" . ", fg="black", bg="#d914e3", font="sans 11 bold", width=8, height=3,
                           borderwidth=5, relief="raised", command=lambda: calculator.press_button(button_decimal))
button_decimal.grid(row=6, column=2)

button_equal = tk.Button(root, text=" = ", fg="black", bg="#1905fa", font="sans 11 bold", width=8, height=3,
                         borderwidth=5, relief="raised", command=calculator.calculate)
button_equal.grid(row=6, column=3)

# run VK_CALCULATOR program
root.mainloop()
