n,m = map(int,input().split())

if m > n:
    x = -1
else:
    rlt = n/2
    if (n/2)%m ==0 and n%2 ==0:
        x = rlt
    elif (n/2)%m == 0  and n%2 != 0:
        rlt += m
        x = rlt
    else:
        rlt += m - (n/2)%m
        x = rlt
print(int(x))
