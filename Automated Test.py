import sys
import os
import platform
import subprocess
import socket
import time
import csv

ipup = False

plat = platform.system()
scriptDir = sys.path[0]

firewalls = os.path.join(scriptDir, 'firewalls.txt')
firewallsFile = open(firewalls, "r")
firelines = firewallsFile.readlines()

hosts = os.path.join(scriptDir, 'hosts.txt')
hostsFile = open(hosts, "r")
hostlines = hostsFile.readlines()

def firewalls():

	for line in firelines:
		line = line.strip( )
		if plat == "Windows":
			response = os.system("ping -n 1 " + line )

		if response == 0:
			print(line, 'is up!')
		else:
			print(line, 'is down!')



firewallsFile.close()


def servers():

    for line in hostlines:
        line = line.strip( )
        if plat == "Windows":
            response = os.system("ping -n 1 " + line )

        if response == 0:
            print(line, 'is up!')
        else:
            print(line, 'is down!')



hostsFile.close()

#--------------------------------------------------
# START PORT CHECK - NON-FUNCTIONAL
#--------------------------------------------------

retry = 3
delay = 10
timeout = 3



def ports():
	def isOpen(ip, port):
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(timeout)

			try:
					s.connect((ip, int(port)))
					s.shutdown(socket.SHUT_RDWR)
					return True
			except:
					return False
			finally:
					s.close()

	def checkHost(ip, port):
			ipup = False
			for i in range(retry):

					if isOpen(ip, port):
							ipup = True
							print (ip + " ", port + ' - UP')
							break
					else:
							if i < retry-1:
								time.sleep(delay)
							else:
								print (ip + " ", port + ' - DOWN') 
                            
                            
                        
			return ipup



	with open('Ports.txt') as csv_file:
		csv_reader = csv.reader(csv_file, delimiter=',')
		line_count = 0
		for row in csv_reader:
			ip = row[0]
			port = row[1]
			checkHost (ip, port)
			line_count += 1

#--------------------------------------------------
#END PORT CHECK
#--------------------------------------------------



if __name__ == "__main__":
        firewalls()
        servers()
        ports()
