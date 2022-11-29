Ax, Ay = map(int, input().split())
Bx, By = map(int, input().split())
Cx, Cy = map(int, input().split())
Dx, Dy = map(int, input().split())

def check_angle(Ax,Ay,Bx,By,Cx,Cy):
    S = (Ax*By+Bx*Cy+Cx*Ay-Ay*Bx-By*Cx-Cy*Ax)
    if S >= 0:
        return True
    else:
        return False

result = []

result.append(check_angle(Ax,Ay,Bx,By,Cx,Cy))
result.append(check_angle(Bx,By,Cx,Cy,Dx,Dy))
result.append(check_angle(Cx,Cy,Dx,Dy,Ax,Ay))
result.append(check_angle(Dx,Dy,Ax,Ay,Bx,By))

for r in result:
    if r == False:
        print('No')
        exit()
print('Yes')