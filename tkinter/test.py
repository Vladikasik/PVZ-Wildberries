import tkinter as tk
my_w = tk.Tk()
my_w.geometry("500x500")

def my_upd():
    print('Check box value :',c1_v1.get())

c1_v1=tk.BooleanVar()
c1 = tk.Checkbutton(my_w, text='PHP', variable=c1_v1,onvalue=True,offvalue=False,command=my_upd)
c1.grid(row=2,column=2)

my_w.mainloop()