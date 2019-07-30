import smtplib
from getpass import getpass
from simplecrypt import encrypt, decrypt
from base64 import b64encode, b64decode
from email.mime.text import MIMEText

def sendEmail(filename,to,subject,body):
	gmail_user = 'schreiber.felipe@gmail.com'
	to = ", ".join(to)
	encoded_cipher = bytearray()
	with open(filename, 'rb') as f:
		encoded_cipher = bytearray(f.read())
		f.close()
	cipher = b64decode(encoded_cipher)
	password = getpass()
	gmail_password = str(decrypt(password, cipher))
	gmail_password = gmail_password[2:-1]
	msg = MIMEText(body)
	msg['Subject'] = subject
	msg['From'] = gmail_user
	msg['To'] = to
	#print(msg.as_string())
	server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
	server.ehlo()
	server.login(gmail_user, gmail_password)
	server.sendmail(gmail_user,to,msg.as_string())
	server.quit()
