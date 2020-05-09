import tkinter as tk
from tkinter import ttk
import tk_main,py
root = tk.Tk()

root.title('Wildberries')
root.geometry('1000x750')

global frame1
frame1 = tk.Frame(root)

global zakaz_number
zakaz_number = tk.Text(frame1,height=2,width=100)

zakaz_number.grid(row=0,column=0)

def clear_all(frame1,frame2):
    frame1.destroy()


def get_zakaz():
    print(zakaz_number.get('1.0', '2.0'))
    clear_all(frame1,4)

next_bt = ttk.Button(frame1,text='Далее',command=get_zakaz)



next_bt.grid(row=0,column=1)

frame1.pack()

root.mainloop()