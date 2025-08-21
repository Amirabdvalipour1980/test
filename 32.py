import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('500x600')

e1 = tk.Entry(window, width=10, font=('Tahoma', 25))
l1 = tk.Label(window, text = 'رمز عبور')
e2 = tk.Entry(window, width=10, font=('Tahoma', 25))
l2 = tk.Label(window, text = 'تکرار رمز عبور')


def on_click():
   if e1.get() == e2.get():
        messagebox.showinfo('in yek info ast', 'رمز با موفقیت ثبت شد' )
   else:
       messagebox.showinfo('in yek info ast', 'رمز ها مطابقت ندارد' )



b1 = tk.Button(window, padx=10, pady=10, font=('Tahoma', 20), text='click here', command=on_click)
e1.pack()
l1.pack()
e2.pack()
l2.pack()
b1.pack()

window.mainloop()