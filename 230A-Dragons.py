import sys
s,n = map(int,input().split())
arr = []

for i in range(n):
    x,y = map(int,input().split())
    arr.append((x,y))
arr.sort()
for i in range(n):
    if s > arr[i][0]:
        s += arr[i][1]
    else:
        print('NO')
        sys.exit()
print('YES')
