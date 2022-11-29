import sys
sys.setrecursionlimit(10**6)

H, W = map(int, input().split())
G = [None for i in range(H)]

for i in range(H):
    G[i] = list(input())

def rec(pos, G):
    string = G[pos[0]][pos[1]]
    G[pos[0]][pos[1]] = '-'
    if string == 'U':
        if pos[0] == 0:
            print(pos[0]+1, ' ',pos[1]+1)
            exit()

        pos[0] -= 1
        rec(pos, G)
    elif string == 'D':
        if pos[0] == H-1:
            print(pos[0]+1, ' ',pos[1]+1)
            exit()
        pos[0] += 1
        rec(pos, G)
    elif string == 'L':
        if pos[1] == 0:
            print(pos[0]+1, ' ',pos[1]+1)
            exit()
        pos[1] -= 1
        rec(pos, G)
    elif string == 'R':
        if pos[1] == W-1:
            print(pos[0]+1, ' ',pos[1]+1)  
            exit()
        pos[1] += 1
        rec(pos, G)
    else:
        print(-1)

rec([0,0], G)
