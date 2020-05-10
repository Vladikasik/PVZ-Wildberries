import socket
import json

class FakeServer:

    def __init__(self):

        self.socket = socket.socket()
        self.socket.bind(('194.67.78.210', 7777))
        self.socket.listen(1)
        self.connection = None
        self.address = None
        self.bufer_size = 0

    def main(self):

        try:
            while 1 == 1:
                    self.connection, self.address = self.socket.accept()

                    request_data = self.connection.recv(8).decode('utf-8')

                    request_data = request_data.split('!!')

                    self.bufer_size = request_data[0]

                    if request_data[1] == 'orders':
                        self.get_data()
                    elif request_data[1] == 'items':
                        self.get_items()
                    elif request_data[1] == 'update':
                        self.update_data()

        except Exception as ex:
            print(ex)
        finally:
            self.socket.close()

    def get_orders(self):

        with open('main.json','r') as file:
            database_json = json.load(file)

        self.connection.send(bytes(str(len(database_json)), encoding='utf-8'))

        self.connection.send(bytes(database_json, encoding='utf-8'))
        

    def update_data(self):

        pass

    def get_items(self):

        pass


