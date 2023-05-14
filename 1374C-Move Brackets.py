t = int(input())
for _ in range(t):
    n = int(input())
    s = str(input())
    cnt = 0
    bal = 0
    for i in range(n):
        if s[i] == '(':
            bal += 1
        else:
            bal -= 1
            if bal < 0:
                cnt += 1
                bal = 0
    print(cnt)
