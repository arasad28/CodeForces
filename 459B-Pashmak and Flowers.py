t = int(input())
a =list(map(int,input().split()))

mx = max(a)
mn = min(a)

t1 = 0
t2 = 0

for e in a:
    if e == mx:
        t1 += 1
    if e == mn:
        t2 += 1
print(mx - mn, end =" ")
if mn == mx:
    print(int(t*(t-1) / 2))
else:
    print(int(t1*t2))

