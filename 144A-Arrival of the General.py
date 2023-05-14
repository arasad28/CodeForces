n = int(input())
l = list(map(int,input().split()))

l1 = l[::-1]

mi = min(l1)
ma = max(l)

p = l1.index(mi)
z = l.index(ma)

miv = len(l)-1-p
mav = z
cnt1 = len(l)-1-miv
if miv < mav:
    print(cnt1+mav-1)
else:
    print(cnt1+mav)
