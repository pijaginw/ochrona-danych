# -*- coding: utf-8 -*-
import sys
from Crypto.Hash import MD5

def md5sum(fileName):
	f = open(fileName, 'r')
	if f is None:
		print 'Błędny plik'
		return

	h = MD5.new()
	h.update(f.read())
	fileSum = h.hexdigest()

	fname = fileName[:-4] + '.md5'
	f = open(fname, 'w')
	f.write(fileSum)
	f.close()

	print '\nSuma kontrolna pliku "%s": %s' % (fileName, fileSum)
	return fileSum

def md5sumCheck(fileName):
	fname = fileName[:-4] + '.md5'
	f = open(fname, 'r')
	fileSumFromFile = f.read()

	fileSum = md5sum(fileName)

	if fileSumFromFile == fileSum:
		print u'Suma kontrolna nie uległa zmianie.'
	else:
		print u'Plik został zmieniony.'

if __name__ == '__main__':
	
	if len(sys.argv) == 2:
		md5sum(sys.argv[1])
	elif len(sys.argv) == 3 and sys.argv[1] == '-c':
		md5sumCheck(sys.argv[2])