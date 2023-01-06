import socket
import requests
import time



HOST = '192.168.0.100'    # The remote host
PORT = 8081             # The same port as used by the server




with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    s.sendall(b"{\"message\" : \"id\",\"params\":[\"-1\"]}")
    data = s.recv(1024)


print(f"Received {data!r}")

s.send(b"{\"message\": \"event\",\"params\": [ \"DOOR_OPEN_SUCCESS\", \"Miikka opened the door\"]}")
