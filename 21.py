import tkinter as tk
window = tk.Tk()

def jam():
    n = int(l1['text']) + 1
    l1.config(text=n)
def menha():
    h = int(l1['text']) - 1
    l1.config(text=h)    

b2 = tk.Button(window, text='+', command=jam, font=('IRANSans', 25))
b1 = tk.Button(window, text='-', command=menha, font=('IRANSans', 20))
l1 = tk.Label(window, text='0', font=('IRANSans', 20))

b2.pack()
b1.pack()
l1.pack()

window.mainloop()