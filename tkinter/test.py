from tkinter import *
from tkinter import ttk


def show_hide_psd():
    if(check_var.get()):
        entry_psw.config(show="")
    else:
        entry_psw.config(show="*")

    print(entry_psw.get())


window = Tk()
window.wm_title("Password")

window.geometry("300x100+30+30")
window.resizable(0,0)

entry_psw = Entry(window, width=30, show="*", bd=3)
entry_psw.place(x = 5, y = 25)



check_var = IntVar()
check_show_psw = Checkbutton(window, text = "Show", variable = check_var, \
                 onvalue = 1, offvalue = 0, height=2, \
                 width = 5, command = show_hide_psd)
check_show_psw.place(x = 5, y = 50)

window.mainloop()