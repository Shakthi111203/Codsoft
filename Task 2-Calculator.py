from tkinter import *

def buttonclick(number):
    global operator
    operator += str(number)
    input_value.set(operator)

def buttonclear():
    global operator
    operator = ""
    input_value.set("")

def buttonEqual(event=None):
    global operator
    try:
        result = str(eval(operator))
        input_value.set(result)
        operator = result 
    except Exception:
        input_value.set("Error")
        operator = ""

main = Tk()
main.title("Calculator")

operator = ""
input_value = StringVar()
display_text = Entry(main, font=("arial", 20, "bold"), textvariable=input_value, bd=30, insertwidth=4, bg="powder blue", justify=RIGHT)
display_text.grid(columnspan=4)

main.bind('<Return>', buttonEqual)

def create_button(text, row, column, padx_value=16, command=None):
    button = Button(main, padx=padx_value, bd=8, fg="black", font=("arial", 20, "bold"), text=text, command=command)
    button.grid(row=row, column=column)
    return button

# Row 1
create_button('7', 1, 0, command=lambda: buttonclick(7))
create_button('8', 1, 1, command=lambda: buttonclick(8))
create_button('9', 1, 2, command=lambda: buttonclick(9))
create_button('+', 1, 3, command=lambda: buttonclick('+'), padx_value=12)

# Row 2
create_button('4', 2, 0, command=lambda: buttonclick(4))
create_button('5', 2, 1, command=lambda: buttonclick(5))
create_button('6', 2, 2, command=lambda: buttonclick(6))
create_button('-', 2, 3, command=lambda: buttonclick('-'), padx_value=16)

# Row 3
create_button('1', 3, 0, command=lambda: buttonclick(1))
create_button('2', 3, 1, command=lambda: buttonclick(2))
create_button('3', 3, 2, command=lambda: buttonclick(3))
create_button('*', 3, 3, command=lambda: buttonclick('*'), padx_value=15)

# Row 4
create_button('0', 4, 0, command=lambda: buttonclick(0))
create_button('.', 4, 1, command=lambda: buttonclick('.'), padx_value=20)
create_button('=', 4, 2, command=buttonEqual)
create_button('/', 4, 3, command=lambda: buttonclick('/'))

# Row 5
btn_clr = Button(main, padx=160, bd=8, fg="black", font=("arial", 20, "bold"), text="C", command=buttonclear)
btn_clr.grid(row=5, column=0, columnspan=4, padx=10, pady=10)

main.mainloop()