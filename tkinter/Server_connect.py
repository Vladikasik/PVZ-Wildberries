import socket


class Server:

    def __init__(self, request_data, request_type):
        self.request_data = request_data
        self.request_type = request_type
        self.sock1 = socket.socket()
        self.sock1.connect(('194.67.78.210', 1024))
        self.buffer_size = 0

    def main(self):

        if self.request_type == 'order':
            data_to_send = '["GetOrderInfo", {"OrderId": %s}]' % self.request_data
        elif self.request_type == 'UpdateReturn' or 'UpdateSubmission':
            request_data = self.request_data.split('!!')

            data_to_send = '["%s", {"OrderId": %s, "OrderItems": %s}]' % (self.request_type, request_data[1], request_data[0])
            data_to_send = data_to_send.replace("'",'"')
        print(data_to_send)
        len_stroke = len(data_to_send)

        self.sock1.send(bytes(str(len_stroke), encoding='utf-8'))

        self.sock1.send(bytes(data_to_send, encoding='utf-8'))

        dataToRecieve = self.sock1.recv(256)

        self.buffer_size = dataToRecieve.decode('utf-8')

        print(self.buffer_size)

        dataToRecieve = self.sock1.recv(int(self.buffer_size)+100)

        result = dataToRecieve.decode('utf-8')
        return result

    def run(self):

        try:
            return self.main()
        except Exception as ex:
            print(ex)
