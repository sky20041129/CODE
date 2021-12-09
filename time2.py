from datetime import datetime
import tkinter as tk
import os
import sys
import tkinter.font as tkFont


'''
This tool is for date and time calculator

'''
def time_cal():
  #  x = time1_entry.get()
  #  y = time2_entry.get()
    timex = datetime.strptime(time1_entry.get() ,"%Y-%m-%d %H:%M:%S")

    timey = datetime.strptime(time2_entry.get() ,"%Y-%m-%d %H:%M:%S")

    if timey < timex:
        gap = timex - timey

    else:
        gap = timey - timex

    timeresult_label.configure(text=timeresult_label.cget('text') + str(gap) + '\n' , wraplength=700,font=fontExample)


def get_path(filename):
    if hasattr(sys, "_MEIPASS"):
        return f'{os.path.join(sys._MEIPASS, filename)}'
    else:
        return f'{filename}'


def clear():
    timeresult_label.configure(text="")

window = tk.Tk()
window.title('NEC Taiwan Server R&D Center ')
window.geometry('1000x800')
window.iconbitmap(get_path("../NEC.ico"))

fontExample = tkFont.Font(family="Segoe UI", size=20)
fontExample3 = tkFont.Font(family="Segoe UI", size=15)
header_label = tk.Label(window, text='Time of day calculator',font=fontExample)
header_label.pack()


time1_frame = tk.Frame(window)
time1_frame.pack(side=tk.TOP)
time1_label = tk.Label(time1_frame, text='Time 1:',font=fontExample3,padx=5,pady=10)
time1_label.pack(side=tk.LEFT)
time1_entry = tk.Entry(time1_frame)
time1_entry.pack(side=tk.LEFT)

time2_frame = tk.Frame(window)
time2_frame.pack(side=tk.TOP)
time2_label = tk.Label(time2_frame, text='Time 2:',font=fontExample3,padx=5,pady=10)
time2_label.pack(side=tk.LEFT)
time2_entry = tk.Entry(time2_frame)
time2_entry.pack(side=tk.LEFT)

calculate_btn = tk.Button(window, text='Time calculator', command=time_cal,font=fontExample3,padx=5,pady=10)
calculate_btn.pack()

timeresult_label = tk.Label(window)
timeresult_label.pack(pady=100)


clear_label = tk.Label(window)
clear_label.pack()
clear_btn= tk.Button(window,text="Clear", command=clear,font=fontExample,padx=5,pady=10)
clear_btn.pack(side = 'bottom')
clear_btn.pack(pady = 50)

window.mainloop()
