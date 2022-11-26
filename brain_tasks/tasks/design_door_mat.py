n, m = input().split()
N, M = int(n), int(m)
x = 1
for i in range(N // 2):
    print(('.|.' * x).center(M, '-'))
    x += 2
print('WELCOME'.center(M, '-'))
for i in range(N // 2):
    print(('.|.' * (x -2)).center(M, '-'))
    x -= 2