N = int(input())
H = list(map(int,input().split()))

ans = -1 
tmp = -1 

for idx, h in enumerate(H):
    if h > tmp:
        tmp = h
        ans = idx + 1

print(ans)