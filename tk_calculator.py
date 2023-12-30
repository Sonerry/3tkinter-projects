##########                              ############
#                                                  #
#  Author: Soner Yıldırım                          #
#  python version 3.10                             #               
##########                              ############
import tkinter as tk 
from tkinter import END
from tkinter import messagebox

root = tk.Tk()
root.title("Calculator")

entry = tk.Entry(root,width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = entry.get()
    entry.delete(0,END)
    entry.insert(0, str(current) + str(number))

def button_clear():
    entry.delete(0, END)

def button_add():
    first_num = entry.get()
    global f_num 
    global math
    math = "addition"
    f_num = int(first_num)
    entry.delete(0, END)

def button_equal():  
    try:
        second_num = entry.get()
        entry.delete(0, END)
        if math == "addition":
            entry.insert(0, f_num+int(second_num))
        elif math == "subtraction":
            entry.insert(0, f_num - int(second_num))
        elif math == "multiplication":
            entry.insert(0, f_num * int(second_num))
        elif math == "division":
             entry.insert(0, f"{f_num / int(second_num):.3f}")
    except ZeroDivisionError:
            messagebox.showinfo("result","A number cannot be divided by !!!zero!!! .Please enter positive")
def button_subtract():
    first_num = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_num)
    entry.delete(0, END)


def button_multiply():
    first_num = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_num)
    entry.delete(0, END)


def button_divide():
    first_num = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_num)
    entry.delete(0, END)

button1 = tk.Button(root, text="1", padx=38, pady=20, command=lambda: button_click(1))
button2 = tk.Button(root, text="2", padx=40, pady=20, command=lambda: button_click(2))
button3 = tk.Button(root, text="3", padx=42, pady=20, command=lambda: button_click(3))
button4 = tk.Button(root, text="4", padx=38, pady=20, command=lambda: button_click(4))
button5 = tk.Button(root, text="5", padx=40, pady=20, command=lambda: button_click(5))
button6 = tk.Button(root, text="6", padx=42, pady=20, command=lambda: button_click(6))
button7 = tk.Button(root, text="7", padx=38, pady=20, command=lambda: button_click(7))
button8 = tk.Button(root, text="8", padx=40, pady=20, command=lambda: button_click(8))
button9 = tk.Button(root, text="9", padx=42, pady=20, command=lambda: button_click(9))
button0 = tk.Button(root, text="0", padx=38, pady=20, command=lambda: button_click(0))
# Options
button_add = tk.Button(root, text="+", padx=37, pady=20, command=button_add)
button_equal = tk.Button(root, text="=", padx=89, pady=20, command=button_equal)
button_clear = tk.Button(root, text="Clear", padx=89, pady=20, command=button_clear)
button_subtract = tk.Button(root, text="-", padx=42, pady=20, command=button_subtract)
button_multiply = tk.Button(root, text="*", padx=38, pady=20, command=button_multiply)
button_divide = tk.Button(root, text="/", padx=38, pady=20, command=button_divide)

# numbers on the screen
button1.grid(row=3, column=0)
button2.grid(row=3, column=1)
button3.grid(row=3, column=2)

button4.grid(row=2, column=0)
button5.grid(row=2, column=1)
button6.grid(row=2, column=2)

button7.grid(row=1, column=0)
button8.grid(row=1, column=1)
button9.grid(row=1, column=2)

button0.grid(row=4, column=0)

button_add.grid(row=5, column=0)
button_equal.grid(row=5, column=1, columnspan=2)
button_clear.grid(row=4, column=1, columnspan=2)
button_subtract.grid(row=6, column=0)
button_multiply.grid(row=6, column=1)
button_divide.grid(row=6, column=2)

root.mainloop()