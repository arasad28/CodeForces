# 200B - Drinks

n = int(input())
p = list(map(int,input().split()))
count = 0
for i in range(n):
    count = count + p[i]
s = (count)/n
print('%.12f' % s)