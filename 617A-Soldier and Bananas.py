# 617A - Elephant
n = int(input())
if n == 1 or n ==2 or n== 3 or n==4 or n==5:
    print(1)
elif n%5 == 0:
    print(n//5)
else:
    print((n//5)+1)