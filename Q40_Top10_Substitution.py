cipher=input('Enter Ciphertext: ').upper()
for i in range(10):
 print(f'Guess {i+1}:', ''.join(chr((ord(c)-65-i)%26+65) if c.isalpha() else c for c in cipher))
