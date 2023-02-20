n,h = map(int,input().split())
l = list(map(int,input().split()))
sum = 0
sum1 = 0
for i in range(n):
    if l[i]>h and l[i]%h==0:
        sum = sum + l[i]//h
    elif l[i]>h and l[i]%h !=0:
        sum = sum + l[i]//h+1
    elif l[i]<h or l[i] == h:
        sum+=1
print(sum)