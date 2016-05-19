from Crypto.Cipher import AES
from pbkdf2 import PBKDF2
import sys
import os

def AESEncryption(key, data):
	salt = os.urandom(8)
	iv = os.urandom(16)
	key = PBKDF2(key, salt).read(32)
	aes = AES.new(key, AES.MODE_CBC, iv)
	encrypted = aes.encrypt(data)
	print encrypted

	### test - odszyfrowanie
	aes2 = AES.new(key, AES.MODE_CBC, iv)
	decrypted = aes2.decrypt(encrypted)
	print decrypted

	return encrypted

if __name__ == '__main__':
	if len(sys.argv) > 2:
		if (len(sys.argv[2]) % 16) != 0:
			print 'Plaintext must be a multiple of 16 in length.'
		else:
			key = sys.argv[1]
			plaintext = sys.argv[2]
			AESEncryption(key, plaintext)
