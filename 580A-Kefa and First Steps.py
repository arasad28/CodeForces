# 580A - Kefa and First Steps

n = int(input())
s = list(map(int,input().split()))
best = 0
last = 0
counter = 0
for i in s:
    if i<last:
        best = max(best,counter)
        counter = 0
    counter +=1
    last = i
print(max(best,counter))

