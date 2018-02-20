import socket
from Crypto.PublicKey import RSA

Server_Name= '127.0.0.1'
PORT = 8888
BUFFER_SIZE = 1024


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((Server_Name, PORT))


publicKey= open("key.pem","r").read()
public_key = RSA.importKey(publicKey)

privateKey = open("key.pem","r").read()
private_key = RSA.importKey(privateKey)

file = open('asn1.txt','r')
text= file.read()
print "Original data:",text

encrypt = public_key.encrypt(text, 32)

print "Encrypted Data: ",encrypt

s.send(encrypt[0])


s.close()


