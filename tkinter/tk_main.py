from tkinter import *
from tkinter import ttk
import json

class Wildberries_App:

    def __init__(self):

        self.root = Tk()

        #some settings for window
        self.root.title('Wildberries')
        self.root.geometry('1000x750')
        #

        self.data_from_file = None
        self.order_number_from_field = ''
        self.order = {}

    def set_up_1(self):

        self.frame_1ts = Frame(self.root)

        self.order_number = Text(self.frame_1ts,height=1, width=50)

        self.order_number.grid(row=0,column=0)

        bttn_next = ttk.Button(self.frame_1ts,text='Далее',command=self.get_order)

        bttn_next.grid(row=0,column=1)

        self.frame_1ts.pack()

    def get_order(self):

        self.order_number_from_field = self.order_number.get('1.0', END)

        try:
            file = open(r'..\files\orders.json',encoding='utf-8')
            self.data_from_file = file.read()
            file.close()
        except Exception as ex:
            print('Error with opening file')
            print('---')
            print(ex)

        self.data_from_file = json.loads(self.data_from_file)

        for order in self.data_from_file:
            if order['Order_num'] == int(self.order_number_from_field):
                self.order = order

    def replace(self,field1,field2):

    def mainloop(self):

        self.root.mainloop()

