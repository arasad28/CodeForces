a,b = map(int,input().split())

if a > b:
    r = b
    b = (a-b)//2
elif b > a:
    r = a
    b = (b-a)//2
else:
    r = a
    b = 0
    

print(f"{r} {b}")


#https://codeforces.com/problemset/problem/581/A
#Vasya the Hipster
