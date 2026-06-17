def encrypt(text, key):
    text = text.upper()
    key = key.upper()
    result = ""
    for i in range(len(text)):
        if text[i].isalpha():
            p = ord(text[i]) - 65
            k = ord(key[i % len(key)]) - 65
            result += chr((p + k) % 26 + 65)
    return result

text = input("Enter Plaintext: ")
key = input("Enter Key: ")
print("Ciphertext:", encrypt(text, key))
