S = input()

target = ['dream', 'dreamer', 'erase', 'eraser']

flag = True
while flag:
    sin = False
    for s in target:
      	if s == S:
          print('YES')
          exit()


    for s in target:
        if s == S[:5]:
            if S[5] in ['d', 'e']:
                S = S[5:]
                sin = True
                break

        elif s == S[:7]:
            if S[7] in ['d', 'e']:
                S = S[7:]
                sin = True
                break
            
    if sin == False:
        print('NO')
        flag = False

    if len(S) == 0:
        print('YES')
        flag = False

    if len(S) < 5:
        print('NO')
        flag = False