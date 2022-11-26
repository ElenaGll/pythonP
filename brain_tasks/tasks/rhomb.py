n, m = input().split()
N, M = int(n), int(m)
s = '10' * (N // 2)
x = 1
print(f"{s[0:(len(s))]}{'1'}{s[0:(len(s))]}")
for i in range(1, N - 1):
    print(f"{s[0:(len(s) - i)]}{'1'}{'0' * x}{'1'}{s[0:(len(s) - i)]}")
    x += 2
i = N - 1
while i > 0:
    print(f"{s[0:(len(s) - i)]}{'1'}{'0' * x}{'1'}{s[0:(len(s) - i)]}")
    i -= 1
    x -= 2
print(f"{s[0:(len(s))]}{'1'}{s[0:(len(s))]}")