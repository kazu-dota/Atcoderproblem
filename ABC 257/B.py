
N, K, Q = map(int,input().split())
A = list(map(int, input().split()))
L = list(map(int, input().split()))

result = [False] * N

for a in A:
    result[a-1] = True


for q in range(Q):
    flag = 0
    l = L[q]
    for i in range(N):
        if result[i]:
            flag += 1
            if i+1 < N:
                if flag == l and result[i+1] == False:
                    result[i] = False
                    result[i+1] = True

for idx,r in enumerate(result):
    if idx+1  == len(result) and r:
        print(str(idx+1), end='')

    elif r:
        print(str(idx+1) + ' ', end='')


                