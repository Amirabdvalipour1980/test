import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('500x600')

# def on_click():
#     messagebox.showinfo('in yek info ast', 'hello ' )
# def om_click():
#     messagebox.showwarning('in yek warning ast', '253625')
#     messagebox.showerror('in yek error ast', 'hello ' )
e1 = tk.Entry(window, width=10, font=('Tahoma', 25))

def on_click():
   if e1.get() == '':
        messagebox.showinfo('in yek info ast', 'مشخصات کامل خود را وارد کنید' )
   else:
        messagebox.showwarning('in yek warning ast', 'شما وارد شدید')


b1 = tk.Button(window, padx=10, pady=10, font=('Tahoma', 20), text='click here', command=on_click)
e1.pack()
b1.pack()

window.mainloop()