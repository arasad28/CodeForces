m = int(input())
a =list(map(int,input().split()))
n = int(input())
b = list(map(int,input().split()))
a.sort(),b.sort()
cnt = 0
for i in range(m):
    for j in range(n):
        if abs(a[i] - b[j]) <= 1:
            b[j] = 1000
            cnt += 1
            break
print(cnt)
