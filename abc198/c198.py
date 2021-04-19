import math

r, x, y = map(int, input().split())

d = math.sqrt(x**2 + y**2)

if d == r:
    print(1)
elif 2*r > d:
    print(2)
else:
    print(math.ceil(d/r))

