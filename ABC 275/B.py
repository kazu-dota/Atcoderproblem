A,B,C,D,E,F = map(int,input().split())

ABC = A * B * C
DEF = D * E * F

ans = (ABC-DEF) % 998244353

print(ans)