# -*- coding: utf-8 -*-
import socket

local_address = ("0.0.0.0", 8000)


def main():
	socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
	socket_server.bind(local_address)
	socket_server.listen(1)
	while 1:
		client_socket, client_address = socket_server.accept()
		print "Tupla de conexão %s:%s<-->%s:%s." % (client_socket.getsockname() + client_address)
		client_socket.send("Type your name: ")
		name = client_socket.recv(256)
		client_socket.send("Tchau querido(a) " + name + "!\n")
		client_socket.close()

if __name__ == "__main__":
	main()
