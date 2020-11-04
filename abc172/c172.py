from itertools import accumulate

n, m, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_acc = [0] + list(accumulate(a))
b_acc = [0] + list((accumulate(b)))

ans = 0
bn = m

for an in range(n + 1):
    rem = k - a_acc[an]
    if rem < 0:
        break

    # rem >= 0 かつ、b_acc[0] = 0なので、bnはどんなに減っても0で必ず止まります。マイナスになってバグることはありません
    while b_acc[bn] > rem:
        bn -= 1
    ans = max(ans, an + bn)

print(ans)
