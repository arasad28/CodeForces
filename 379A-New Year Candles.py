a,b = map(int,input().split())
cnt = a
rslt = a
for i in range(a):
    if cnt >= b:
        x = cnt//b
        rslt = rslt + x
        cnt = x + (cnt - x*b)
print(rslt)


#https://codeforces.com/problemset/problem/379/A
#379A - New Year Candles 
