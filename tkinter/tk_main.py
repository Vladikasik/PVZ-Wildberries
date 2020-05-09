from tkinter import *
from tkinter import ttk

class Wildberries_App:

    def __init__(self):

        self.root = Tk()

        #some settings for window
        self.root.title('Wildberries')
        self.root.geometry('1000x750')
        #

    def set_up_1(self):

        self.frame_1ts = Frame(self.root)

        self.order_number = Text(self.frame_1ts,height=1, width=50)

        self.order_number.grid(row=0,column=0)

        bttn_next = ttk.Button(self.frame_1ts,text='Далее',command=self.get_order)

        bttn_next.grid(row=0,column=1)

        self.frame_1ts.pack()

    def get_order(self):

        self.order_number = self.order_number.get('1.0', END)
        print(self.order_number)

    def mainloop(self):

        self.root.mainloop()

