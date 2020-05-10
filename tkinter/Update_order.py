import socket

class Chacnhe_order_status:

    def __init__(self, request_data):
        self.request_data = request_data
        self.sock1 = socket.socket()
        self.sock1.connect(('194.67.78.210', 1024))
        self.buffer_size = 0

    def main(self):

        len_stroke = len(self.request_data)

        self.sock1.send(bytes(str(len_stroke), encoding='utf-8'))

        self.sock1.send(bytes(self.request_data, encoding='utf-8'))

    def run(self):
        try:
            self.main()
        except Exception as ex:
            print(ex)