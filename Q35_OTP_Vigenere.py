plaintext=input('Enter plaintext: ').upper()
key=[3,19,5,7,11,2,8,4,15,6]
cipher=''
for i,ch in enumerate(plaintext):
 if ch.isalpha():
  cipher+=chr(((ord(ch)-65+key[i%len(key)])%26)+65)
print(cipher)
