# -*- coding: utf-8 -*-
import socket

server_address = ("192.168.47.255", 8000)

def main():
	socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
	socket_server.sendto("Claudio Scheer", server_address)

if __name__ == "__main__":
	main()
