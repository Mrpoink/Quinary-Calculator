import tkinter as tk
from tkinter import messagebox
from src.quinaryCalculator import quinaryAddition, quinarySubtraction, quinaryMultiplication, quinaryDivision, quinarySquare, quinarySquareRoot, convertQuinaryToDecimal, convertDecimalToQuinary

window = tk.Tk()
window.title("Quinary Calculator")
window.geometry("300x400")
window.resizable(False, False)

current_input = "0"
first_operand = ""
operator = ""
is_decimal_mode = False

display = tk.Label(window, text="0", font=("Arial", 24), bg="lightgray", anchor="e", padx=10)
display.grid(row=0, column=0, columnspan=5, sticky="ew")


def on_number_click(number):
    global current_input
    try:
        if current_input == "0" or current_input == "Error":
            current_input = str(number)
        else:
            current_input += str(number)
    except TypeError:
        messagebox.showinfo(title="TypeError", message="Please press Clear (C) before continuing. \nTry entering your inputs in a different order.")

    update_display(current_input)

def on_operator_click(op):
    global first_operand, operator, current_input
    first_operand = current_input
    operator = op
    current_input = ""

def on_equals_click():
    global first_operand, operator, current_input
    if first_operand and operator and current_input:
        second_operand = current_input
        result = ""
        if operator == '+': result = quinaryAddition(first_operand, second_operand)
        elif operator == '-': result = quinarySubtraction(first_operand, second_operand)
        elif operator == '*': result = quinaryMultiplication(first_operand, second_operand)
        elif operator == '/': result = quinaryDivision(first_operand, second_operand)
        
        update_display(result)
        current_input = result
        first_operand = ""
        operator = ""

def on_unary_operator_click(op):
    global current_input
    if op == 'sqrt': result = quinarySquareRoot(current_input)
    elif op == 'sq': result = quinarySquare(current_input)
    elif op == 'C': result = "0"
    else: return
        
    current_input = result
    update_display(current_input)

def on_toggle_click():
    global is_decimal_mode
    is_decimal_mode = not is_decimal_mode
    update_display(current_input)
    
def update_display(value):
    global is_decimal_mode
    # Handle the case where the value is an error string
    if value == "Error":
        display.config(text=value)
    elif is_decimal_mode:
        display.config(text=str(convertQuinaryToDecimal(value)))
    else:
        display.config(text=value)

# --- Buttons ---
button_0 = tk.Button(window, text="0", command=lambda: on_number_click(0))
button_1 = tk.Button(window, text="1", command=lambda: on_number_click(1))
button_2 = tk.Button(window, text="2", command=lambda: on_number_click(2))
button_3 = tk.Button(window, text="3", command=lambda: on_number_click(3))
button_4 = tk.Button(window, text="4", command=lambda: on_number_click(4))

button_plus = tk.Button(window, text="+", command=lambda: on_operator_click('+'))
button_minus = tk.Button(window, text="-", command=lambda: on_operator_click('-'))
button_multiply = tk.Button(window, text="*", command=lambda: on_operator_click('*'))
button_divide = tk.Button(window, text="/", command=lambda: on_operator_click('/'))
button_equals = tk.Button(window, text="=", command=on_equals_click)
button_clear = tk.Button(window, text="C", command=lambda: on_unary_operator_click('C'))
button_square = tk.Button(window, text="x²", command=lambda: on_unary_operator_click('sq'))
button_sqrt = tk.Button(window, text="√", command=lambda: on_unary_operator_click('sqrt'))
button_toggle = tk.Button(window, text="Toggle", command=on_toggle_click)


button_4.grid(row=1, column=3, padx=5, pady=5)
button_3.grid(row=1, column=2, padx=5, pady=5)
button_2.grid(row=1, column=1, padx=5, pady=5)
button_1.grid(row=1, column=0, padx=5, pady=5)
button_0.grid(row=2, column=0, padx=5, pady=5)
button_plus.grid(row=1, column=4, padx=5, pady=5)
button_minus.grid(row=2, column=4, padx=5, pady=5)
button_multiply.grid(row=3, column=4, padx=5, pady=5)
button_divide.grid(row=4, column=4, padx=5, pady=5)
button_equals.grid(row=5, column=4, padx=5, pady=5)
button_clear.grid(row=2, column=1, padx=5, pady=5)
button_square.grid(row=2, column=2, padx=5, pady=5)
button_sqrt.grid(row=2, column=3, padx=5, pady=5)
button_toggle.grid(row=5, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()