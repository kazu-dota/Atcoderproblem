N = input()
A = list(map(int, input().split()))

result = 0
while True:
    for a in A:
        if a % 2 == 1:
            print(result)
            exit()

        if a == 0:
            print(result)
            exit()

    A = list(map(lambda x: x//2, A))
    result += 1