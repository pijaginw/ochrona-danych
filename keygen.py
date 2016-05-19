import sys, random
from testpierwszosci import testPierwszosci
from nwd import nwd, odwrotnoscMod

def keyGenerator(t= 5):

	print t
	### p i q
	p = random.randint(300, 1000)
	q = random.randint(300, 1000)
	if p%2 == 0:
		p += 1
	if q%2 == 0:
		q += 1
	while not testPierwszosci(p, t):
		p = random.randint(300, 1000)
		if p%2 == 0:
			p += 1

	while not testPierwszosci(q, t):
		q = random.randint(300, 1000)
		if q%2 == 0:
			q += 1

	print '--> p= %d, q= %d' % (p,q)

	### n
	n = p*q
	print '--> n= %d' % n

	### e
	e = random.randint(2, n-1)
	while nwd(e, (p-1)*(q-1)) != 1:
		e = random.randint(2, 1000)
	print '--> e= %d' % e

	### d
	x = 1
	y = 0
	d = odwrotnoscMod(e, (p-1)*(q-1))
	print '--> d= %d' % d

	return [e, n, d]

if __name__ == '__main__':

	k = raw_input("Opcjonalna liczba testow: ")

	if k:
		print keyGenerator(int(k))
	else:
		print keyGenerator()