N, Y = map(int, input().split())

if 10000 * N < Y:
  print('-1 -1 -1')
  exit()
  
if 1000 * N > Y:
  print('-1 -1 -1')
  exit()

for i in range(N+1):
  for r in range(N-i+1):
    total = (10000*i) + (5000*r) + (1000*(N-i-r))
    if total == Y:
      print(f'{i} {r} {N-i-r}')
      exit()
      
print('-1 -1 -1')