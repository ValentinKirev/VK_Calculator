import tkinter as tk
from utils import center_window, display_buttons, display_expression_field
from calculator import Calculator
from PIL import Image, ImageTk

# define window
root = tk.Tk()

# window configuration
root.title("VK_CALCULATOR")
root.resizable(False, False)
root.geometry(center_window(root, 352, 428))
ico = Image.open('images/logo.jpg')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)

# initialize calculator object
calculator = Calculator()

# configure and place expression field
display_expression_field(root, calculator)

# configure and place buttons
display_buttons(root, calculator)

# run VK_CALCULATOR program
root.mainloop()
