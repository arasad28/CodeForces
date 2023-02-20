n = int(input())

for i in range(n):
    t = int(input())
    x = t//2
    lst1 = []
    lst2 = []
    if x % 2 == 0 and x >= 2:
        print('YES')
        for j in range(2,(2*x)+1):
            if j%2 == 0:
                lst1.append(j)
        for k in range(1,(2*x)-1):
            if k % 2 != 0:
                lst2.append(k)
        p = sum(lst1)
        q = sum (lst2)
        r = p - q
        lst2.append(r)
        print(*(lst1+lst2))
    else:
        print('NO')

#https://codeforces.com/problemset/problem/1343/B
#B. Balanced Array
# using * for without list result
