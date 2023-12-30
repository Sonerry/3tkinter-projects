##########                              ############
#                                                  #
# Aouthor: Soner Yıldırım , Date: 19.12.2023 16:59 #
#   python version 3.10                            #                                        
##########                              ############

import time
import tkinter as tk

def times():
    current_time = time.strftime("%H:%M:%S")
    clock.config(text=current_time)
    clock.after(200,times)
root = tk.Tk()
root.title(" Clock App / Py")

clock = tk.Label(root, font=("times",50,"bold"), bg="white")
clock.grid(row=2,column=2)
times()
digi = tk.Label(root, text="Now Time", font=("times",23,"bold"))
digi.grid(row=0,column=2)

nota = tk.Label(root, text="Hours Minute Second", font=("times",23,"bold"))
nota.grid(row=3,column=2)
root.mainloop()
