import sys
N = int(input())
S = input()
sys.setrecursionlimit(10000000)
def solve(S):
    if len(S) == 0:
        print('No')
    if len(S) == 1:
        print('Yes')
        exit()
    if S[0] == 'B':
        print('Yes')
        exit()
    else:
        if S[-1] == 'B':
            print('No')
            exit()
        else:
            S = S[1:-1]
            solve(S)

solve(S)



