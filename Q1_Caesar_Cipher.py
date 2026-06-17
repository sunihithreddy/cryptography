def encrypt(text, key):
    result = ""
    for ch in text:
        if ch.isalpha():
            shift = 65 if ch.isupper() else 97
            result += chr((ord(ch) - shift + key) % 26 + shift)
        else:
            result += ch
    return result

text = input("Enter Plaintext: ")
key = int(input("Enter Key (1-25): "))
print("Ciphertext:", encrypt(text, key))
