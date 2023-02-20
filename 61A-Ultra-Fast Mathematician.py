# Ultra-Fast Mathematician 

n = list(input())
k = list(input())
l=[]
for i in range (len(n)):
    if n[i] == k[i]:
        l.append('0')
    else:
        l.append('1')
print(''.join(l))