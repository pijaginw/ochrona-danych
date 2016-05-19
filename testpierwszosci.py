import sys
import random

def testPierwszosci(liczba, k=10):

	for i in range(k):
		a = random.randint(2, liczba-2)

		if (pow(a, liczba-1) % liczba) != 1:
			print 'liczba %d nie jest pierwsza\n' % liczba
			return False

	print 'liczba %d jest prawdopodobnie pierwsza\n' % liczba
	return True

if __name__ == '__main__':

	k = raw_input("Opcjonalna liczba testow: ")
	a = raw_input("Podaj liczbe: ")

	if k:
		print testPierwszosci(int(a), int(k))
	else:
		print testPierwszosci(int(a))
