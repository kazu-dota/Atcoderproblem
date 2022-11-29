A, B = map(int, input().split())
score_A = []
score_B = []
 
if A == 7:
    print(7)
    exit()
elif A == 6:
    score_A.append(2)
    score_A.append(4)
elif A == 5:
    score_A.append(4)
    score_A.append(1)
elif A == 4:
    score_A.append(4)
elif A == 3:
    score_A.append(1)
    score_A.append(2)
elif A == 2:
    score_A.append(2)
elif A == 1:
    score_A.append(1)
else:
    score_A.append(0)
 
if B == 7:
    print(7)
    exit()
elif B == 6:
    score_B.append(2)
    score_B.append(4)
elif B == 5:
    score_B.append(4)
    score_B.append(1)
elif B == 4:
    score_B.append(4)
elif B == 3:
    score_B.append(1)
    score_B.append(2)
elif B == 2:
    score_B.append(2)
elif B == 1:
    score_B.append(1)
else:
    score_B.append(0)
 
score_A.extend(score_B)
 
print(sum(list(set(score_A))))