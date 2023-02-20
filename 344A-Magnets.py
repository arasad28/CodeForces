# 344A - Magnets

n = int(input())
a=[]
c=1
for i in range (1,n+1):
    a.append(input())
    if i>1:
        if a[i-1] != a[i-2]:
            c+=1
print(c)
