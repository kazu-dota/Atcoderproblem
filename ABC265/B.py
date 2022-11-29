N,M,T=map(int,input().split())
A=[0]+list(map(int,input().split()))
bonus=[0]*(N+1)
for _ in range(M):
  x,y=map(int,input().split())
  bonus[x]=y
 
# i -> i+1
for i in range(1,N):
  if T<=A[i]:
    print("No")
    exit()
  T-=A[i]
  T+=bonus[i+1]
 
print("Yes")