from tkinter import *
from tkinter import ttk
import json
from tkinter import messagebox
from tkinter import BooleanVar
import Server_connect

class Wildberries_App:

    def __init__(self):

        self.root = Tk()

        # some settings for window
        self.root.title('Wildberries')
        self.root.geometry('1000x750')
        #

        self.data_from_file = None
        self.order_number_from_field = ''
        self.order = {}

        self.frame_1ts = Frame(self.root)

        self.frame_2nd = Frame(self.root)

        self.frame_3rd = Frame(self.root)

        self.choose_list = {}

        self.data_info = []

        self.data_info_text = []

        self.list_nums_items = []
        self.list_names_items = []

        #id of thing and its name
        self.num_item_dict = {}

        self.selected_minimal_1 = False

    def set_up_1(self):

        self.frame_1ts = Frame(self.root)

        self.order_number = Entry(self.frame_1ts)

        self.order_number.grid(row=0, column=0)

        bttn_next = ttk.Button(self.frame_1ts, text='Далее', command=self.get_order)

        bttn_next.grid(row=0, column=1)

        self.frame_1ts.pack()

    def get_order(self):

        self.order_number_from_field = self.order_number.get()

        # receive order
        # try:
        #     file = open(r'..\files\orders.json', encoding='utf-8')
        #     self.data_from_file = file.read()
        #     file.close()
        # except Exception as ex:
        #     print('Error with opening file')
        #     print('---')
        #     print(ex)
        #
        # self.data_from_file = json.loads(self.data_from_file)
        # try:
        #     for order in self.data_from_file:
        #         if order['Order_num'] == int(self.order_number_from_field):
        #             self.order = order
        # except ValueError:
        #     messagebox.showerror('Ошибка', 'Неправильный код заказа')

        sending = Server_connect.Server(self.order_number_from_field, 'order')
        receive = sending.run()
        if receive == 'ERROR 404: ORDER ID NOT FOUND.' or receive == 'CODE 501 : NOT IMPLEMENTED.':
            messagebox.showerror('Ошибка', receive)

        json_data = '"' + receive + '"'
        json_data = json_data.replace("'", '"')[1:-1]
        json_data = json_data.replace('F','f')
        self.order = json.loads(json_data)
        print(self.order)

        # each clothes (id into name)
        # self.order_clothes = []
        #
        # numbers = self.order['Вещи']
        #
        # try:
        #     file = open(r'..\files\clothes.json', encoding='utf-8')
        #     file_read = file.read()
        #     file.close()
        # except Exception as ex:
        #     print(ex)
        #
        # self.data_clothes = json.loads(file_read)
        #
        # for item in self.data_clothes:
        #     for number in numbers:
        #         if item == number:
        #             self.order_clothes.append(self.data_clothes[item])
        for i in self.order["OrderItemsInfo"].keys():
            self.list_nums_items.append(i)

        for i in self.order["OrderItemsInfo"].values():
            print(i)
            print(type(i))
            if i == 'ERROR 404: ITEM NOT fOUND.':
                self.list_names_items.append(i)
            else:
                self.list_names_items.append(i["ItemInfo"])
        ####

        ####info
        fio = self.order['ClientfullName']
        last_4 = self.order['OrderVerificationCode']
        phone = self.order['ClientPhone']

        self.data_info = [fio, last_4, phone]
        self.data_info_text = ['ФИО', 'Последние 4', 'Телефон']
        ####
        self.frame_1ts.destroy()
        self.set_up_2()
        self.frame_2nd.pack()

    def init_choose_list(self):
        for i in self.list_nums_items:
            self.choose_list[i] = BooleanVar()

    def set_up_2(self):

        text_lb = 'Заказ ' + str(self.order['OrderId'])
        Label(self.frame_2nd, text=text_lb, font='Calibri 14 bold').grid(row=0, column=2, columnspan=2, padx=1,
                                                                         pady=0.5)

        text_lb = '____________________'
        Label(self.frame_2nd, text=text_lb, font='Calibri 14 bold').grid(row=1, column=2, columnspan=2, padx=1,
                                                                         pady=0.5)

        text_lb = 'Вещи'
        Label(self.frame_2nd, text=text_lb, font='Calibri 13').grid(row=2, column=0, columnspan=2, padx=1, pady=0.5)

        text_lb = 'Информация'
        Label(self.frame_2nd, text=text_lb, font='Calibri 13').grid(row=2, column=3, columnspan=2, padx=1, pady=0.5)

        print(self.choose_list)

        self.init_choose_list()

        j = 0
        for i in self.list_nums_items:
            Checkbutton(self.frame_2nd, text=str(i), variable=self.choose_list[i], onvalue=True, offvalue=False).grid(
                row=3 + j, column=0, padx=0.5, pady=0.5)
            j += 1

        j = 0
        for i in self.list_names_items:
            Label(self.frame_2nd, text=i).grid(row=3 + j, column=1, padx=1, pady=0.5)
            j += 1

        j = 0
        for i in self.data_info_text:
            Label(self.frame_2nd, text='|').grid(row=3 + j, column=2, padx=10, pady=0.5)
            j += 1

        j = 0
        for i in self.data_info:
            if j == 0:
                Label(self.frame_2nd, text=i).grid(row=3 + j, column=4, columnspan=2, padx=0.5, pady=0.5)
            else:
                Label(self.frame_2nd, text=i).grid(row=3 + j, column=4, padx=0.5, pady=0.5)
            j += 1

        j = 0
        for i in self.data_info_text:
            Label(self.frame_2nd, text=i).grid(row=3 + j, column=3, padx=10, pady=0.5)
            j += 1


        bttn_give = Button(self.frame_2nd, text='Осуществить возврат', font='Calibri 13', command=self.button_give)
        bttn_get = Button(self.frame_2nd, text='Выдать заказ', font='Calibri 13', command=self.button_get)

        bttn_give.grid(row=j + 4, column=1, pady=50)
        bttn_get.grid(row=j + 4, column=4, pady=50)

    def check_chosen(self):
        is_true = False
        for item, variable in self.choose_list.items():
            if variable.get():
                is_true = True

        if is_true:
            self.selected_minimal_1 = True
            return True
        else:
            # messagebox.showerror('Ошибка', 'Вы не выбрали не одну вещь')
            self.selected_minimal_1 = False
            return False

    def button_give(self):
        if self.check_chosen():
            self.check_available('UpdateReturn')

    def button_get(self):
        if self.check_chosen():
            self.check_available('UpdateSubmission')

    def check_available(self, state_func):

        window = Toplevel()

        window.title('Пароль')
        window.geometry('200x77')

        text_pas = Label(window, text='Введит пароль работника')

        password = Entry(window, show='*')

        def confirm():
            result = password.get()
            with open(r'..\files\private\password_rabotnika') as file:
                correct = file.read()
            if result == correct:
                window.destroy()
                go_next(state_func)
            else:
                messagebox.showerror('Ошибка', 'Неправильный пароль')
                window.lift()

        bttn = Button(window, text='Подтвердить', command=confirm)

        text_pas.pack()
        password.pack()
        bttn.pack()

        def go_next(state_1):
            self.frame_2nd.destroy()
            self.set_up_3(state_1)
            self.frame_3rd.pack()

    def set_up_3(self, state):

        self.frame_3rd = Frame(self.root)

        text_lb = 'Заказ ' + str(self.order['OrderId'])
        Label(self.frame_3rd, text=text_lb, font='Calibri 14 bold').grid(row=0, column=2, columnspan=2, padx=1,
                                                                         pady=0.5)

        text_lb = '____________________'
        Label(self.frame_3rd, text=text_lb, font='Calibri 14 bold').grid(row=1, column=2, columnspan=2, padx=1,
                                                                         pady=0.5)

        if state == 'UpdateReturn':
            text_lb = 'Вещи на возврат'
        elif state == 'UpdateSubmission':
            text_lb = 'Вещи на сдачу'

        Label(self.frame_3rd, text=text_lb, font='Calibri 13').grid(row=2, column=0, columnspan=2, padx=1, pady=0.5)

        print(self.choose_list)

        Label(self.frame_3rd, text='ID товара').grid(row=2, column=2, columnspan=2, padx=0.5, pady=0.5)
        Label(self.frame_3rd, text='Наименование товара').grid(row=2, column=4, columnspan=2, padx=0.5, pady=0.5)

        j = 3
        for item, state_item in self.choose_list.items():
            if state_item.get():
                Label(self.frame_3rd, text=item).grid(row=j, column=2, columnspan=2, padx=0.5, pady=0.5)
                item_id = self.list_nums_items.index(item)
                Label(self.frame_3rd, text=self.list_names_items[item_id]).grid(row=j, column=4, columnspan=2, padx=0.5,
                                                                         pady=0.5)
                j += 1



        def return_to_main():
            self.frame_3rd.destroy()
            self.init_choose_list()
            self.frame_2nd = Frame(self.root)
            self.set_up_2()
            self.frame_2nd.pack()

        def accept(request_type):

            selected_list =[]

            for item, state in self.choose_list.items():
                if state.get():
                    selected_list.append(item)
            date_to_send = str(selected_list) + '!!' + str(self.order["OrderId"])
            connection = Server_connect.Server(date_to_send,request_type)

            answer = connection.run()


        Label(self.frame_3rd, text='', font='Calibri 13').grid(row=j + 1, column=0, columnspan=5, padx=1, pady=0.5)

        Button(self.frame_3rd, text='Вернутся на главную страницу', command=return_to_main).grid(row=j + 2, column=0,
                                                                                                 columnspan=2)
        Button(self.frame_3rd, text='Подтвердить', command=lambda: accept(state)).grid(row=j + 2, column=2,
                                                                                                 columnspan=2)

    def mainloop(self):

        self.root.mainloop()
