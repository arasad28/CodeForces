n,l = map(int,input().split())

a = list(map(int,input().split()))

a.sort()

d = 2 * max(a[0],l-a[n-1])

for i in range(1,n):
    d = max(d,(a[i]-a[i-1]))

print("{0:.10f}".format(d/2))

#https://codeforces.com/problemset/problem/492/B
#B. Vanya and Lanterns
