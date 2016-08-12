import socket
import random
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

host, port = '', 5000
queue = 5
s.bind((host, port))
s.listen(queue)

responses = ["That's interesting", "Cool!", "Oh really?", "Sounds good", "Okay"]

stay_open = True

while stay_open:
    client, address = s.accept()
    data = client.recv(4096)
    while data:
        data_text = data.decode('utf-8').lower().strip()
        if data_text == "hi" or data_text == "hello" or data_text == "howdy" or data_text == "hey" or data_text == "hola":
            res = "Hi there!"
            client.send(bytes(res, 'utf-8'))
            data = client.recv(4096)
        elif data_text == "bye" or data_text == "later" or data_text == "ttyl":
            res = "Goodbye!"
            client.send(bytes(res, 'utf-8'))
            client.close()
            stay_open = False
            break
        else:
            res = responses[random.randint(0, len(responses) - 1)]
            client.send(bytes(res, 'utf-8'))
            data = client.recv(4096)


