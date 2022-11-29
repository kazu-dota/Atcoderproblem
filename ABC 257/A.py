import string
N ,X = map(int, input().split())

alphabet = list(string.ascii_lowercase)

strings = []
for i in alphabet:
    for n in range(N):
        strings.append(i)


print(strings[X-1].upper())