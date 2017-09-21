# -*- coding: utf-8 -*-
import socket

server_address = ("192.168.42.131", 8000)

def main():
	socket_server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	socket_server.sendto("Claudio", server_address)

if __name__ == "__main__":
	main()
