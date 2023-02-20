n = int(input())

l = list(map(int,input().split()))

cnt = 0
l = sorted(l,reverse=True)
val = l[0]
for i in range(n):
    cnt += val - l[i]

print(cnt)

##https://codeforces.com/problemset/problem/758/A
#A. Holiday Of Equality
