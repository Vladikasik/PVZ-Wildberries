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

        self.frame_2nd = Frame(self.root)

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
        ###each clothes
        self.order_clothes = []

        numbers = self.order['Вещи']

        try:
            file = open(r'..\files\clothes.json', encoding='utf-8')
            file_read = file.read()
            file.close()
        except Exception as ex:
            print(ex)

        self.data_clothes = json.loads(file_read)

        for item in self.data_clothes:
            for number in numbers:
                if item == number:
                    self.order_clothes.append(self.data_clothes[item])
        ####

        ####info
        self.fio = self.order['ФИО']
        self.last_4 = self.order['Last_4']
        self.phone = self.order['Телефон']

        self.data_info = [self.fio,self.last_4,self.phone]
        self.data_info_text = ['ФИО','Последние 4','Телефон']
        ####
        self.frame_1ts.destroy()
        self.set_up_2()
        self.frame_2nd.pack()

    def set_up_2(self):

        text_lb = 'Заказ ' + str(self.order['Order_num'])
        Label(self.frame_2nd,text=text_lb,font='Calibri 14 bold').grid(row=0,column=1,columnspan=2,padx=1,pady=0.5)

        text_lb = 'Вещи'
        Label(self.frame_2nd, text=text_lb,font='Calibri 13').grid(row=1, column=0, columnspan=2, padx=1, pady=0.5)

        text_lb = 'Информация'
        Label(self.frame_2nd, text=text_lb,font='Calibri 13').grid(row=1, column=2, columnspan=2, padx=1, pady=0.5)

        j=0
        for i in self.order['Вещи']:
            Label(self.frame_2nd,text=str(i)).grid(row=2+j,column=0,padx=0.5,pady=0.5)
            j+=1

        j = 0
        for i in self.order_clothes:
            Label(self.frame_2nd, text=i).grid(row=2 + j, column=1, padx=1, pady=0.5)
            j += 1

        j = 0
        for i in self.data_info:
            Label(self.frame_2nd, text=i).grid(row=2 + j, column=3, padx=0.5, pady=0.5)
            j += 1

        j = 0
        for i in self.data_info_text:
            Label(self.frame_2nd, text=i).grid(row=2 + j, column=2, padx=100, pady=0.5)
            j += 1
        print(self.order_clothes)

    def replace(self,field1,field2):
        field1.destroy()
        field2.pack()

    def mainloop(self):

        self.root.mainloop()

