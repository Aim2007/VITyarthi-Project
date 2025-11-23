import tkinter as tk

expression = ""

def add_to_display(value):
    global expression
    expression += str(value)
    display.delete(0, tk.END)
    display.insert(0, expression)

def clear_display():
    global expression
    expression = ""
    display.delete(0, tk.END)

def calculate():
    global expression
    # dividing by zero gives error, so we gotta handle it
    try:
        result = str(eval(expression))
        expression = result
        display.delete(0, tk.END)
        display.insert(0, result)
    except:
        expression = ""
        display.delete(0, tk.END)
        display.insert(0, "Error")

root = tk.Tk()
root.title("Calculator")

display = tk.Entry(root)
display.grid(row=0, column=0, columnspan=4)


# Row 1 (7, 8, 9, /)
btn_7 = tk.Button(root, text='7', width=5, height=2, command=lambda: add_to_display('7'))
btn_7.grid(row=1, column=0)

btn_8 = tk.Button(root, text='8', width=5, height=2, command=lambda: add_to_display('8'))
btn_8.grid(row=1, column=1)

btn_9 = tk.Button(root, text='9', width=5, height=2, command=lambda: add_to_display('9'))
btn_9.grid(row=1, column=2)

btn_div = tk.Button(root, text='/', width=5, height=2, command=lambda: add_to_display('/'))
btn_div.grid(row=1, column=3)

# Row 2 (4, 5, 6, *)
btn_4 = tk.Button(root, text='4', width=5, height=2, command=lambda: add_to_display('4'))
btn_4.grid(row=2, column=0)

btn_5 = tk.Button(root, text='5', width=5, height=2, command=lambda: add_to_display('5'))
btn_5.grid(row=2, column=1)

btn_6 = tk.Button(root, text='6', width=5, height=2, command=lambda: add_to_display('6'))
btn_6.grid(row=2, column=2)

btn_mul = tk.Button(root, text='*', width=5, height=2, command=lambda: add_to_display('*'))
btn_mul.grid(row=2, column=3)

# Row 3 (1, 2, 3, -)
btn_1 = tk.Button(root, text='1', width=5, height=2, command=lambda: add_to_display('1'))
btn_1.grid(row=3, column=0)

btn_2 = tk.Button(root, text='2', width=5, height=2, command=lambda: add_to_display('2'))
btn_2.grid(row=3, column=1)

btn_3 = tk.Button(root, text='3', width=5, height=2, command=lambda: add_to_display('3'))
btn_3.grid(row=3, column=2)

btn_sub = tk.Button(root, text='-', width=5, height=2, command=lambda: add_to_display('-'))
btn_sub.grid(row=3, column=3)

# Row 4 (C, 0, =, +)
btn_clr = tk.Button(root, text='C', width=5, height=2, command=clear_display)
btn_clr.grid(row=4, column=0)

btn_0 = tk.Button(root, text='0', width=5, height=2, command=lambda: add_to_display('0'))
btn_0.grid(row=4, column=1)

btn_eq = tk.Button(root, text='=', width=5, height=2, command=calculate)
btn_eq.grid(row=4, column=2)

btn_add = tk.Button(root, text='+', width=5, height=2, command=lambda: add_to_display('+'))
btn_add.grid(row=4, column=3)

root.mainloop()