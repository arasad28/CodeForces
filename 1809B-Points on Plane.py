import math
t = int(input())

for i in range(t):
    n = int(input())
    rslt =int(math.sqrt(n))
    while rslt*rslt > n:
        rslt -= 1
    while rslt*rslt < n:
        rslt += 1
    print(rslt-1)
