import socket
from Crypto.PublicKey import RSA  
   
Server_Name = '127.0.0.1'
PORT = 8888
BUFFER_SIZE = 1024 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((Server_Name, PORT))
s.listen(1)

publickey = open("key.pem","r").read()
public_key = RSA.importKey(publickey)

privateKey = open("key.pem","r").read()
private_key = RSA.importKey(privateKey)

conn, addr = s.accept()

data = conn.recv(BUFFER_SIZE)     

decrypted = private_key.decrypt(data)
print "Decrypted Data:",decrypted


conn.close()
