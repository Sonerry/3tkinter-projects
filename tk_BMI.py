##########                              ############
#                                                  #
#  Author: Soner Yıldırım                          #
#  python version 3.10                             #               
##########                              ############

import tkinter as tk
from tkinter import messagebox
from tkinter import W


def get_weight():
    weight = int(entry.get())
    return weight

def get_height():
    height = int(entry2.get())
    return height

def calculate_bmi():
    try:
        height = get_height()
        weight = get_weight()
        height = height / 100.0
        bmi = int(weight / (height ** 2))
    except ZeroDivisionError:
        messagebox.showinfo("result","Please enter positive height.")
    except ValueError:
        messagebox.showinfo("result","Please enter valid data.")
    else:
        if bmi <= 15.0:
            result = "Your BMI is" + str(bmi) +  "\n Remarks: Very severely underweight!!"    
        elif 15.0 < bmi <= 16.0:
            result = "Your BMI is " + str(bmi) + "\n Remarks: Severely underweight!"
            messagebox.showinfo("result", result)
        elif 16.0 < bmi < 18.5:
            result = "Your BMI is " + str(bmi) + "\n Remarks: Underweight!"
            messagebox.showinfo("result", result)
        elif 18.5 <= bmi <= 25.0:
            result = "Your BMI is " + str(bmi) + "\n Remarks: Normal."
            messagebox.showinfo("result", result)
        elif 25.0 < bmi <= 30:
            result = "Your BMI is " + str(bmi) + "\n Remarks: Overweight."
            messagebox.showinfo("result", result)
        elif 30.0 < bmi <= 35.0:
            result = "Your BMI is " + str(bmi) + "\n Remarks: Moderately obese!"
            messagebox.showinfo("result", result)
        elif 35.0 < bmi <= 40.0:
            result = "Your BMI is " + str(bmi) + "\n Remarks: Severely obese!"
            messagebox.showinfo("result", result)
        else:
            result = "Your BMI is " + str(bmi) + "\n Remarks: Super obese!!"
            messagebox.showinfo("result", result)

root = tk.Tk()
root.bind("<Return>", calculate_bmi)
root.geometry("500x400")
root.configure(background="#307678")
root.title("BMI Calculator")
root.resizable(width=False, height=False)
LABLE = tk.Label(root, bg="#307678", text="Welcome to BMI Calculator", font=("times",15,"bold"), pady=10)
LABLE.place(x=55, y=0)
label = tk.Label(root, bg="#cef0f1", text="Enter Weight (in kg):", bd=6,
               font=("times",15,"bold"), pady=5)
label.place(x=55, y=60)
entry = tk.Entry(root, bd=8, width=6, font="Roboto 11")
entry.place(x=250, y=60)
label2 = tk.Label(root, bg="#cef0f1", text="Enter Height (in cm):", bd=6,
               font=("times",15,"bold"), pady=5)
label2.place(x=55, y=120)
entry2 = tk.Entry(root, bd=8, width=6, font="Roboto 11")
entry2.place(x=250, y=120)
button = tk.Button(bg="#2187e7", bd=12, text="BMI", padx=33, pady=15, command=calculate_bmi,
                font=("Helvetica", 20, "bold"))
button.grid(row=3, column=0, sticky=W)
button.place(x=115, y=250)
root.mainloop()