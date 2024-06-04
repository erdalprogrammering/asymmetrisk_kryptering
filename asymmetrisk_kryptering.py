import rsa
import os
import base64

with open("public_key.pem", "rb") as key:
    publicKey = rsa.PublicKey.load_pkcs1(key.read())

with open("private_key.pem", "rb") as key:
    privateKey = rsa.PrivateKey.load_pkcs1(key.read())

targetFile = input('Hvilken fil vil du kryptere?\n')

with open(targetFile, "rb") as file:
    innhold = file.read()

kryptert_innhold = rsa.encrypt(innhold, publicKey)
base64_kryptert = base64.b64encode(kryptert_innhold)

targetFile_encoded = targetFile + "_encoded.enc"

with open(targetFile_encoded, "wb") as file:
    file.write(base64_kryptert)