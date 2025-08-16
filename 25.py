import tkinter as tk
import math
from tkinter import messagebox

window = tk.Tk()
window.geometry('600x400')

text = ''

def add_text(a):
    global text
    text = text + a
    l1.config(text=text)
def mosavi():
    global text
    print(eval(text))

l1 = tk.Label(window, text=text, padx=10, pady=10)
btn1 = tk.Grid(row=2, column=0, text='1', padx=10, pady=5, command=lambda: add_text('1'))
# btn2 = tk.Button(window, text='2', padx=10, pady=5, command=lambda: add_text('2'))
# btn3 = tk.Button(window, text='3', padx=10, pady=5, command=lambda: add_text('3'))
# btn4 = tk.Button(window, text='4', padx=10, pady=5, command=lambda: add_text('4'))
# btn5 = tk.Button(window, text='5', padx=10, pady=5, command=lambda: add_text('5'))
# btn6 = tk.Button(window, text='6', padx=10, pady=5, command=lambda: add_text('6'))
# btn7 = tk.Button(window, text='7', padx=10, pady=5, command=lambda: add_text('7'))
# btn8 = tk.Button(window, text='8', padx=10, pady=5, command=lambda: add_text('8'))
# btn9 = tk.Button(window, text='9', padx=10, pady=5, command=lambda: add_text('9'))
# btn0 = tk.Button(window, text='0', padx=10, pady=5, command=lambda: add_text('0'))
# btn13 = tk.Button(window, text='+', padx=10, pady=5, command=lambda: add_text('+'))
# btn12 = tk.Button(window, text='-', padx=10, pady=5, command=lambda: add_text('-'))
# btn10 = tk.Button(window, text='*', padx=10, pady=5, command=lambda: add_text('*'))
# btn11 = tk.Button(window, text='/', padx=10, pady=5, command=lambda: add_text('/'))
# btn14 = tk.Button(window, text='.', padx=10, pady=5, command=lambda: add_text('.0'))



btn = tk.Button(window, text='=', padx=10, pady=10, command=mosavi)

# btn1.grid(row=2, column=0, padx=10, pady=5, sticky='w')
# btn2.grid(row=2, column=1, padx=10, pady=5, sticky='w')
# btn3.grid(row=2, column=2, padx=10, pady=5, sticky='w')
# btn13.grid(row=2, column=3, padx=10, pady=5, sticky='w')
# btn4.grid(row=3, column=0, padx=10, pady=5, sticky='n')
# btn5.grid(row=3, column=1, padx=10, pady=5, sticky='n')
# btn6.grid(row=3, column=2, padx=10, pady=5, sticky='n')
# btn12.grid(row=3, column=3, padx=10, pady=5, sticky='n')
# btn7.grid(row=4, column=0, padx=10, pady=5, sticky='n')
# btn8.grid(row=4, column=1, padx=10, pady=5, sticky='n')
# btn9.grid(row=4, column=2, padx=10, pady=5, sticky='n')
# btn10.grid(row=4, column=3, padx=10, pady=5, sticky='n')
# btn11.grid(row=5, column=0, padx=10, pady=5, sticky='n')
# btn0.grid(row=5, column=1, padx=10, pady=5, sticky='n')
# btn14.grid(row=5, column=2, padx=10, pady=5, sticky='n')
# btn.grid(row=5, column=3, padx=10, pady=5, sticky='n')



l1.pack()
btn0.pack()
# btn1.pack()
btn2.pack()
btn3.pack()
btn4.pack()
btn5.pack()
btn6.pack()
btn7.pack()
btn8.pack()
btn9.pack()
btn10.pack()
btn11.pack()
btn12.pack()
btn13.pack()
btn14.pack()

window.mainloop()