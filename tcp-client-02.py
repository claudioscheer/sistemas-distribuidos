# -*- coding: utf-8 -*-
import socket

server_address = ("127.0.0.1", 8000)


def main():
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect(server_address)
	while 1:
		response = client_socket.recv(256)
		print response
		client_socket.send(raw_input().strip())

if __name__ == "__main__":
	main()
