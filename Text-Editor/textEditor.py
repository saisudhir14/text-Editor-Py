import tkinter as tk
from tkinter import Text, Button, filedialog, Menu, IntVar

root = tk.Tk()
root.title("Text Editor")

text = Text(root)
text.grid()

def saveas():
    t = text.get("1.0", "end-1c")
    savelocation = filedialog.asksaveasfilename()
    if savelocation:
        with open(savelocation, "w+") as file1:
            file1.write(t)

button = Button(root, text="Save", command=saveas)
button.grid()

def FontHelvetica():
    text.config(font="Helvetica")

def FontCourier():
    text.config(font="Courier")

font = Menu(root)
root.config(menu=font)
font.add_command(label="Helvetica", command=FontHelvetica)
font.add_command(label="Courier", command=FontCourier)

root.mainloop()
