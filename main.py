import tkinter as tk

root = tk.Tk()
root.title("Калькулятор")
root.minsize(200, 155)

expression = ""

text_input = tk.Entry(root, font=('Arial', 14), justify='right')
text_input.grid(row=0, column=0, columnspan=4, sticky="ew")


def button_click(item):
    global expression
    if item == '=':
        try:
            result = str(eval(expression))
            text_input.delete(0, tk.END)
            text_input.insert(0, result)
            expression = result
        except Exception:
            text_input.delete(0, tk.END)
            text_input.insert(0, "Ошибка")
            expression = ""
    elif item == 'C':
        expression = ""
        text_input.delete(0, tk.END)
    else:
        expression += str(item)
        text_input.delete(0, tk.END)
        text_input.insert(0, expression)

digits = [
    '7', '8', '9',
    '4', '5', '6',
    '1', '2', '3',
    '0'
]

row_val = 1
col_val = 0

for digit in digits:
    btn = tk.Button(root, text=digit, command=lambda x=digit: button_click(x))
    btn.grid(row=row_val, column=col_val, sticky="nsew")

    col_val += 1
    if col_val > 2:
        col_val = 0
        row_val += 1

operators = ['+', '-', '*', '/', '=']

row_val = 1
for op in operators:
    btn = tk.Button(root, text=op, command=lambda x=op: button_click(x))
    btn.grid(row=row_val, column=3, sticky="nsew")
    row_val += 1

btn_clear = tk.Button(root, text='C', command=lambda: button_click('C'))
btn_clear.grid(row=4, column=2, sticky="nsew")

root.mainloop()