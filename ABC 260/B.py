N, X, Y, Z = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ald = []
sum_list =[]
for a,b in zip(A, B):
  sum_list.append(a+b)
  
A_idx = [i[0] for i in sorted(enumerate(A), key=lambda x:x[1],reverse=True)]
B_idx = [i[0] for i in sorted(enumerate(B), key=lambda x:x[1],reverse=True)]
sum_idx = [i[0] for i in sorted(enumerate(sum_list), key=lambda x:x[1],reverse=True)]
 
 
if X != 0:
  for idx in A_idx[:X]:
    ald.append(idx)
    
n = 0  
if Y != 0:
  while Y:
    if B_idx[n] not in ald:
      ald.append(B_idx[n])
      Y -= 1
    n += 1
n = 0
if Z!=0:
  while Z:
    if sum_idx[n] not in ald:
      ald.append(sum_idx[n])
      Z -= 1
    n += 1
    
ald = sorted(ald)
for i in ald:
  print(i+1)