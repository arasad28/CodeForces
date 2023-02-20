# HQ9+
n = str(input())
l = list('HQ9')
l1 = [i for i in n if i in l]
if l1:
    print('YES')
else:
    print('NO')