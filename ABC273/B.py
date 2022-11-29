X, K = map(int, input().split())
from decimal import Decimal, ROUND_HALF_UP, ROUND_HALF_EVEN


for k in range(K):
    X = int(Decimal(X).quantize(Decimal(f'1E{k+1}'), rounding=ROUND_HALF_UP))

print(X)