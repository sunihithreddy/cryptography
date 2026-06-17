block_size=8
msg='HELLO'
pad=block_size-(len(msg)%block_size)
msg+=chr(128)+chr(0)*(pad-1)
print(msg.encode())
