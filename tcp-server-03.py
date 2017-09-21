# -*- coding: utf-8 -*-
import socket
import threading

local_address = ("0.0.0.0", 8000)


def clientSocketController(client_socket, client_address):
	client_socket.send("Sou um servidor de eco.")
	while client_socket is not None:
		try:
			response = client_socket.recv(256).strip()
			#client_socket.send("Eco: %s!\n" % response)
		except:
			printTuplaConnection(client_socket, client_address, False)
			client_socket = None

def printTuplaConnection(client_socket, client_address, on_off):
	print "Tupla de conexão %s:%s<-->%s:%s %s." % (client_socket.getsockname() + client_address + ("online" if on_off else "offline", ))

def main():
	socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        socket_server.bind(local_address)
	socket_server.listen(5)
	print "Servidor online."
	while 1:
		client_socket, client_address = socket_server.accept()
		printTuplaConnection(client_socket, client_address, True)
		try:
			thread = threading.Thread(target = clientSocketController, args = (client_socket, client_address))
			thread.start()
		except Exception as ex:
			print ex

if __name__ == "__main__":
	main()
