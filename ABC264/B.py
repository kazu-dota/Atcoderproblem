R, C = map(int, input().split())

def solve(c, r):
    if C % 2== 1:
        if abs(c - 7.5) == 4.5:
            if r in [2, 14]:
                print('white')
                exit()
            else:
                print('black')
                exit()
                
        if abs(c - 7.5) == 2.5:
            if r in [2,4,12, 14]:
                print('white')
                exit()
            else:
                print('black')
                exit()
        if abs(c - 7.5) == 1.5:
            if r in [2,4,6,10,12, 14]:
                print('white')
                exit()
            else:
                print('black')
                exit()

        if abs(c - 7.5) == 0.5:
            if r in [2,4,6,10,12, 14]:
                print('white')
                exit()
            else:
                print('black')
                exit()
        else:
            print('black')
            exit()

    else:
        if abs(c - 7.5) == 5.5:
            if r in [1, 15]:
                print('black')
                exit()
            else:
                print('white')
                exit()

        if abs(c - 7.5) == 3.5:
            if r in [1,3,13, 15]:
                print('black')
                exit()
            else:
                print('white')
                exit()


        if abs(c - 7.5) == 1.5:
            if r in [1,3,5,11,13,15]:
                print('black')
                exit()

            else:
                print('white')
                exit()

        if abs(c - 7.5) == 0.5:
            if r in [1,3,5,7,9,11,13,15]:
                print('black')
                exit()

            else:
                print('white')
                exit()
        else:
            print('white')
            exit()

solve(C,R)