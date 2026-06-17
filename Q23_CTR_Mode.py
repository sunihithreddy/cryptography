counter=0
plaintext=[1,2,4]
cipher=[]
for p in plaintext:
 cipher.append(p^counter); counter+=1
print(cipher)
