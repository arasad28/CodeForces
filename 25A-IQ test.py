n = int(input())
m = map(int,input().split())
m = list(m)
even = 0
odd = 0
idexEven = 0
idexOdd = 0
for i in range (n):
    if m[i]%2 == 0:
        even += 1
        idexEven = m.index(m[i])
    else:
        odd += 1
        idexOdd = m.index(m[i])

if even == 1:
    print(idexEven+1)
else:
    print(idexOdd+1)
