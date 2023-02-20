n = int(input())
s = list(map(int,input().split()))
l = sorted(s,reverse=True)
t = sum(s)//2+1
sum = 0
c = 0
for i in range(n):
    if t>sum:
        sum = sum+l[i]
        c+=1
print(c)