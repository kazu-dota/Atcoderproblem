H ,W = map(int, input().split())
S = [None for i in range(H)]
T = [None for i in range(H)]

import numpy as np

for  i in range(H):
    S[i] = list(input())
for i in range(H):
    T[i] = list(input())


S = np.array(S)
S = np.where(S == '.', 1, 0)

T = np.array(T)
T = np.where(T == '.', 1, 0)


S_l = np.sum(S,axis=0)
T_l = np.sum(T,axis=0)

import collections
s_l = collections.Counter(S_l)
t_l = collections.Counter(T_l)


e = set(t_l.keys())

for key, value in s_l.items():
    if key not in e:
        print('No')
        exit()
    elif t_l[key] != value:
        print('No')
        exit()


S_l = np.sum(S,axis=1)
T_l = np.sum(T,axis=1)
if not np.all(S_l==T_l):
    print('No')
    exit()
print('Yes')