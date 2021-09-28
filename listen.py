#!/usr/bin/python3

import sys
import socket
import threading


def main():
	ip = '0.0.0.0'

	try:
		port = int(sys.argv[1])

	except:
		exit()

	if (port > 0 and port < 65536):

		server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		server.bind((ip,port))
		server.listen(5)

	else:
		exit()

	while True:
		try:
			client, address = server.accept()
			print(f'Accepted from {address[0]}:{address[1]}')
			client_handler = threading.Thread(target=handleC, args=(client,))
			client_handler.start()
		except:
			pass

def handleC(client_socket):
	with client_socket as sock:
		try:
			r= sock.recv(1024)
			print(f' Recived: {r.decode("utf-8")}')
			sock.send(b'ACK')
		except:
			pass

if __name__ == '__main__':
	main()
