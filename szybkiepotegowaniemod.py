import sys

def szybkiePotegowanieMod(a, b, n):
	### a^b mod n

	# postac binarna
	bits = []
	for i in format(b if b >= 0 else (1 << 16) + b, '016b'):
		bits.append(int(i))

	bits.reverse()

	a = a % n
	res = 1
	x = a

	for i in range(len(bits)):
		if bits[i] == 1:
			res = (res * x) % n
		else:
			x = (pow(x, 2)) % n
		#print '(i= %d) x= %d, res= %d' % (i, x, res)

	return res

if __name__ == '__main__':
	if len(sys.argv) > 3:
		print 'result = %d\n' % szybkiePotegowanieMod(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
