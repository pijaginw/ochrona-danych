import sys

def nwd(a, b):

	while a!=0 and b!=0:
		if a > b:
			a = a % b
		else:
			b = b % a

	if a == 0:
		return b
	elif b == 0:
		return a
	else:
		return 1

x = 1
y = 0
def odwrotnoscMod(a, b):

	global x
	global y
	if b != 0:
		odwrotnoscMod(b, a%b)
		tmp = y
		y = x - (a/b)*y
		x = tmp
	return x

if __name__ == '__main__':

	"""print "NWD"
	a = raw_input("pierwsza liczba: ")
	b = raw_input("druga liczba: ")
	print nwd(int(a), int(b))"""

	print "Odwrotnosc modulo"
	c = raw_input("pierwsza liczba: ")
	d = raw_input("druga liczba: ")
	print odwrotnoscMod(int(c), int(d))