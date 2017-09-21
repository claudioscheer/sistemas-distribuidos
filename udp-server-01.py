# -*- coding: utf-8 -*-
import socket

local_address = ("0.0.0.0", 8000)


def main():
	socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	# socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEPORT, 1)
	socket_server.bind(local_address)
	while 1:
		data, remote_address = socket_server.recvfrom(256)
		print data

if __name__ == "__main__":
	main()
