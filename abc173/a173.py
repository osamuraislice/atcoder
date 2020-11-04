n = int(input())

chk = n % 1000
if chk != 0:
    print(1000-chk)
else:
    print(0)
