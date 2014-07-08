#!/usr/bin/python
# -*- coding: utf-8 -*-

import socket
import re
import sys
import ssl

def divide(url):
	diretorio = url.split("/", 1)[-1]

	if diretorio == url:
		diretorio = "/"
	else:
		diretorio = "/" + diretorio 

	return diretorio

def search(url, profundidade):        
	
	url = url.split("http://")[-1]
	
	port = 80
	host = url.split("/")[0]
	diretorio = divide(url)
	conection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
	## adicionando ssl
	port = 443
	
	sslSocket = ssl.wrap_socket(conection, ca_certs = "ca-certificates.crt", cert_reqs = ssl.CERT_REQUIRED)
	
	try:
		sslSocket.connect((host, port))
	except:
		certificadoInvalido = True
	
	validacao = ''
	if certificadoInvalido :
		try:
			sslSocket = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM),
								ca_certs = "ca-certificates.crt")
			sslSocket.connect((host, port))
			validacao = 'Certificado nao confiavel'
		except:
			print "Erro de certificacao\n"
		
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
	
		print '\n'
		
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
