import sys
import os
import platform
import subprocess

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


def Servers():

    for line in hostlines:
        line = line.strip( )
        if plat == "Windows":
            response = os.system("ping -n 1 " + line )
       
        if response == 0:
            print(line, 'is up!')
        else:
            print(line, 'is down!')
            

        
hostsFile.close()




if __name__ == "__main__":
        firewalls()
        Servers()
    
