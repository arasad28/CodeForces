n =int( input())

l1 = []
l2 = []
res = 0
for i in range(n):
    p,q = map(int,input().split())
    l1.append(p)
    l2.append(q)

for i in range(n):
    for j in range(n):
        if l1[i] == l2[j]:
            res += 1

print(res)
print(l1)
print(l2)
