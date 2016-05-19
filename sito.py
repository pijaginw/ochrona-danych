import sys

def sito(n):

	tab = []
	for i in range(n):
		tab.append(i)

	for i in range(2, n):
		if tab[i] != 0:
			for j in range(i+1, n):
				if tab[j] % tab[i] == 0:
					tab[j] = 0

	res = []
	for liczba in tab:
		if liczba != 1 and liczba != 0:
			res.append(liczba)

	return res

if __name__ == '__main__':
	
	if len(sys.argv) > 1:
		print "\nLiczby pierwsze z przedzialu od 0 do %s:\n" % sys.argv[1]
		print sito(int(sys.argv[1]))
	else:
		print "\nLiczby pierwsze z przedzialu od 0 do 100:\n"
		print sito(100)