n,m,a,b = map(int,input().split())

if m*a <= b:
    ans = n*a
else:
    ans = (n//m)*b + min ((n%m)*a,b)
print(int(ans))
#https://codeforces.com/problemset/status?my=on

#if b == a/2 or a == b/2: 
#    print(n*a)
#elif b > a and a > b/2:
#    x = m*b
#    y = n - 2*m
#    x += y*a
#    print(x)
#else:
#    if n%m !=0:
#        p = (n//m) +1
#        x = p*b
#        print(x)
#    else:
#        p = (n//m)
#        x = p*b
#        print(x)
#
