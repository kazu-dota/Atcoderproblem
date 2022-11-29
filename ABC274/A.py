A,B = map(int, input().split())
ans = B/A

ans = round(ans, 3)
s_ans = str(ans)

if len(str(ans)) < 5:
    for i in range(5-len(str(ans))):
        s_ans += '0'
print(s_ans)