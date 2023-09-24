import tkinter as tk
from utils import center_window
from PIL import Image, ImageTk

root = tk.Tk()

root.title("VK_CALCULATOR")
root.resizable(False, False)
root.geometry(center_window(root, 350, 428))
ico = Image.open('logo.jpg')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)
equation = tk.StringVar()

expression_field = tk.Entry(root, textvariable=equation, bg="#c4abab", font="sans 16 bold")
expression_field.grid(columnspan=4, ipadx=54, ipady=20)

button_clear = tk.Button(root, text=" clear ", fg="black", bg="#d914e3", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button_clear.grid(row=2, column=0)

button_percentage = tk.Button(root, text=" % ", fg="black", bg="#d914e3", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button_percentage.grid(row=2, column=1)

button_power = tk.Button(root, text=" x\u00b2 ", fg="black", bg="#d914e3", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button_power.grid(row=2, column=2)

button_plus = tk.Button(root, text=" + ", fg="black", bg="#14e3a5", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button_plus.grid(row=2, column=3)

button1 = tk.Button(root, text=" 1 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button1.grid(row=3, column=0)

button2 = tk.Button(root, text=" 2 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button2.grid(row=3, column=1)

button3 = tk.Button(root, text=" 3 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button3.grid(row=3, column=2)

button_minus = tk.Button(root, text=" - ", fg="black", bg="#14e3a5", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button_minus.grid(row=3, column=3)

button4 = tk.Button(root, text=" 4 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button4.grid(row=4, column=0)

button5 = tk.Button(root, text=" 5 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button5.grid(row=4, column=1)

button6 = tk.Button(root, text=" 6 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button6.grid(row=4, column=2)

button_multiply = tk.Button(root, text=" * ", fg="black", bg="#14e3a5", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button_multiply.grid(row=4, column=3)

button7 = tk.Button(root, text=" 7 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button7.grid(row=5, column=0)

button8 = tk.Button(root, text=" 8 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button8.grid(row=5, column=1)

button9 = tk.Button(root, text=" 9 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button9.grid(row=5, column=2)

button_divide = tk.Button(root, text=" / ", fg="black", bg="#14e3a5", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button_divide.grid(row=5, column=3)

button_clear = tk.Button(root, text=" +/- ", fg="black", bg="#d914e3", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button_clear.grid(row=6, column=0)

button0 = tk.Button(root, text=" 0 ", fg="black", bg="#c79e0c", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button0.grid(row=6, column=1)

button_decimal = tk.Button(root, text=" . ", fg="black", bg="#d914e3", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button_decimal.grid(row=6, column=2)

button_equal = tk.Button(root, text=" = ", fg="black", bg="#1905fa", font="sans 11 bold", width=8, height=3, borderwidth=5, relief="raised")
button_equal.grid(row=6, column=3)

root.mainloop()

