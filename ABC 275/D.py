N = int(input())
from functools import lru_cache

@lru_cache(maxsize=100000)
def func(N):
    if N == 0:
        return 1
    else:
        return func(N//2) + func(N//3)

ans = func(N)
print(ans)