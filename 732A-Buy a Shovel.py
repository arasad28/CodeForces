x,y = map(int,input().split())

cnt = 1
res = 1
p = x
for i in range(100):
    res = (p//10)*10
    if res == p or (res+y) == p:
        break
    else:
        cnt += 1
        p = x*cnt

print(cnt)

#https://codeforces.com/problemset/problem/732/A
#A. Buy a Shovel
