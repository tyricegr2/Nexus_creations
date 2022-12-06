
import socket

HOST = 'www.google.com'
PORT = 443 # For HTTPS, if I want HTTP, then I use Port = 90

client_socket = socket.socket(socket.AF_INTET, socket.SOCK_STREAM)
server_address_google = (HOST, PORT)
client_socket.connect(server_address_google)

request_header_google = b'GET / HTTPS/1.0\r\nHost: www.google.com\r\n\r\n'
client_socket.sendall(request_header_google)

response = ''
while True:
    recv = client_socket.recv(1024)
