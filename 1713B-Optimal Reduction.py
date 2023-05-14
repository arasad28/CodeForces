t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    
    inc = 1
    while inc < n and a[inc-1] <= a[inc]:
        inc += 1
    
    dec = 1
    while dec < n and a[n-dec] <= a[n-dec-1]:
        dec += 1

    if inc+dec >= n:
        print('YES')
    else:
        print('NO')
