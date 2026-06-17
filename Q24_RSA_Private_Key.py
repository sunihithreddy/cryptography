def mod_inverse(e,phi):
 for d in range(1,phi):
  if (e*d)%phi==1:return d
e=31;n=3599;p=59;q=61
phi=(p-1)*(q-1)
print((mod_inverse(e,phi),n))
