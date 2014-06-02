#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import re
import sys


def divide(url):
	diretorio = url.split("/", 1)[-1]

	if diretorio == url:
		diretorio = "/"
	else:
		diretorio = "/" + diretorio 

	return diretorio


def search(url, profundidade):        
	
	url = url.split("http://")[-1]
	
	porta = 80
	host = url.split("/")[0]
	diretorio = divide(url)
	conection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
	try:
		conection.connect((host, porta))
		conection.send("GET %s HTTP/1.1\r\nHost: %s\r\n\r\n" %(diretorio, host))
	except:
		print "Erro"
		return
		
	html = ''
	stream = ''
	while(len(stream) != 0):
		try:
			stream = conection.recv(1024)
			html = html + stream
		except:
			break
	conection.close()
	
	print html


def main(argc, argv):
    
	profundidade = int(argv[1])
	url = argv[2]
	
	print 'Url: ' + url
	print 'Profundidade: ' + str(profundidade)
	
	
main(len(sys.argv), sys.argv)
