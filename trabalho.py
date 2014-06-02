#!/usr/bin/python
# -*- coding: utf-8 -*-


def main(argc, argv):
    
	profundidade = int(argv[1])
	url = argv[2]
	
	print 'Url: ' + url
	print 'Profundidade: ' + str(profundidade)
	
	
main(len(sys.argv), sys.argv)
