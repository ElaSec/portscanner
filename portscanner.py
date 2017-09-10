#Created By: Milad Khoshdel
#Special Thanks: Mikili
#Blog: https://blog.regux.com
#Email: miladkhoshdel@gmail.com
#Telegram: @miladkho5hdel

import socket
import subprocess
import ipaddress

def banner():
	print(' ')
	print('#######################################################################################')
	print('##                                                                                   ##')
	print('##                         __  __ ___ _      _   __  __ ___ _  __                    ##')
	print('##                        |  \/  |_ _| |    /_\ |  \/  |_ _| |/ /                    ##')
	print("##                        | |\/| || || |__ / _ \| |\/| || || ' <                     ##")
	print('##                        |_|  |_|___|____/_/ \_\_|  |_|___|_|\_\                    ##')
	print('##                                                                                   ##')
	print('##                                                    BY: Milad Khoshdel | Mikili    ##')
	print('##                                                    Blog: https://blog.regux.com   ##')
	print('##                                                                                   ##')
	print('#######################################################################################')
	print(' ')
	
banner()

try:

	ip = raw_input('Enter ip address > ')
	begin_port = input('Enter start port > ')
	end_port = input('Enter end port > ')

	for i in range(begin_port,end_port+1):

		sock = socket.socket()
		sock.settimeout(0.5)
		result = sock.connect_ex((str(ip),int(i)))
		
		if result == 0:
			print 'Port ' + str(i) + " is OPEN on " + str(ip)
			sock.close()
		else:
			print 'Port ' + str(i) + " is CLOSE on " + str(ip) 
			sock.close()
except KeyboardInterrupt:
	print "exit ..."
	exit()