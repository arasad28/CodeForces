t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    a,b = map(int,input().split())

    b = min(b,a+a)
    if x < y:
        x,y = y,x
    print(y*b+(x-y)*a)
