import socket

sock = socket.socket()
sock.connect(("194.67.78.210", 1024))
sock.send(bytes('["GetOrderInfo", [{"OrderId": 0}]]', encoding="utf-8"))
