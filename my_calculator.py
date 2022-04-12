import tkinter
from tkinter import *
from tkmacosx import Button

global f_num
global math

root = Tk()

root.geometry('508x300')
root.title('My Calculator App')


input_field = Entry(root, width=50, borderwidth=5)
# input_field.insert(0, "0")
input_field.grid(row=0, column=0, columnspan=4, padx=10, pady=10)


def button_click(num):
    current_num = input_field.get()
    input_field.delete(0, END)
    input_field.insert(0, str(current_num) + str(num))


def clear_field():
    input_field.delete(0, END)


def add_nums():
    first_num = input_field.get()
    global f_num
    global math
    math = "add"
    f_num = int(first_num)
    input_field.delete(0, END)


def subtract_nums():
    first_num = input_field.get()
    global f_num
    global math
    math = "subtract"
    f_num = int(first_num)
    input_field.delete(0, END)


def multiply_nums():
    first_num = input_field.get()
    global f_num
    global math
    math = "multiply"
    f_num = int(first_num)
    input_field.delete(0, END)


def divide_nums():
    first_num = input_field.get()
    global f_num
    global math
    math = "divide"
    f_num = int(first_num)
    input_field.delete(0, END)


def percent():
    num = int(input_field.get())
    input_field.delete(0, END)
    input_field.insert(0, str(num/100))


def total():
    second_num = input_field.get()
    input_field.delete(0, END)

    if math == "add":
        input_field.insert(0, f_num + int(second_num))
    elif math == "subtract":
        input_field.insert(0, f_num - int(second_num))
    elif math == "multiply":
        input_field.insert(0, f_num * int(second_num))
    else:
        input_field.insert(0, f_num / int(second_num))


# defining the buttons

button_1 = Button(root, text="1", padx=20, pady=20, command=lambda: button_click(1), bg="#505050", fg="white")
button_2 = Button(root, text="2", padx=20, pady=20, command=lambda: button_click(2), bg="#505050", fg="white")
button_3 = Button(root, text="3", padx=20, pady=20, command=lambda: button_click(3), bg="#505050", fg="white")
button_4 = Button(root, text="4", padx=20, pady=20, command=lambda: button_click(4), bg="#505050", fg="white")
button_5 = Button(root, text="5", padx=20, pady=20, command=lambda: button_click(5), bg="#505050", fg="white")
button_6 = Button(root, text="6", padx=20, pady=20, command=lambda: button_click(6), bg="#505050", fg="white")
button_7 = Button(root, text="7", padx=20, pady=20, command=lambda: button_click(7), bg="#505050", fg="white")
button_8 = Button(root, text="8", padx=20, pady=20, command=lambda: button_click(8), bg="#505050", fg="white")
button_9 = Button(root, text="9", padx=20, pady=20, command=lambda: button_click(9), bg="#505050", fg="white")
button_0 = Button(root, text="0", padx=20, pady=20, command=lambda: button_click(0), bg="#505050", fg="white")
button_plus = Button(root, text="+", padx=20, pady=20, command=add_nums, bg="#FF9500", fg="white")
button_minus = Button(root, text="-", padx=20, pady=20, command=subtract_nums, bg="#FF9500", fg="white")
button_multiply = Button(root, text="x", padx=20, pady=20, command=multiply_nums, bg="#FF9500", fg="white")
button_divide = Button(root, text="÷", padx=20, pady=20, command=divide_nums, bg="#FF9500", fg="white")
# button_percent = Button(root, text="%", padx=20, pady=20, command=percent)
button_clear = Button(root, text="Clear", padx=20, pady=20, command=clear_field, bg="#D4D4D2")
button_total = Button(root, text="=", padx=20, pady=20, command=total, bg="#FF9500", fg="white")
# button_point = Button(root, text=".", padx=20, pady=20, command=lambda: button_click("."))


# mapping the buttons to the screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)


button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)


button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_plus.grid(row=4, column=1)
button_minus.grid(row=3, column=3)


button_multiply.grid(row=2, column=3)
button_divide.grid(row=1, column=3)
button_clear.grid(row=4, column=2)
# button_point.grid(row=4, column=1)


# button_percent.grid(row=4, column=2)
button_total.grid(row=4, column=3)

# input_field.pack()

if __name__ == '__main__':

    root.mainloop()
