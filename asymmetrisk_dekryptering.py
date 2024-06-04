import rsa
import base64
#from Crypto.PublicKey import rsa

targetFile = input('Hvilken fil vil du dekryptere?\n')

innhold = open(targetFile, "rb").read()
#privateKey = open("private_key.pem", "rb").read()

with open("private_key.pem", "rb") as key_file:
    privateKey = rsa.PrivateKey.load_pkcs1(key_file.read())

dekodet_kryptert_innhold = base64.b64decode(innhold)

message_cleartext = rsa.decrypt(dekodet_kryptert_innhold, privateKey)

with open("decrypted_file.txt", "wb") as file:
    file.write(message_cleartext)