import tkinter as tk

window = tk.Tk()
window.geometry('800x600')
window.title('2آزمایش دکمه ها')

def on1_click():
    l1.config(text='مرحله ی اول خوش آمدید')
def on2_click():
    l1.config(text='این مرحله ی دوم است ')
def on3_click():
    l1.config(text='شما به مرحله ی سوم رسیدید')
def on4_click():
    l1.config(text='پایان مراحل تبریک')

l1 = tk.Label(window, text='')
# l2 = tk.Label(window, text='')
# l3 = tk.Label(window, text='')
# l4 = tk.Label(window, text='')
b2 = tk.Button(window, text='بعدی', width=25, height=5,command=on1_click)
b2 = tk.Button(window, text='بعدی', width=25, height=5,command=on2_click)
b2 = tk.Button(window, text='بعدی', width=25, height=5,command=on3_click)
b2 = tk.Button(window, text='بعدی', width=25, height=5,command=on4_click)
b5 = tk.Button(window, text='آخر به اول', width=20, height=5,command=on4_click)
b5 = tk.Button(window, text='آخر به اول', width=20, height=5,command=on3_click)
b5 = tk.Button(window, text='آخر به اول', width=20, height=5,command=on2_click)
b5 = tk.Button(window, text='آخر به اول', width=20, height=5,command=on1_click)

b2.pack()
# b3.pack()
# b4.pack()
# b1.pack()
# b5.pack()
# b6.pack()
# b7.pack()
# b8.pack()
l1.pack()
# l2.pack()
# l3.pack()
# l4.pack()

window.mainloop()