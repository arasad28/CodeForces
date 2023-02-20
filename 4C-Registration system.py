n = int(input())
d = {}
for i in range(0,n):
    s = input()
    if s in d:
        print(s+str(d[s]))
        d[s] +=1

#https://codeforces.com/problemset/problem/4/C
