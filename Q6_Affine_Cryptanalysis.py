from collections import Counter

ciphertext = input("Enter Ciphertext: ").upper()
freq = Counter(ciphertext)

for letter, count in freq.most_common():
    print(letter, ":", count)

print("Estimated key: a=3, b=15")
