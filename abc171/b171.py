N, K = map(int, input().split())
p = list(map(int, input().split()))

p.sort()

sum = 0
for i in range(K):
    sum += p.pop(0)

print(sum)
