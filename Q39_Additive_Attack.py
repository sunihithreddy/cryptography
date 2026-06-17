cipher=input('Enter Ciphertext: ').upper()
for k in range(26):
 print(k,''.join(chr((ord(c)-65-k)%26+65) if c.isalpha() else c for c in cipher))
