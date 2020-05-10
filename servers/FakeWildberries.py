import socket
import json

class FakeServer:

    def __init__(self):

        self.socket = socket.socket()
        self.socket.bind(('194.67.78.210', 2048))
        self.socket.listen(1)
        self.connection = None
        self.address = None
        self.bufer_size = 0
        self.json_data = 0

    def main(self):

        try:
            while 1 == 1:
                    self.connection, self.address = self.socket.accept()

                    self.bufer_size = self.connection.recv(8).decode('utf-8')

                    data_recieve = self.connection.recv(int(self.bufer_size)).decode('utf-8')

                    data_recieve = data_recieve.split('!!')
                    request_data = data_recieve[0]
                    self.json_data = data_recieve[1]


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

        try:
            with open('main.json','r') as file:
                data = json.load(file)

            json_obj = kson.loads(self.json_data)

            data.append(json_obj)

            with open('main.json', 'w') as file:
                file.write(data)

            self.connection.send(b'Successful')
        except Exception as ex:
            print(ex)

              

    def get_items(self):
        pass

if __name__ == '__main__':
    a = FakeServer()
    a.main()