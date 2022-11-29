S = input()
 
a = S[0]
b = S[1]
c = S[2]
 
 
if a == b == c:
  print(-1)
elif a==b:
  print(c)
elif b==c:
  print(a)
elif c==a:
  print(b)
else:
  print(a)
