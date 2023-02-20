n = int(input())
x = list(map(int,input().split()))
x.sort()
x1 = x[len(x)-1]
q = int(input())
l = []
for i in range(q):
    p = int(input())
    cnt = 0
    for j in range(n):
        if p >= x1:
            cnt = n
            break
        elif p >= x[j]:
            cnt += 1
        else:
            break
    print(cnt)
