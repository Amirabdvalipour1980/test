import tkinter as tk

window = tk.Tk()
window.geometry('170x200')

def on_click(a):
    print(a)
b0 = tk.Button(window, command=lambda: on_click('0'), text='0' , width=2)
b1 = tk.Button(window, command=lambda: on_click('1'), text='1' , width=2)
b2 = tk.Button(window, command=lambda: on_click('2'), text='2' , width=2)
b3 = tk.Button(window, command=lambda: on_click('3'), text='3' , width=2)
b4 = tk.Button(window, command=lambda: on_click('4'), text='4' , width=2)
b5 = tk.Button(window, command=lambda: on_click('5'), text='5' , width=2)
b6 = tk.Button(window, command=lambda: on_click('6'), text='6' , width=2)
b7 = tk.Button(window, command=lambda: on_click('7'), text='7' , width=2)
b8 = tk.Button(window, command=lambda: on_click('8'), text='8' , width=2)
b9 = tk.Button(window, command=lambda: on_click('9'), text='9' , width=2)
b10 = tk.Button(window, command=lambda: on_click('/'), text='/' , width=2)
b11 = tk.Button(window, command=lambda: on_click('*'), text='*' , width=2)
b12 = tk.Button(window, command=lambda: on_click('-'), text='-' , width=2)
b13 = tk.Button(window, command=lambda: on_click('+'), text='+' , width=2)
b14 = tk.Button(window, command=lambda: on_click('.'), text='.' , width=2)
b15 = tk.Button(window, command=lambda: on_click('%'), text='%' , width=2)
b16 = tk.Button(window, command=lambda: on_click('='), text='=' , width=2)


b1.grid(row=1, column=0, padx=10, pady=5, sticky='w')
b2.grid(row=1, column=1, padx=10, pady=5, sticky='w')
b3.grid(row=1, column=2, padx=10, pady=5, sticky='w')
b13.grid(row=1, column=3, padx=10, pady=5, sticky='w')
b5.grid(row=2, column=0, padx=10, pady=5, sticky='n')
b6.grid(row=2, column=1, padx=10, pady=5, sticky='n')
b7.grid(row=2, column=2, padx=10, pady=5, sticky='n')
b12.grid(row=2, column=3, padx=10, pady=5, sticky='n')
b8.grid(row=3, column=0, padx=10, pady=5, sticky='n')
b9.grid(row=3, column=1, padx=10, pady=5, sticky='n')
b0.grid(row=3, column=2, padx=10, pady=5, sticky='n')
b11.grid(row=3, column=3, padx=10, pady=5, sticky='n')
b10.grid(row=4, column=0, padx=10, pady=5, sticky='n')
b14.grid(row=4, column=1, padx=10, pady=5, sticky='n')
b15.grid(row=4, column=2, padx=10, pady=5, sticky='n')
b16.grid(row=4, column=3, padx=10, pady=5, sticky='n')








window.mainloop()