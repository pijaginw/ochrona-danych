import sys
import fcrypt
import string
import random

password = sys.argv[0]

salt = ''.join(random.sample(string.ascii_letters, 2))

protected_password = fcrypt.crypt(password, salt)
print protected_password