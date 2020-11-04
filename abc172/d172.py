'''
https://at274.hatenablog.com/entry/2020/06/28/193139
'''
N = int(input())

ans = 0
for x in range(1, N + 1):
    n = N // x
    ans += n * (2 * x + (n - 1) * x) // 2

print(ans)
