# for loop
import tkinter as tk
from tkinter import ttk
from time import sleep
win = tk.Tk()
win.title('LOOP')

labels = ['What is your name : ', 'What is your age ',
          'What is your gender : ', 'Country : ', 'State : ', 'City : ', 'address']


for i in range(len(labels)):
    cur_label = 'label' + str(i)  # label0, label1
    cur_label = ttk.Label(win, text=labels[i])
    cur_label.grid(row=i, column=0, sticky=tk.W)

    # cur_entrybox = 'entry' + i  # entryname # entryage
    # cur_entrybox = ttk.Entry(win, width=16, textvariable=user_info[i])
    # cur_entrybox.grid(column=1, row=counter)
    # counter += 1


# name_entry = ttk.Entry(win, width=16, textvariable=name_var)
# name_entry.grid(row=0, column=1)


win.mainloop()
