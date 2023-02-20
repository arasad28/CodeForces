# Even Odds
n,k = map(int,input().split())
o,e = (n+1)//2,n//2

if k<=o:
    print((k*2)-1)
else:
    print((k-o)*2)

        