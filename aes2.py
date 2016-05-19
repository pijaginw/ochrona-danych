from Crypto.Cipher import AES
from pbkdf2 import PBKDF2
import sys
import os

class AESCipher():
	key = ''
	iv = ''
	def AESEncryption(self, k, plaintext, mode):
		salt = os.urandom(8)
		self.iv = os.urandom(16)
		self.key = PBKDF2(k, salt).read(32)
		if mode == 'CBC':
			aes = AES.new(self.key, AES.MODE_CBC, self.iv)
		elif mode == 'ECB':
			aes = AES.new(self.key, AES.MODE_ECB, self.iv)
		encrypted = aes.encrypt(plaintext)
		return encrypted

	def AESDecryption(self, encrypted):
		aes = AES.new(self.key, AES.MODE_CBC, self.iv)
		decrypted = aes.decrypt(encrypted)
		return decrypted

	def entropy(data):

		histogram = {}
		for i in data:
			if i in histogram:
				histogram[i] += 1
			else:
				histogram[i] = 1

		for i in histogram:
			histogram[i] = histogram[i] / float(len(data))

		H = 0
		for i in histogram:
			H += histogram[i] * log(histogram[i], 2)
		H = -H
		return H


if __name__ == '__main__':

	if len(sys.argv) > 2:
		if len(sys.argv[2])%16 != 0:
			print 'Plaintext must be a multiple of 16 in length.'
		else:
			key = sys.argv[1]
			plaintext = sys.argv[2]
			if len(sys.argv) == 4:
				ac = AESCipher()
				mode = sys.argv[3]
				encrypted = ac.AESEncryption(key, plaintext, mode)
				decrypted = ac.AESDecryption(encrypted)
				print 'Mode: %s\nPlaintext: "%s"\nEncrypted: "%s"\nDecrypted: "%s"' \
					% (mode, plaintext, encrypted, decrypted)
			elif len(sys.argv) == 5:
				ac1 = AESCipher()
				ac2 = AESCipher()
				m1 = sys.argv[3]
				m2 = sys.argv[4]
				en1 = ac1.AESEncryption(key, plaintext, m1)
				en2 = ac2.AESEncryption(key, plaintext, m2)
				print 'Porownanie wynikow w trybach CBC i ECB:\nECB: "%s"\nCBC: "%s"\n' \
					% (en1, en2)
				
