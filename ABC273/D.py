H, W , r_s, c_s = map(int,input().split())
N = int(input())
R = [None for i in range(N+1)]
C = [None for i in range(N+1)]

for i in range(N):
    R[i+1], C[i+1] = map(int, input().split())

Q = int(input())
D = [None for i in range(Q+1)]
L = [None for i in range(Q+1)]

for i in range(Q):
    A = input().split()
    D[i+1] = A[0]
    L[i+1] = int(A[1])
