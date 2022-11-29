S = [None for i in range(9)]
for i in range(9):
    S[i] = input()


H = 9
W = 9
def check(vect):
    dist = []
    for i in range(3):
        for j in range(i+1, 4):
            dx = vect[i][0] - vect[j][0] 
            dy = vect[i][1] - vect[j][1]
            dist.append(dx**2 + dy**2) 
    dist = sorted(dist)
    # print(dist[4] == dist[5])
    if dist[0] == dist[1] == dist[2] == dist[3]:
        a = dist[0] * 2
        if dist[4] == dist[5] == a:

            return True
        
    return False

point = []
for h in range(H):
    for w in range(W):
        if S[h][w] == '#':
            point.append([h,w])


import itertools
ans = 0
for v in itertools.combinations(point, 4):
    if check(v):
        ans += 1

print(ans)