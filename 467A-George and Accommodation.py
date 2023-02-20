n = int(input())
count = 0
for i in range(n):
    h,k = map(int,input().split())
    if k-h>=2:
        count +=1
print(count)