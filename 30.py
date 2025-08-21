import tkinter as tk

window = tk.Tk()
window.geometry('500x600')

def show_value(val):
    window.config(bg='{red.get():02x}{green.get():02x}{blue.get():02x}')

red = tk.Scale(window, from_=0, to=255, orient='horizontal', length=200, command=show_value)
red.pack()
green = tk.Scale(window, from_=0, to=255, orient='horizontal', length=200, command=show_value)
blue = tk.Scale(window, from_=0, to=255, orient='horizontal', length=200, command=show_value)


window.mainloop()