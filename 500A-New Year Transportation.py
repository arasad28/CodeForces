n,t = map(int,input().split())
d = list(map(int,input().split()))
i = 1
cnt = 1
while i <= n:
    if cnt == t:
        print('YES')
        break
    cnt += d[i-1]
    i = cnt
    if cnt > t:
        print('NO')
        break   


#https://codeforces.com/problemset/problem/500/A
#A. New Year Transportation
