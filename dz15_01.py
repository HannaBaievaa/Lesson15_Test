#client
import socket
import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='log_server.log',
                    format='client %(asctime)s - %(levelname)s - %(message)s')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
logging.info("The client connects to the server")
sock.connect(('localhost', 55000))
logging.info('Client has joined')

while True:
    massage = input('Enter your message: ')
    while not massage:
        logging.warning("Input empty massage")
        massage = input('Enter your message: ')
    if massage == 'exit':
        break
    else:
        logging.info(f"Message sent: {massage}")
        sock.send(bytes(massage, encoding='UTF-8'))
        data = sock.recv(1024)
        print(data.decode('utf-8'))
sock.close()