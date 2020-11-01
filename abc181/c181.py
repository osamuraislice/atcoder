"""
TIPS
roundで丸めないと、WAになってしまう。
整数型と小数型を、Pythonは意識しなくて便利だけど、ハマるとわからないね。
今後もround(xxx, 10)くらいで丸めるとよさそう
"""

n = int(input())
x = []
y = []
for i in range(n):
    c = list(map(int, input().split()))
    x.append(c[0])
    y.append(c[1])


flg = 0
zero = 1
for i in range(n - 2):
    for j in range(i+1, n-1):
        if 0 != (x[j] - x[i]):
            a = (y[j] - y[i]) / (x[j] - x[i])
            zero=1
        else:
            a = 0
            zero=0
        if zero != 0:
            b = y[j] - a * x[j]
        else:
            b = x[j]

        for k in range(j+1, n):
            if zero != 0:
                if y[k] == round(a * x[k] + b, 10):
                    flg = 1
#                    print("xi:",x[i]," yi:",y[i]," xj:",x[j]," yj:",y[j], "xk:",x[k]," yk:",y[k])
#                    print("a:",a,"  b:",b)
#                    print("yes_chk")
#                    print()
                    break
            else:
                if b == x[k]:
                    flg = 1
#                    print("xi:",x[i]," yi:",y[i]," xj:",x[j]," yj:",y[j], "xk:",x[k]," yk:",y[k])
#                    print("a:",a,"  b:",b)
#                    print("yes_zero")
#                    print()
                    break

        if flg == 1:
            break

if flg == 1:
    print("Yes")
else:
    print("No")
