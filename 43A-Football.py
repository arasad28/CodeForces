n = int(input())
x = []
y = []
for i in range(n):
    p = input()
    if i == 0:
        x.append(p)
    elif x[0] == p:
        x.append(p)
    else:
        y.append(p)

if len(x) > len(y):
    print(x[0])
else:
    print(y[0])

#https://codeforces.com/problemset/problem/43/A
#A. Football
