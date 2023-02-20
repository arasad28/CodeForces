# 116A - Tram
n = int(input())
x = 0
l=0
for i in range(0,n):
    a,b = map(int,input().split())
    x = x+b-a
    if x>l:
        l=x
print(l) 