# 266A - Stones on the Table
n = int(input())
a = str(input())
count = 0
for i in range(1,n):
    if a[i] == a[i-1]:
        count+=1
print(count)