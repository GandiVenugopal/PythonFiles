# Enter your code here. Read input from STDIN. Print output to STDOUT

N, M = map(int, input().split())

x = len('.|.')

for i in range(N // 2):
    m = int((M - x) / 2) - (i * 3)  # --------
    a = '-' * m
    print(a, end='')

    p = '.|.' * (2 * i + 1)  # .|.
    print(p, end='')
    print(a)

wel = '-' * int((M - 7) / 2)
print(wel + 'WELCOME' + wel)

for i in range((N // 2) - 1, 0 - 1, -1):
    m = int((M - x) / 2) - (i * 3)  # ---------
    a = '-' * m
    print(a, end='')
    p = '.|.' * (2 * i + 1)  # .|.
    print(p, end='')
    print(a)

