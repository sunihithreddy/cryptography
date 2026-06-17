keyword = "CIPHER"
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

cipher = keyword
for ch in alphabet:
    if ch not in cipher:
        cipher += ch

print("Plain :", alphabet)
print("Cipher:", cipher)
