n,k = map(int,input().split())
a = list(map(int,input().split()))

cnt = 0
for i in range(n):
    if (5-a[i]) >= k:
        cnt += 1
print(int(cnt/3))
