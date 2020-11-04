#参考：https://marco-note.net/abc-174-work-log/
n = int(input())
c = input()

R=c.count('R')
cnt = 0

for i in range(R):
    if c[i]=="R":
        cnt += 1
print(R-cnt)
