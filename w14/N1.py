import socket                            # Подключаем
import threading
import sys
import gzip


sock = socket.socket()                   # Создаём
sock.connect(('81.200.31.248', 9000))    # Присоединяемся



def listener(sock):
	while sock.fileno() != -1:
		data = sock.recv(1024)
		if len(data) > 0:
			try:
				print(gzip.decompress(data).decode())
			except Exception:
				print(data.decode())


threads = [threading.Thread(target=listener, args=(sock,))]
for thread in threads:
	thread.start()

while True:
	mes = input()
	if mes == 'exit':
		break
	if mes == 'z':
		print('zipping: ', end='')
		mes = input()
		sock.send(gzip.compress(mes.encode()))
	else:
		sock.send(mes.encode())