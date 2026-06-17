from Crypto.Cipher import DES3
from Crypto.Random import get_random_bytes
key=DES3.adjust_key_parity(get_random_bytes(24))
iv=get_random_bytes(8)
cipher=DES3.new(key,DES3.MODE_CBC,iv)
print("CBC 3DES Ready")
