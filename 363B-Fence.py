import sys
n,k = map(int,input().split())
h = list(map(int,input().split()))
if len(h) == 1:
    print(1)
    sys.exit()
h1 = h[:k]
cnt = sum(h1)
rslt = cnt
ind = 1
for i in range(n-k):
    rslt = rslt - h[i] + h[i+k]
    if rslt < cnt:
        cnt = rslt
        ind = i+2
print(ind)
