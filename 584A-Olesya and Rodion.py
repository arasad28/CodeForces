while True:
    n,t = map(int,input().split())
    if n == 1 and t == 10:
        print('-1')
        break
    elif n >= 2 and t == 10:
        print('1'*(n-1)+'0')
        break
    else:
        print(str(t)*n)
        break

