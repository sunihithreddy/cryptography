from Crypto.Cipher import DES
key=b'12345678'
cipher=DES.new(key,DES.MODE_ECB)
print(cipher.encrypt(b'ABCDEFGH').hex())
