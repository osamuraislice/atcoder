n = int(input())
a = []
b = []
for i in range(n):
    c = list(map(int, input().split()))
    a.append(c[0])
    b.append(c[1])

cnt = 0
for i in range(n):
    diff = (b[i] - a[i])
    diff1 = diff+1
    ck = int(diff * (diff+1)/2)
#    print()
#    print(diff1)
#    print(ck)

    cnt += a[i] * diff1 + ck

print(cnt)
