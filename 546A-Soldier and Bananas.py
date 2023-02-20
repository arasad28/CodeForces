# 546A - Soldier and Bananas
k,n,w = map(int,input().split())
 
count = 0
for i in range(1,w+1):
    count = count + i*k
n1 = count-n
if n1>=0:
    print(n1)
else:
    print(0)