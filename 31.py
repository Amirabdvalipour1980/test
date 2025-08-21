import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.geometry('500x600')

e1 = tk.Entry(window, width=10, font=('Tahoma', 25))
l1 = tk.Label(window, text = 'پایتخت ایران')
# e2 = tk.Entry(window, width=10, font=('Tahoma', 25))
# l2 = tk.Label(window, text = 'نام و نام خانوادگی')
# e3 = tk.Entry(window, width=10, font=('Tahoma', 25))
# l3 = tk.Label(window, text = 'کلمه ی عبور')

def on_click():
   if e1.get() == 'تهران':
        messagebox.showinfo('in yek info ast', 'آفرین جواب شما درست است' )
   else: 
       messagebox.showinfo('in yek info ast', 'جواب شما غلت است' )
#    elif e3.get() != '123456':
#        messagebox.showinfo('in yek info ast', 'کلمه ی عبور خود را درست وارد کنید' )
#    else:
#         messagebox.showwarning('in yek warning ast', 'شما وارد شدید')


b1 = tk.Button(window, padx=10, pady=10, font=('Tahoma', 20), text='click here', command=on_click)
e1.pack()
l1.pack()
# e2.pack()
# l2.pack()
# e3.pack()
# l3.pack()
b1.pack()

window.mainloop()