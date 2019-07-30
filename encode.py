import sys
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
from getpass import getpass

password = getpass()
filename = sys.argv[1]
file = open(filename, 'r') 
message = file.readline() 
message = message.rstrip('\n')
file.close()
cipher = encrypt(password, message)
filename = filename[:-4]
encoded_cipher = b64encode(cipher)
with open(filename+'.bin', 'wb') as f:
		f.write(encoded_cipher)
		f.close()

