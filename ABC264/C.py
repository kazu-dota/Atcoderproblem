H1, W1 = map(int,input().split())
A = [None for i in range(H1)]

for i in range(W1):
    A[i] = list(map(int, input().split()))

H2, W2 = map(int,input().split())
B = [None for i in range(H2)]

for i in range(W2):
    B[i] = list(map(int, input().split()))

for w in range(2 ** W1):
    for h in range(2 ** H1):
        for j in (W1):
            for r in (H1):
                