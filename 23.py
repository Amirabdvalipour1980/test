import tkinter as tk

window = tk.Tk()
window.geometry('800x600')
window.title('تایمر')
window.after(600000) + 1

def on_click():
    l1.config(text='on')
def off_click():
    l1.config(text='off')
def reset_click():
    l1.config(text='off')

l1 = tk.Label(window, text='')
b1 = tk.Button(window, text='start', width=15, height=5,command=on_click)
b2 = tk.Button(window, text='stop', width=15, height=5,command=off_click)
b3 = tk.Button(window text='reset', width=15, height=5,command=reset_click)

b1.pack()
b2.pack()
b3.pack()
l1.pack()

window.mainloop()