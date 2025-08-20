import tkinter as tk


window = tk.Tk()
window.geometry('500x600')


l1 = tk.Label(window, text = 'امروز صبح استخر')
l2 = tk.Label(window, text = 'حل پروژه ی پایتون')
l3 = tk.Label(window, text = 'رفتن به باشگاه')

def on1_click():
    l1.config(bg='green')
def on2_click():
    l2.config(bg='yellow')
def on3_click():
    l3.config(bg='red')


b1 = tk.Button(window, padx=5, pady=5, font=('Tahoma', 20), text='click here', command=on1_click)
b2 = tk.Button(window, padx=5, pady=5, font=('Tahoma', 20), text='click here', command=on2_click)
b3 = tk.Button(window, padx=5, pady=5, font=('Tahoma', 20), text='click here', command=on3_click)


l1.pack()
b1.pack()
l2.pack()

b2.pack()
l3.pack()
b3.pack()
l3.pack()


window.mainloop()