# 791A - Bear and Big Brother
a,b = map(int,input().split())
count = 0
for i in range(10):
    a = a*3
    b = b*2
    count+=1
    if a>b:
        break
print(count)