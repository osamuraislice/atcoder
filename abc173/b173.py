n = int(input())

c = []
for i in range(n):
    c.append(input())

ac = c.count("AC")
wa = c.count("WA")
tle = c.count("TLE")
re = c.count("RE")

print("AC x", ac)
print("WA x", wa)
print("TLE x", tle)
print("RE x", re)
