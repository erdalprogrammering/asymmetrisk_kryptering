import rsa

publicKey, privateKey = rsa.newkeys(1024)

with open("public_key.pem", "wb") as key:
    key.write(publicKey.save_pkcs1("PEM")) # skriver public key inn i en 'pem' fil (Privacy-Enhanced Mail); sikkerhets drit

with open("private_key.pem", "wb") as key:
    key.write(privateKey.save_pkcs1("PEM"))