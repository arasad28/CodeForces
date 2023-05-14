t = int(input())

for i in range(t):
    n = int(input())
    s = list(map(int,input().split()))
    a = []
    cnt = 0
    for j in range(n):
        if j!=0 and sum(a) !=0 and s[j] == 0:
            cnt += max(a)
            a.remove(max(a))
        else:
            a.append(s[j])
    print(cnt)
