key=[[9,4],[5,7]]
plaintext="MEET"
p=[ord(c)-65 for c in plaintext]
c1=(key[0][0]*p[0]+key[0][1]*p[1])%26
c2=(key[1][0]*p[0]+key[1][1]*p[1])%26
print(chr(c1+65)+chr(c2+65))
