t = int(input())
for i in range(t):
    n,k = map(int,input().split())
    
    cnt = (k-1)/(n-1)
    rslt = cnt + k
    print(int(rslt))
