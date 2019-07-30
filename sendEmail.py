import smtplib
from getpass import getpass
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode

def sendEmail(filename,to,subject,body):
	gmail_user = 'schreiber.felipe@gmail.com'
	encoded_cipher = bytearray()
	with open(filename, 'rb') as f:
		encoded_cipher = bytearray(f.read())
		f.close()
	cipher = b64decode(encoded_cipher)
	password = getpass()
	gmail_password = str(decrypt(password, cipher))
	gmail_password = gmail_password[2:-1]
	sent_from = gmail_user
	#to = ['schreiber.felipe@gmail.com','schreiber.bruna@gmail.com']
	#subject = 'OMG Super Important Message'
	#body = 'Hey, what\'s up?\n\n- You'

	email_text = """\
	From: %s
	To: %s
	Subject: %s

	%s
	""" % (sent_from, ", ".join(to), subject, body)

	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.login(gmail_user, gmail_password)
	server.sendmail(gmail_user,to,email_text)
	server.quit()
