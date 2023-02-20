n =int(input())
for i in range(n):
    p = int(input())

    if p < 3:
        print(0)
    elif p % 2 == 0:
        print( p//2 -1)
    else:
        print( p//2)

