block_size=8
text=input('Enter text: ')
padding=block_size-(len(text)%block_size)
if padding==block_size: padding=block_size
text+=chr(padding)*padding
print(text)
