N, P, Q, R = map(int, input().split())
A = list(map(int, input().split()))

partial_sum = [0 for i in range(N+1)]


for i in range(1, N+1):
    partial_sum[i] = partial_sum[i-1] + A[i-1]

def binary_search(sorted_list, search_value):

    left_index: int = 0
    right_index: int = len(sorted_list) - 1
    while left_index <= right_index:
        middle_index: int = (left_index + right_index) // 2
        middle_value: int = sorted_list[middle_index]

        if search_value > middle_value:
            left_index = middle_index + 1
            continue
        
        if search_value < middle_value:
            right_index = middle_index - 1
            continue

        return True
    
    return False
ans = False
for x in range(N+1):
    if binary_search(partial_sum, partial_sum[x] + P):
            if binary_search(partial_sum, partial_sum[x] + Q + P) :
                    if binary_search(partial_sum, partial_sum[x]+ R + P + Q):
                        ans = True

if ans:
    print('Yes')
else:
    print('No')
 
