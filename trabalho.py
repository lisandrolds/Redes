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
		print "Impossible connect TCP or send HTTP request.."
		return
		
	html = ''
	stream = "Initial Value"
	while(len(stream) != 0):
		try:
			stream = conection.recv(1024)
			html = html + stream
		except:
			print "Connection closed! "
			break
	conection.close()
		
	lista = re.findall(r'a href=[\'"]?([^\'" >]+)', html)
	lista = retirandoURLsRepitidas(lista)
	
	
	for i in range(len(lista)):
		print lista[i] + ', profundidade: ' + str(profundidade)
		print 'Imagens dessa pagina: \n'
		
		img = re.findall(r'img src=[\'"]?([^\'" >]+)', html)
		img = retirandoURLsRepitidas(img)
	
		for imagem in img:
			print imagem
		
		if(profundidade - 1 > 0):
			search(lista[i], profundidade - 1)
	
	return	

def retirandoURLsRepitidas(lista):
	novaLista = []
	for url in lista :
		if not(url in novaLista) :
			novaLista.append(url)
	return novaLista	
		
def main(argc, argv):
    
	profundidade = int(argv[1])
	url = argv[2]
	
	print 'Url: ' + url
	print 'Profundidade: ' + str(profundidade)
	
	search(url, profundidade)
	
main(len(sys.argv), sys.argv)
