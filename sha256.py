import sys
import hashlib
import os


def mac(fileName, fName1, fName2):

	f = open(fileName, 'w+')

	f1 = open(fName1, 'r')
	h1 = hashlib.sha256( f1.read() )
	print h1.hexdigest()
	f.write(h1.hexdigest())
	f.write(' ')
	f.write(os.path.abspath(os.path.dirname(fName1)))
	f.write('\n')

	f2 = open(fName2, 'r')
	h2 = hashlib.sha256( f2.read() )
	print h2.hexdigest()
	f.write(h2.hexdigest())
	f.write(' ')
	f.write(os.path.abspath(os.path.dirname(fName2)))
	f.write('\n')

	f1.close()
	f2.close()
	f.close()

if __name__ == '__main__':
	mac('pliki.txt', 'plik1.txt', 'plik2.txt')
	# do porownania wystarczy split linii po spacji