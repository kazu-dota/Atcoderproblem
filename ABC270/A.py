X, Y, Z = map(int, input().split())
 
#壁がない
if X < 0:
    if X >= Y or Y > 0:
        print(abs(X))
        exit()
 
    else:
        if Z < 0:
            if Z < Y:
                print(-1)
                exit()
 
            else:
                print(abs(X))
                exit()
 
        else:
            print(abs(2*Z) + abs(X))
            exit()
 
elif X > 0:
    if X <= Y or Y <0:
        print(X)
        exit()
    else:
        if Z > 0:
            if Z > Y:
                print(-1)
                exit()
 
            else:
                print(X)
                exit()
        
        else:
            print(abs(2*Z) + X)
            exit()
 
 