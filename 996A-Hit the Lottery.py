n = int(input())

cnt = 0
rem = n

for i in range(n):
    if rem >= 100:
        cnt += rem//100
        rem = rem % 100
    elif rem < 100 and rem >=20:
        cnt += rem//20
        rem = rem % 20
    elif rem < 20 and rem >= 10:
        cnt += rem // 10
        rem = rem % 10
    elif rem < 10 and rem >= 5:
        cnt += rem//5
        rem = rem % 5
    elif rem < 5 and rem >= 1:
        cnt += rem //1
        rem = rem % 1
    else:
        break
print(cnt)


