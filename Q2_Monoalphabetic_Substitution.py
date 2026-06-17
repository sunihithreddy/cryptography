plain = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cipher = "QWERTYUIOPASDFGHJKLZXCVBNM"

text = input("Enter Plaintext: ").upper()
result = ""

for ch in text:
    if ch.isalpha():
        result += cipher[plain.index(ch)]
    else:
        result += ch

print("Ciphertext:", result)
