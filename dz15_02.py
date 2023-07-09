#server
import socket
import logging
from datetime import datetime

logging.basicConfig(level=logging.DEBUG,
                    filename='log_server.log',
                    format='server %(asctime)s - %(levelname)s - %(message)s')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('localhost', 55000))
sock.listen(5)
logging.info("Server started!")
conn, addr = sock.accept()
logging.debug(f"Connected {addr}")

while True:
    data = conn.recv(1024)
    print(data)
    logging.debug(f"Message received: {data}")
    if data.decode('utf-8') == "Hi!":
        logging.debug("Sending welcome message to the user")
        answer = "Welcome!"
    elif data.decode('utf-8').strip() == "":
        logging.warning("Input empty massage")
        answer = "You input empty message"
    elif data.decode('utf-8') == "Problem":
        logging.error("Sending error message to the user")
        answer = "Nothing to help"
    else:
        logging.debug(f"Sending a message to the user")
        answer = f"Your message was received at {datetime.now()}"
    conn.send(bytes(answer, encoding='UTF-8'))
conn.close()
