iv=170
plaintext=[1,35]
cipher=[]; prev=iv
for p in plaintext:
 c=p^prev; cipher.append(c); prev=c
print(cipher)
