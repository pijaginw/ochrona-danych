from Crypto.PublicKey import RSA
from keygen import keyGenerator
import sys, random
from szybkiepotegowaniemod import szybkiePotegowanieMod
from nwd import odwrotnoscMod

def textToNum(text, secretkey):
	t = []
	cnt = 0
	for c in text:
		if cnt == len(secretkey):
			cnt = 0
		t.append(ord(c)^secretkey[cnt])
		cnt += 1

	print 'text to numbers: ' + str(t)
	return t

def numToText(data, secretkey):
	t = []
	cnt = 0
	for c in data:
		if cnt == len(secretkey):
			cnt = 0
		t.append(chr(int(c)^secretkey[cnt]))
		cnt += 1

	print 'numbers to text: ' + str(t)
	return t

class MyRSA():

	keys = keyGenerator()
	print keys

	secretkey = []
	for i in range(3):
		secretkey.append(random.randint(1,255))

	e = keys[0]
	n = keys[1]
	d = keys[2]
	def encrypt(self, text, secretkey):
		result = []
		msg = textToNum(text, secretkey)

		for i in msg:
			result.append(pow(i, self.e)%self.n)

		print result
		return result

	def decrypt(self, msg, secretkey):
		result = []
		res = ''

		for i in msg:
			#result.append(pow(i, self.d)%self.n)
			result.append(szybkiePotegowanieMod(i, self.d, self.n))

		print 'decrypt: ' + str(result)
		result = numToText(result, secretkey)
		for r in result:
			res += r
		return res

if __name__ == '__main__':
	
	"""rsa_keys = RSA.generate(1024)
	pub_key = rsa_keys.publickey()

	encrypted = pub_key.encrypt("Top secret", "some randomness")

	print encrypted
	print rsa_keys.decrypt(encrypted)"""

	print '********************'
	msg = raw_input("Podaj tekst: ")
	rsa = MyRSA()
	enc = rsa.encrypt(str(msg), rsa.secretkey)
	print rsa.decrypt(enc, rsa.secretkey)