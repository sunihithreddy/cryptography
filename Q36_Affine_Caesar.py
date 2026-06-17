def encrypt(text,a,b):
 r=''
 for ch in text.upper():
  if ch.isalpha():
   r+=chr(((a*(ord(ch)-65)+b)%26)+65)
 return r
print(encrypt(input('Text: '),5,8))
