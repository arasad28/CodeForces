p,t = map(int,input().split())
cnt = 240-t
count = 5
sol = 0
for i in range(p):
    if cnt >= count:
        sol += 1
        cnt -= count 
        count += 5
    else:
        break

print(sol)



#A. New Year and Hurry
#https://codeforces.com/problemset/problem/750/A
