# -*- coding: utf-8 -*-
import socket
import select
import sys
import Queue

local_address = ("0.0.0.0", 8000)


def printTuplaConnection(client_socket, client_address, on_off):
	print "Tupla de conexão %s:%s<-->%s:%s %s." % (client_socket.getsockname() + client_address + ("online" if on_off else "offline", ))

def main():
	socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket_server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        socket_server.setblocking(0)
        socket_server.bind(local_address)
	socket_server.listen(5)
        # Sockets para fazer a leitura.
        inputs = [socket_server]
        # Sockets onde enviar dados.
        outputs = []
        # Messages dos sockets.
        message_queues = {}
	while inputs:
            readble, writeble, exeptional = select.select(inputs, outputs, inputs)
            
            for r in readble:
                if r is socket_server:
	            # Servidor está pronto para receber uma nova conexão.
                    client_socket, client_address = socket_server.accept()
                    printTuplaConnection(client_socket, client_address, 1)
                    client_socket.setblocking(0)
                    inputs.append(client_socket)
                    # Cria a fila para as mensagens que serão enviadas.
                    message_queues[client_socket] = Queue.Queue()
                    message_queues[client_socket].put("Sou um servidor de eco.")
                else:
                    data = r.recv(256)
                    if data:
                        message_queues[r].put(data)
                        if r not in outputs:
                            outputs.append(r)
                    else:
                        # Se a mensagem for vazia o cliente se desconectou.
                        if r in outputs:
                            outputs.remove(r)
                        inputs.remove(r)
                        r.close()
                        del message_queues[r]

            for w in writeble:
                print "Entrou no writeble"
                try:
                    message = message_queues[w].get_nowait()
                except Queue.Empty:
                    # Se não tiver mensagem para de tentar escrever.
                    outputs.remove(w)
                else:
                    w.send(message)

            # Remove o socket se tiver algum erro.
            for e in exeptional:
                inputs.remove(e)
                if e in outputs:
                    outputs.remove(e)
                e.close()
                del message_queues[e]

if __name__ == "__main__":
    main()
