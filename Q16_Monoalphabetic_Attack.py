from collections import Counter
cipher=input("Enter ciphertext: ").upper()
freq_order="ETAOINSHRDLCUMWFGYPBVKJXQZ"
counts=Counter(ch for ch in cipher if ch.isalpha())
sorted_letters=[x[0] for x in counts.most_common()]
mapping={}
for i in range(min(len(sorted_letters),len(freq_order))):
 mapping[sorted_letters[i]]=freq_order[i]
print(''.join(mapping.get(c,c) for c in cipher))
