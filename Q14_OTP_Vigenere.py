plaintext="SENDMOREMONEY"
key=[9,0,1,7,23,15,21,14,11,11,2,8,9]
cipher=""
for i in range(len(plaintext)):
 p=ord(plaintext[i])-65
 cipher+=chr(((p+key[i])%26)+65)
print(cipher)
