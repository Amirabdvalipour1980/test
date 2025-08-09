import tkinter as tk

window = tk.Tk()
window.geometry('800x600')
window.title('2آزمایش دکمه ها')

def on_click():
    l1.config(text='on')
def off_click():
    l1.config(text='off')

l1 = tk.Label(window, text='')
b1 = tk.Button(window, text='off', width=20, height=4,command=off_click)
b2 = tk.Button(window, text='on', width=25, height=5,command=on_click)

b2.pack()
b1.pack()
l1.pack()

window.mainloop()