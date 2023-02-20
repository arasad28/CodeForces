n,m = map(int,input().split())

cnt = 0
ial = 1

p = list(map(int,input().split()))
for i in range(m):
    if p[i] >= ial:
        cnt += p[i] - ial
        ial = p[i]
    else:
        cnt+= n - (ial - p[i])
        ial = p[i]
    
print(cnt)

#B. Xenia and Ringroad
#https://codeforces.com/problemset/problem/339/B
